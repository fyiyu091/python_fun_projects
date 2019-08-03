import sys
import random
import smtplib
from time import perf_counter

def my_dec(fn):
    def inner(*args, **kwargs):
        start = perf_counter()
        fn(*args, **kwargs)
        end = perf_counter()
        print(f"the function running time is {end-start}")
    return inner

@my_dec
def main():
    first = ("lily", "lebron", "kobe", "shaq", "barkey")
    last = ("james", "onlione", "henderson", "williamson")

    while True:
        firstname = random.choice(first)
        lastname = random.choice(last)

        #The format function
        print("\n")
        print("{} {}".format(firstname, lastname), file=sys.stderr)
        print("\n")
        
        userinput = input("press enter to generate a new name or enter q to exit\n\n")
        if (userinput == 'q'):
            break

if __name__ == "__main__":
    main()
