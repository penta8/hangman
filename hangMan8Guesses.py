import random
import os


def loadWords(text):
    f = open(text, 'r')
    words = f.read().split(' ')
    f.close
    return words


def randomWord(words):
    return random.choice(words)


def display(result):
    print('Word:    ' + ' '.join(result['guessedWord']))
    print('Guesses: ' + str(result['guesses']))
    print('Misses:  ' + ','.join(result['misses']))
    print('Correct: ' + ','.join(result['correct']))


def initResult(word):
    result = {'word': word, 'guesses': 0, 'misses': [],
              'correct': [], 'guessedWord': ['_'] * len(word)}
    return result


def getIndexes(letter, word):
    indexes = []
    for index in range(len(word)):
        if word[index] == letter:
            indexes.append(index)
    return indexes


def replace(letter, indexes, letters):
    for index in range(len(letters)):
        if index in indexes:
            letters[index] = letter

word   = randomWord(loadWords('words.txt'))
word   = 'letter'
result = initResult(word)
win    = False

while result['guesses'] < 8:
    display(result)
    letter = input('Select a letter: ').lower()

    os.system('clear')
    if letter not in 'abcdefghijklmnopqrstuvwxyz':
        print(letter + ' is not a valid letter. TRY AGAIN')
        continue
    elif letter in result['correct'] or letter in result['misses']:
        print('You already chose that letter.')
        continue
    elif letter in result['word'].lower():
        result['correct'].append(letter)
        indexes = getIndexes(letter, result['word'])
        replace(letter, indexes, result['guessedWord'])
    else:
        result['misses'].append(letter)

    result['guesses'] += 1

    if result['word'].lower() == ''.join(result['guessedWord']):
        win = True
        break

display(result)
if win:
    print('CONGRATULATIONS YOU WON!!!')
else:
    print('YOU LOST')
    print('The correct word is ' + result['word'])
