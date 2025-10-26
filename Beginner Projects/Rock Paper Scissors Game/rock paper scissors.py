# ask the user to make a choice
# if the choice is invalid:
#     print(Invalid choice)
# if the choice is valid:
#     let the computer make a choice
#     print choices(emojis)
# determine the winner
# ask the user if they want to continue
# if not, terminate the game

import random
# 運用tuple immutable特性存放r,p,s，避免list被remove, append, ...
choices = ('r', 'p', 's')
emojis = {'r': '🪨',
          'p': '📋',
          's': '✂'}

while True:
    user_choice = input('rock, Paper, or Scissors? (r/p/s): ').lower()

    if user_choice not in choices:
        print('Invalid Choice!')
        continue  # 跳過後面的程式碼，回到最前面

    computer_choice = random.choice(choices)  # choice裡面可以放list or tuple

    print(f'You have chosen: {emojis[user_choice]}')
    print(f'Computer has chosen: {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie')
    elif (user_choice == 'r' and computer_choice == 's' or
          user_choice == 's' and computer_choice == 'p' or
          user_choice == 'p' and computer_choice == 'r'):
        print('You Win!')
    else:
        print('You lose')

    should_continue = input(
        'If you want to continue the game? (y/n): ').lower()
    if should_continue == 'n':
        break
