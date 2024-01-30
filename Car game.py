command = " "
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car has already started!")
        else:
            started = True
            print("The car has started! Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("The car has stopped")
    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - quit""")
    elif command == "quit":
        break
    else:
        print("sorry, i don't understand that.")

