import random
options = ['rock', 'paper', 'scissors']
wins = 0
trial = 0
print("Welcome to my game. You have 3 options: rock, paper, scissors. Enjoy and Good luck :)")
while trial < 3: #runs the succeeding lines of code three times
    trial += 1
    user_answer = input("Enter option: ").lower() #converts the user's answer to lower case to prevent crush
    comp_answer = random.choice(options)
    print(f'Computer answer: {comp_answer}')
    # checks if the users answers match those of the computer. if it does the user wins otherwise the user has to try again
    if user_answer == comp_answer:
        wins += 1
        print(f'You have {wins} wins. Noice!!!')
    else:
        print('Try again')
print(f'Total wins: {wins}')
# checks if the user has more 2 or more wins upon completion of trials. Satisfaction of that requirement grants the user victory.
if (trial == 3) and (wins >= 2):
    print("You've won congrats")
elif (trial == 3) and (wins < 2):
    print("You have lost. Comp and me wins.Ha!!!!!")