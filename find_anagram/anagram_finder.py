import load_file

def anagram_finder(input_name):

    word_list = load_file.load("dictionary.txt")

    anagram_list = []

    for word in word_list:
        if word != input_name:
            if sorted(word) == sorted(input_name):
                anagram_list.append(word)

    if len(anagram_list) == 0:
        print("there is no anagram of the input name")
    else:
        print("anagram is list: ", *anagram_list, sep='\n')