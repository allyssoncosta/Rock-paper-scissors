import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number beetwen 1 and {x}:  '))
        if guess < random_number:
            print('sorry, guess again. Too low. ')
        elif guess > random_number:
            print('sorry, guess again. Too high. ')
            
            
    print(f' Yay, Congrats. You guessed the number {random_number}, cool. ')
guess(10)



    
    
