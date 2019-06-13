import json

song1 = {}
song1['song_name'] = 'Comfortably Numb'
song1['artist'] = 'Pink Floyd'
song1['album'] = 'The Wall'

json_string = str(json.dumps(song1))
print(f"Song 1: {json_string}")
song1_keys = list(song1)
print(f"Song keys: {song1_keys}")

song2 = {}
song2[song1_keys[0]] = 'Boulevard of Broken Dreams'
song2[song1_keys[1]] = 'Green Day'
song2[song1_keys[2]] = 'American Idiot'
song2_json_str = str(json.dumps(song2))
print(f"Song 2: {song2_json_str}")