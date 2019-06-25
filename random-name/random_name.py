import sys
import random

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
