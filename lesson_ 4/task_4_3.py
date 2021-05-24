#  Task 3
#  Words combination
#  Create a program that reads an input string and then creates and
#  prints 5 random strings from characters of the input string.
#  For example, the program obtained the word ‘hello’, so it should
#  print 5 random strings(words) that combine characters
#  ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
#  Tips: Use random module to get random char from string)

import random
random_word = list(input('Please, enter a word:'))
i = 1

while i <= 5:
    random.shuffle(random_word)
    shuffled_word = ''.join(random_word)
    print(str(i) + '. ' + shuffled_word)
    i += 1
