# Football league
import random
import time
cups = ['copaamerica', 'euros']
copaamerica = ['Brazil', 'Argentina', 'Chile', 'Ecuador']
euros = ['Italy', 'Germany', 'France', 'England']


# Simulation of cup
def simulation():
    # user game sim
    t_end = time.time() + 18
    team1score = 0
    team2score = 0
    while time.time() < t_end:
        chance = random.randint(1, 1000)
        match_clock = random.randint(2, 8)
        if chance % 2 == 0:
            time.sleep(match_clock)
            team1score += 1
        else:
            time.sleep(match_clock)
            team2score += 1
        print(f'''{team1}  :  {team2}
   {team1score}    :    {team2score}''')
    if team1score > team2score:
        finalist = team1
    if team2score > team1score:
        finalist = team2
    if team1score == team2score:
        tie = random.randint(1, 4)
        if tie % 2 == 0:
            finalist = team1
        else:
            finalist = team2
    print(f'{finalist} is the winner!')
    if team1score == team2score:
        print('By penalties')
    print('They move on to the finals.')

    # AI game sim
    AI_score1 = random.randint(0, 6)
    AI_score2 = random.randint(0, 6)
    if AI_score1 > AI_score2:
        AI_finalist = userpick[0]
    if AI_score2 > AI_score1:
        AI_finalist = userpick[1]
    if AI_score1 == AI_score2:
        AI_tie = random.randint(1, 4)
        if AI_tie % 2 == 0:
            AI_finalist = userpick[0]
        else:
            AI_finalist = userpick[1]
    print(f'''-----------------------------
    The match of {userpick[0]} and {userpick[1]} finished
    {AI_score1}   :   {AI_score2} to {AI_finalist}''')
    if AI_score1 == AI_score2:
        print('By Penalties')

    # finals
    user = input(f'''The finals are going to be {finalist} against {AI_finalist}.
playing for the grand trophy of the {cup}, press enter to begin the finals sim
>''')
    t_end = time.time() + 18
    team1score = 0
    team2score = 0
    while time.time() < t_end:
        chance = random.randint(1, 1000)
        match_clock = random.randint(2, 8)
        if chance % 2 == 0:
            time.sleep(match_clock)
            team1score += 1
        else:
            time.sleep(match_clock)
            team2score += 1
        print(f'''{finalist}  :  {AI_finalist}
      {team1score}    :    {team2score}''')
    if team1score > team2score:
        winner = finalist
    if team2score > team1score:
        winner = AI_finalist
    if team1score == team2score:
        tie = random.randint(1, 4)
        if tie % 2 == 0:
            winner = finalist
        else:
            winner = AI_finalist
    print(f'{winner} win the {cup}!!!')
    if team1score == team2score:
        print('By penalties')


# selection of teams
def select_teams_sf():
    for i in range(len(userpick)):
        if (len(userpick)) == 4:
            if userpick[i-4] == user:
                chosen = i
                userpick.pop(chosen)
        else:
            if userpick[i-3] == user:
                chosen = i
                userpick.pop(chosen)


# Game
while True:
    cup = input('''Do you want to simulate CopaAmerica or the Euros? 
>''').lower()
    while True:
        if cup not in cups:
            cup = input('''Cup not in selection. Select again.
>''')
        else:
            break
    if cup == 'euros':
        userpick = euros
    if cup == 'copaamerica':
        userpick = copaamerica
    user = input(f'''Alright, choose the first team for the first semi final: 
    {userpick} ''').capitalize()
    while True:
        if user not in userpick:
            user = input('''Team not in brackets. Select again.
>''').capitalize()
        else:
            break
    select_teams_sf()
    team1 = user
    user = input(f'''Okay, who will {user} go up against: 
    {userpick} ''').capitalize()
    while True:
        if user not in userpick:
            user = input('''Team not in brackets. Select again.
>''').capitalize()
        else:
            break
    select_teams_sf()
    team2 = user
    print(f'''Great! Simulating match between {team1} and {team2} - ''')
    simulation()
    user = input('''If you want to sim another cup, press enter, if you want to quit, type "x"
>''').lower()
    if user == 'x':
        quit()
