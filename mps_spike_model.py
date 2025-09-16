# mps_spike_model.py
# Educational model of daily MPS spikes via leucine-containing meals.
# See comments for literature references and parameter explanations.

import numpy as np
import matplotlib.pyplot as plt
import math

# --------------------------
# References (for thresholds/spacing)
# --------------------------
# - Leucine threshold ~2–3 g/meal: Layman (2003) J Nutr 133:S261–S267; Witard et al. (2014) AJCN 99:86–95
# - 3 h spacing beneficial vs bolus/pulse across 12 h: Areta et al. (2013) J Physiol 591:2319–2331
# - Transient "muscle full" effect: Atherton & Smith (2012) J Physiol 590:1049–1057; Burd et al. (2011) J Appl Physiol 111:1135–1145
# - Protein dose response: Moore et al. (2009) AJCN 89:161–168

LEUCINE_THRESHOLD_G = 2.5
MIN_SPACING_H = 3.0
MAX_SPACING_H = 5.0
TIME_TO_PEAK_H = 0.75
DECAY_T_HALF_H = 1.0
AMPLITUDE_EXPONENT = 0.6

def refractory_scale(dt_h: float) -> float:
    if dt_h >= MIN_SPACING_H:
        return 1.0
    return max(0.0, dt_h / MIN_SPACING_H)

def make_time_grid(start_h=6.0, end_h=24.0, step_min=5):
    return np.arange(start_h, end_h + step_min/60.0, step_min/60.0)

def feeding_kernel(t, t0, time_to_peak_h=TIME_TO_PEAK_H, decay_t_half_h=DECAY_T_HALF_H):
    k = np.zeros_like(t)
    rise = (t >= t0) & (t < t0 + time_to_peak_h)
    decay = t >= t0 + time_to_peak_h
    k[rise] = (t[rise] - t0) / time_to_peak_h
    lam = math.log(2) / decay_t_half_h
    k[decay] = np.exp(-lam * (t[decay] - (t0 + time_to_peak_h)))
    return k

def mps_response_from_feeding(leu_g, over_threshold_g, scale, t, t0):
    amp = (max(0.0, over_threshold_g)) ** AMPLITUDE_EXPONENT
    return scale * amp * feeding_kernel(t, t0)

def simulate_day(feedings, start_h=6.0, end_h=24.0, step_min=5):
    t = make_time_grid(start_h, end_h, step_min)
    load = np.zeros_like(t)
    mps = np.zeros_like(t)
    last_trigger_time = -1e9
    triggers = []
    for f in sorted(feedings, key=lambda x: x["time_h"]):
        dt = (f["time_h"] - last_trigger_time) if last_trigger_time > -1e6 else 1e9
        over = f["leucine_g"] - LEUCINE_THRESHOLD_G
        triggered = f["leucine_g"] >= LEUCINE_THRESHOLD_G
        att = refractory_scale(dt) if triggered else 0.0
        load += f["leucine_g"] * feeding_kernel(t, f["time_h"])
        if triggered:
            mps += mps_response_from_feeding(f["leucine_g"], over, att, t, f["time_h"])
            if att > 0.0:
                last_trigger_time = f["time_h"]
        triggers.append((f["time_h"], f["leucine_g"], triggered and att > 0.0, att))
    return t, load, mps, triggers

def hhmm_str(h_float):
    h = int(h_float); m = int(round((h_float - h) * 60))
    return f"{h:02d}:{m:02d}"

def demo():
    feedings = [
        {"time_h": 8.5,  "leucine_g": 2.6, "label": "Breakfast"},
        {"time_h": 13.0, "leucine_g": 3.0, "label": "Whey"},
        {"time_h": 16.5, "leucine_g": 3.5, "label": "Post‑workout"},
        {"time_h": 21.5, "leucine_g": 2.8, "label": "Casein"},
    ]
    t, load, mps, triggers = simulate_day(feedings, start_h=6.0, end_h=24.0, step_min=3)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(t, load, label="AA/leucine availability (rel.)")
    ax.plot(t, mps, label="MPS response (a.u.)")
    ax.axhline(LEUCINE_THRESHOLD_G, linestyle="--", linewidth=1, label=f"Leucine threshold ≈ {LEUCINE_THRESHOLD_G:g} g/meal")
    for (time_h, leucine_g, did_trigger, att), f in zip(triggers, sorted(feedings, key=lambda x: x['time_h'])):
        ax.scatter([time_h], [leucine_g], s=60, marker='^')
        txt = f'{f["label"]}\n{hhmm_str(time_h)} | Leu {leucine_g:g} g'
        if did_trigger:
            txt += (f"\nTriggered (atten x{att:.2f})" if att < 1.0 else "\nTriggered")
        else:
            txt += ("\nAttempted trigger (blunted)" if leucine_g >= LEUCINE_THRESHOLD_G else "\nBelow threshold")
        ax.annotate(txt, (time_h, leucine_g), xytext=(5, 12), textcoords="offset points", fontsize=8)
    trigger_times = [time_h for (time_h, _, did, _) in triggers if did]
    for tt in trigger_times:
        ax.axvspan(tt, tt + MIN_SPACING_H, alpha=0.08)
        ax.axvspan(tt + MIN_SPACING_H, tt + MAX_SPACING_H, alpha=0.03)
    ax.set_xlabel("Clock time (h since 00:00)")
    ax.set_ylabel("Relative availability / MPS (a.u.)")
    ax.set_title("Daily MPS Spikes (Leucine threshold & refractory windows)")
    ax.legend(loc="upper right"); ax.set_xlim(6,24); plt.tight_layout(); plt.show()

if __name__ == "__main__":
    demo()
