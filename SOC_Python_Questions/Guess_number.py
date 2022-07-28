import random
a = input('Whats your name? ')
print(f'Hi {a}')

act_num = random.randint(1,100)
guess_count = 0 

while True:
    guess = int(input('Guess: '))
    guess_count = guess_count + 1
     # print(f'You have {guess_limit - guess_count } tries left ')
    if act_num == guess:
        print('You Win')
        break
    elif guess < act_num:
        print('Go higher')
    elif guess > act_num:
        print('Go smaller')
    else:
        continue

print(f'Thank you for playing \n {a} took {guess_count}')
