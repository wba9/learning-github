import random
word_bank = ['sheep', 'you', 'mango', 'me', 'goat', 'window', 'car', 'laptop', 'sleep', 'house', 'flower']

word = random.choice(word_bank)
attempts = 10

question = ['_'] * len(word)
while attempts > 0:
  print(f'\nCurrent word: ' + ' '.join(question))
  guess = input('Guess a letter: ').lower()

  if guess in word:
    correct_guess = False
    for i in range(len(word)):
        if word[i] == guess:
           question[i] = guess
           correct_guess = True
        
    if correct_guess:
     print('Ayy')
  else:
    attempts -= 1
    print(f'You have {attempts} left')

  if question.count('_') == 0:
       print("You guessed the word right!")
       break

if attempts == 0 and '_' in question:
   print(f'You\'ve run out of attempts. The word was {word}')








