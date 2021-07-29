#this is a guess the number game
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask your player to guess 6 time
for guessTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('Your number is too high')
    else: 
        break
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses! ')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
 