import multiprocessing as mp
import time

def add_two_ints(a=2,b=2):
    # If a is even, introduce a sleep that is half as long as the value of 'a'
    if a % 2 == 0:
        time.sleep(a/2)
    print(f"{a}+{b}={a+b}")

class IntegerPair:
    def __init__(self, a=2, b=2):
        self.a = a
        self.b = b

def main():
    print("Number of processors: ", mp.cpu_count())

    # All processes will be contained within the following array
    procs = []

    # Simple proc without explicit args
    procs.append(mp.Process(target=add_two_ints))
    procs[0].start()

    # Create a list of IntegerPairs
    int_pairs = []
    for i in range(10):
        int_pairs.append(IntegerPair(i, i+1))
    
    # Create a proc for each IntegerPair
    for i in range(len(int_pairs)):
        procs.append(mp.Process(target=add_two_ints, args=(int_pairs[i].a, int_pairs[i].b)))
        procs[i+1].start()

    # Complete all processes
    for proc in procs:
        proc.join()

if __name__ == '__main__':
    main()