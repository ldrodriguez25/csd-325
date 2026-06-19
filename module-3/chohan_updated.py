# Luis Rodriguez
# June 18, 2026
# CSD-325 Module 3 Assignment
# Purpose: Modified Cho-Han game with updated house fee and bonus rule.
# Original source adapted from Al Sweigart's Cho-Han example.

import random, sys

JAPANESE_NUMBERS = {1:'ICHI',2:'NI',3:'SAN',4:'SHI',5:'GO',6:'ROKU'}

print('''Cho-Han

In this traditional Japanese dice game, two dice are rolled.
If you roll a total of 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000

while True:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('lr: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2

    print("CHO (even) or HAN (odd)?")
    while True:
        bet = input('lr: ').upper()
        if bet in ('CHO','HAN'):
            break
        print('Please enter either "CHO" or "HAN".')

    print(JAPANESE_NUMBERS[dice1],'-',JAPANESE_NUMBERS[dice2])
    print(dice1,'-',dice2)

    if total in (2,7):
        print(f'You rolled a total of {total} and earned a 10 mon bonus!')
        purse += 10

    correctBet='CHO' if total % 2 == 0 else 'HAN'
    if bet==correctBet:
        print('You won!',pot,'mon.')
        purse += pot
        print('The house collects a', pot*12//100, 'mon fee.')
        purse -= pot*12//100
    else:
        purse -= pot
        print('You lost!')

    if purse==0:
        print('You have run out of money!')
        sys.exit()
