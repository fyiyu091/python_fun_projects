import argparse
import anagram_finder

parser = argparse.ArgumentParser(description='give a name and I will find the anagram for you!')

parser.add_argument('name', help = 'the name that you want the anagram for')

args = parser.parse_args()

anagram_finder.anagram_finder(args.name)