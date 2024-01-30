 #leaderboard
import random
usernames = ['Felipe', 'felyolo', 'idont', 'udo', 'hamzah']
scores = [182, 924, 301, 992, 5302]

def game():
    user = ('Logged in! Press Enter to play. "x" to quit')
    if user == 'x':
        print('This is the final leaderboard')
        for i in range(len(usernames)):
            print(usernames[i], ':', scores[i])
            break
    else:
        for i in range(len(usernames)):
            print(usernames[i], ':', scores[i])
        while True:
            user = input('Press enter! "x" to quit.')
            if user == 'x':
                print('This is the final leaderboard')
                for i in range(len(usernames)):
                    print(usernames[i], ':', scores[i])
                user = input('')
                quit()
             # Adding score to selected username and printing
            score = random.randint(0,200)
            scores[foundit] += score
            print(usernames[foundit])
            print(scores[foundit])

while True:
     # finding position of username
    searchname = input('Input username: ')
    foundit = -1
    for i in range(len(usernames)):
        if usernames[i] == searchname:
            foundit = i

    if foundit > -1:
        game()
    else:
        print('New user added')
        usernames.append(searchname)
        scores.append(0)
        foundit = -1
        for i in range(len(usernames)):
            if usernames[i] == searchname:
                foundit = i
        game()
