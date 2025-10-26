# loop
# ask user questions: roll the dice?
# if y->print the dice num
# if n-> thanks for playing the dice-rolling game :)
# Terminate the program
# if others -> print(invalid choice)

import random  # 亂數模組

while True:
    choice = input('roll the dice? (y/n): ').lower()
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1},{dice2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid Choice!')
        break
print('程式已完成')
