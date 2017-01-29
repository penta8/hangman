import random
import os


def loadWords(text):
    f = open(text, 'r')
    words = f.read().split(' ')
    f.close
    return words


def randomWord(words):
    return random.choice(words)


def initHangman():
    hangman = [[' ', ' ', '_', '_', '_', '_', '\n'],
               [' ', ' ', '|', ' ', ' ', '|', '\n'],
               [' ', ' ', ' ', ' ', ' ', '|', '\n'],
               [' ', ' ', ' ', ' ', ' ', '|', '\n'],
               [' ', ' ', ' ', ' ', ' ', '|', '\n'],
               [' ', ' ', ' ', ' ', ' ', '|', '\n'],
               ['_', '_', '_', '_', '_', '|', '\n']]
    return hangman


def updateHangman(misses, hangman):
    man = {1: {'char': 'O',  'positions': [[2,2]]},
           2: {'char': '|',  'positions': [[3,2],[4,2]]},
           3: {'char': '/',  'positions': [[3,1]]},
           4: {'char': '\\', 'positions': [[3,3]]},
           5: {'char': '/',  'positions': [[5,1]]},
           6: {'char': '\\', 'positions': [[5,3]]}}
    for index in range(misses):
        for pos in man[index + 1]['positions']:
            hangman[pos[0]][pos[1]] = man[index + 1]['char']


def displayHangman(hangman):
    for row in hangman:
        for column in row:
            print(column,end='')


def display(hangman, result):
    displayHangman(hangman)
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

word    = randomWord(loadWords('words.txt'))
result  = initResult(word)
hangman = initHangman()
win     = False

while len(result['misses']) < 6:
    display(hangman, result)
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
        updateHangman(len(result['misses']), hangman)

    result['guesses'] += 1

    if result['word'].lower() == ''.join(result['guessedWord']):
        win = True
        break

display(hangman, result)
if win:
    print('CONGRATULATIONS YOU WON!!!')
else:
    print('YOU LOST')
    print('The correct word is ' + result['word'])
