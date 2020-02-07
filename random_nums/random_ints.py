from random import seed
from random import random

def main():
    list_of_fruits = ["apples", "banana", "orange"]
    seed(len(list_of_fruits))
    print(random())

    return

if __name__ == "__main__":
    main()