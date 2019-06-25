import load_file

palingrams = []
the_words = load_file.load('dictionary.txt')
for word in the_words:
    if word == word[::-1]:
        palingrams.append(word)
print(*palingrams, sep='\n')