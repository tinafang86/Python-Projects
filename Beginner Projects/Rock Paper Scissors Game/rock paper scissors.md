# Rock Paper Scissors
```
ask the user to make a choice
    if the choice is invalid:
        print(Invalid choice)
    if the choice is valid:
        let the computer make a choice
        print choices(emojis)
    determine the winner
    ask the user if they want to continue
        if not, terminate the game
```

## 基礎

### 針對choice建立一個list存入

- tuple是immutable，所以會比list存放安全
- emojis是dic，後續針對key, values取出值

```python
import random
# 運用tuple immutable特性存放r,p,s，避免list被remove, append, ...
choices = ('r', 'p', 's')
emojis = {'r': '🪨',
          'p': '📋',
          's': '✂'}
```
### while true裡面放入條件：user_choice是否成立、computer choice為何？、user_choice和computer_choice比較、是否繼續遊戲

- random.randint(a, b)：產生一組數字介於a-b之間，包含a,b
- random.choice(sequence)：可以放list or tuple

```python
#檢查user_choice是否為正確輸入值
    user_choice = input('rock, Paper, or Scissors? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invalid Choice!')
        continue  # 跳過當前，回到迴圈開頭重來
    #檢查computer_choice
    computer_choice = random.choice(choices)  # choice裡面可以放list or tuple
```
- 比較輸贏
- 最後如果n，則break跳出迴圈終止遊戲
- 如果y，則不用寫continue，Python自己會回到開頭while true，符合」無窮迴圈的特性

```python
#比較輸贏
    if user_choice == computer_choice:
        print('Tie')
    elif (user_choice == 'r' and computer_choice == 's' or
          user_choice == 's' and computer_choice == 'p' or
          user_choice == 'p' and computer_choice == 'r'):
        print('You Win!')
    else:
        print('You lose')

    #是否繼續玩
    should_continue = input(
        'If you want to continue the game? (y/n): ').lower()
    if should_continue == 'n':
        break #完全跳出迴圈
```

## Moduling寫法: def
### 核心為拆解程式讓他變區塊組成，這樣之後有問題，就可以從區塊裡面去找或優化

- 1. while loop裡面的檢查使用者輸入，先檢查打包為def()
- 使用者輸入參數

```python
def get_user_choice():  # 接收參數
    while True:
        user_choice = input('rock, Paper, or Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice  # return:輸出函式，結束迴圈
        else:
            print('Invalid Choice!')
```
- 2. 顯示user_choice和computer_choice

```python

def display_choice(user_choice, computer_choice):
    print(f'You have chosen: {emojis[user_choice]}')
    print(f'Computer has chosen: {emojis[computer_choice]}')
```

- 3. 贏或輸

```python
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie')
    elif (user_choice == 'r' and computer_choice == 's' or
          user_choice == 's' and computer_choice == 'p' or
          user_choice == 'p' and computer_choice == 'r'):
        print('You Win!')
    else:
        print('You lose')
```

- 4. 玩遊戲流程

```python

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choice(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)
        # 是否繼續玩
        should_continue = input(
            'If you want to continue the game? (y/n): ').lower()
        if should_continue == 'n':
            break  # 完全跳出迴圈

```

```python 
play_game()
```