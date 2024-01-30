#this is car game
started = False
gas_count = 0
gas_limit = 2
input('You are about to start the game, \n Are you ready? Press Enter to start ')
while gas_count < gas_limit:
    while True:
        user_input = input('Type "help" for the instructions''\n >').lower()
        if user_input == 'help':
            print(''' To start the car - "start" 
                To stop the car - "stop"
                To refuel - "gas"
                To quit the game - "quit"''')
        elif user_input == 'start':
            if started:
                print('Car already started!')
            elif not started:
                print('Car moving!')
                started = True
        elif user_input == 'stop':
            if started:
                print('You stopped!')
                started = False
            elif not started:
                print('You already stopped!!')
        elif user_input == 'quit':
            print('Okay, Bye.')
            break
        elif user_input == 'gas':
            if gas_count == 0:
                gas_count = 1
                print('You refilled, only 1 refill left!''\n''if gas is refilled more than 2 times your car will stop working!')
            elif gas_count == 1:
                gas_count = 2
                print('Thats your last refill, one more and your car is totalled!')
            elif gas_count == 2:
                print('Nice one, game over!')
                gas_count += 1
                break
        elif user_input == 'quit':
            print('You Quit!')
            break
        else:
            print('Sorry, i didnt understand that.')