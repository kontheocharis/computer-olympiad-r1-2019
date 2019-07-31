# Q3 Constantine Theocharis, Python 3.7

digit_words = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

word = input()

for digit_word in digit_words:
    shortened_word = ''.join([c if c in digit_word else '' for c in word])
    if shortened_word == digit_word:
        print(digit_word)
        break
else:
    print('NONE')
