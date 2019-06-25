import sys

def main():
    load("dictionary.txt")

def load(filename):
    try:
        with open(filename) as in_file:
            the_words = in_file.read().strip().split('\n')
            the_words = [x.lower() for x in the_words]
            return the_words
            
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()