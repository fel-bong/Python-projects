import random

crew_mates = ['red', 'blue', 'yellow', 'orange', 'black']
imposter = random.choice(crew_mates)
user = input('You are about to play Among Us, press enter to start - "quit" to quit''\n').lower()
if user == 'quit':
    exit()
member = input(f'Which member do you want to be, {crew_mates} type out your colour \n >')
if member not in crew_mates:
    while member not in crew_mates:
        print('That is not part of the crew, choose again')
        member = input('>')

print(f'''The crew consists of {len(crew_mates)} members. {crew_mates} 
You are {member}, there is going to be 1 imposter amongst you,
If you are imposter, don't tell the others! You have to sabotage them!
If you're not an imposter, you will have to guess who it is
and vote them off.''')
# if imposter
if imposter == member:
    user = input('You are the imposter!').lower()
# if crew mate
else:
    user = input('You are not the imposter, who do you think it is? Type out their colour.''\n''>').lower()
    while True:
        if user not in crew_mates:
            while user not in crew_mates:
                print('That is not part of the crew, choose again')
                user = input('>')
        elif user == imposter:
            print('0 Imposters left, you did it!')
            break
        elif user == member:
            user = input('apologies but you cant kick yourself out...  \n >')
        else:
            crew_mates.remove(user)
            if len(crew_mates) <= 2:
                print("You failed, imposter wasn't kicked, you're left alone with him!")
                break
            else:
                user = input(f'''You kicked out the wrong member, only
        {len(crew_mates)}, {crew_mates} of you remain, and one is the imposter....
        Be careful! \n try again \n >''')
