# guess the number between 1-100
# if number ->開始guess
# if a -> print invalid message


import random
# 這個隨機數字只會被製造出一個，所以放在for loop外面
correct_num = random.randint(1, 100)

while True:
    try:
        input_number = int(input('Guess the number from 1 to 100: '))
        if input_number < correct_num:
            print('Too low!')
        elif input_number > correct_num:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number!')
            break
    except ValueError:
        print('Please enter a valid number!')
