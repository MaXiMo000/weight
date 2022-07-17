command = ""
started = False
while command != "quit":
    command = input("U CAN PUT HELP, START,STOP,QUIT>> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("CAR STARTED....")
    elif command == "stop":
        if not started:
            print("car already started man")
        else:
            started = False
            print("CAR STOPPED")
    elif command == "help":
        print("""START > TO START THE CAR
                 STOP > TO STOP THE CAR
                 QUIT > TO QUIT THE FUN """)

        print("JUST HOW DESPERATE ARE U ?")
    elif command == "quit":
        print("U ALREADY DONE MAN ?")
        break
    else:
        print("LOL DO WHAT U ARE ASKED FOR MAN")

