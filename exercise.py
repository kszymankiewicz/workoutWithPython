import random

secretNumber = random.randint(1,20)
print('I am thinking about one number from the 1 to 20. You have 7 trails ')

for guessTaken in range(1,8):
    print('Take guess. ')
    guess = int(input())
    
    if guess < secretNumber:
        print('The number is too low. ')

    elif guess > secretNumber:
        print('The number is too hight. ')
    else:
        break
if guess == secretNumber:
    print('You won !!! This is guess number')
else:
    print("You lose....")
