 #Two dimensional array
import random
print('Welcome to the battleship game, guess what position the ship is in')
 # making the battleship
grid1 = [["" for x in range(3)] for x in range(3)]
grid1[0][0] = 'O'
grid1[0][1] = 'O'
grid1[0][2] = 'O'
grid1[1][0] = 'O'
grid1[1][1] = 'O'
grid1[1][2] = 'O'
grid1[2][0] = 'O'
grid1[2][1] = 'O'
grid1[2][2] = 'O'
 # where the battleship will be
number1 = random.randint(0,3)
number2 = random.randint(0,3)
 # actual game
while True:
    print(grid1[0])
    print(grid1[1])
    print(grid1[2])
    user1 = int(input('Input a X Position from 0-2: '))
    user2 = int(input('Input a Y position from 0-2: '))
    if user1 == number1 and user2 == number2:
        grid1[number1][number2] = 'X'
        print(grid1[0])
        print(grid1[1])
        print(grid1[2])
        print('Congratulations, you win!')
        break
    else:
        grid1[user1][user2] = 'N'
