import collections
import logging as log

def main():
    letters = collections.deque('abc')
    letters.append('d')
    letters.appendleft('h')
    
    try:
        f = open('collections_file.txt', 'w')
        if letters[0] == 'h':
            f.write(str(letters))
        else:
            f.write('the appendleft function of deque is not working')
    except IndexError:
        print('got an IndexError')

    a = 0
    b = 5

    while a < 6:
        print('-----------------')
        try:
            a += 1
            b -= 1
            a / b
        except ZeroDivisionError:
            print('got the divisionerror')
            continue
        finally:
            print('this always exceute')
        print("main print")
    else:
        print('this else runs')

    my_list = [2,3,'d',6,9]
    for (idx, elements) in enumerate(my_list):
        print(idx, elements)

    

if __name__ == "__main__":
    main()