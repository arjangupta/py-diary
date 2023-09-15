import multiprocessing as mp
import time

def nested_busy_loop(a=20,b=2000):
    # Create a O(n^2) loop to keep the CPU busy
    c = 0
    for i in range(a):
        for j in range(1,b):
            c += i*j
            x = i^j
            y = i/j
    print("Nested busy loop complete: ", c)

class IntegerPair:
    def __init__(self, a=2, b=2):
        self.a = a
        self.b = b

def main():
    print("Number of processors: ", mp.cpu_count())

    # All processes will be contained within the following array
    procs = []

    # Simple proc without explicit args
    procs.append(mp.Process(target=nested_busy_loop))
    procs[0].start()

    # Create a list of IntegerPairs, but only as many as there are processors
    int_pairs = []
    for i in range(1, mp.cpu_count()+1):
        int_pairs.append(IntegerPair(i*10000, (i+1)*1000))
    
    # Create a proc for each IntegerPair
    for i in range(len(int_pairs)):
        procs.append(mp.Process(target=nested_busy_loop, args=(int_pairs[i].a, int_pairs[i].b)))
        procs[i+1].start()

    # Complete all processes
    for proc in procs:
        proc.join()

if __name__ == '__main__':
    main()