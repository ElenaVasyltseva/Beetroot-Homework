#  Task 1
#  Make a program that has some sentence (a string) on input
#  and returns a dict containing all unique words as keys
#  and the number of occurrences as values.


while True:
    user_text = input('Please, enter a text:').replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')
    user_text = user_text.replace('(', ' ').replace(')', ' ').replace('-', ' ').lower().split(' ')
    words_count = {}
    for word in user_text:
        if word not in words_count:
            if word == "":
                continue
            words_count[word] = 0
        words_count[word] += 1

    for key, value in words_count.items():
        print(f'{key} --> {value} time')

    question_continue = input('Do you want to check another sentence? Enter yes or no:')
    if question_continue == 'yes':
        continue
    elif question_continue == 'no':
        print('Finish')
        break
    else:
        print('Incorrect input! Finish!!')
        break
