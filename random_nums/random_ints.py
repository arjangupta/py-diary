import time
from random import seed
from random import randint

def main():
    list_of_fruits = ["apples", "banana", "orange"]
    seed(int(round(time.time() * 1000)))
    print(randint(1, len(list_of_fruits)))

    return

if __name__ == "__main__":
    main()