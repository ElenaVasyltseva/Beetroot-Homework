#  to get a string made of the first 2 and the last 2 chars from a given string

word = input()

if len(word) >= 2:
    print(word[0] + word[1] + word[-2] + word[-1])
else:
    print()
