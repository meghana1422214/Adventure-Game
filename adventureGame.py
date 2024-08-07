print("Welcome to the Adventure Game !!!")
name=input("Hey!What's your name ?")
print(f"Welcome {name}!\n There are some rules in this game\n--Your intution Matters")
print("<<------------------Stage 1------------------->>")
print(f"stage 1: {name}, you are on a dirt road. It's so uncomfortable for You..")
print("\U0001F630")
print("You need to escape from this.")
answer=input("Choose Left \U0001F448 or Right \U0001F449")
if(answer.lower()=="left"):
    print("<<<---------------------Stage 2------------------------------->>>")
    print("You Choosed Left")
    print("After walking a mile you found a forest and a mountain.\nYou ahve to choose one to continue your journery.")
    ForestORMountain=input("Choose Forest or Mountain:")
    if(ForestORMountain.lower()=="forest"):
        print("<<<---------------------Stage 3------------------------------->>>")
        print("You choosed Forest.")
        print("You came across a Lion. You wanna fight with it or Go back?")
        FightORBack=input("Choose Fight or Back")
        if(FightORBack.lower()=="fight"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("Unfortunately You were eaten by Lion.\U0001F981")
            print("You Loose..........")
            print("Had Fun!!! Play Again.")
        elif(FightORBack.lower()=="back"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You walked miles and Dead with starving for Water\U0001F92F.")
            print("You Loose.........")
            print("Had Fun!!! Play Again.")
        else:
            print("Invalid Option.Please choose Fight or Back")
    elif(ForestORMountain.lower()=="mountain"):
        print("<<<---------------------Stage 3------------------------------->>>")
        print("You recognized Mountain Height is more than 1000 meters.\n You should climb or Go Back to continue your journey")
        ClimbORBack=input("Choose Climb or Back")
        if(ClimbORBack.lower()=="climb"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You Climbed far but Dead because of Less Oxygen Supply\U0001F92F.")
            print("You Loose.........")
            print("Had Fun!!! Play Again.")
        elif(ClimbORBack.lower()=="back"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You walked miles and Dead with starving for Water\U0001F92F.")
            print("You Loose.........")
            print("Had Fun!!! Play Again.")
        else:
            print("Invalid Option.Please choose Climb or Back.")
    else:
        print("Invalid Option.Please choose Forest or Mountain")
elif(answer.lower()=="right"):
    print("<<<---------------------Stage 2------------------------------->>>")
    print("You Choosed Right")
    print("You came across a Bridge, a River and a Haunting House.You should choose one to continue your journey.")
    BridgeORRiverORHaunting=input("Choose Bridge or River or Haunting House")
    if(BridgeORRiverORHaunting.lower()=="bridge"):
        print("<<<---------------------Stage 3------------------------------->>>")
        print("You recognized there is a Stranger Standing on Bridge. You wanna meet him or refuse and go back.")
        MeetORRefuse=input("Meet or Refuse")
        if(MeetORRefuse.lower()=="meet"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You met the stranger ,he gave you a gloden box.\U0001F929")
            print("You WON!!!\nCongratulations\n","\U0001F973"*3)
            print("Had Fun???\n Play Again..")
        elif(MeetORRefuse.lower()=="refuse"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You Refused the Stranger,he didn't gave a golden box to you.")
            print("You Loose.........")
            print("Had Fun!!! Play Again.")
        else:
            print("Invalid option. Please select Meet or Refuse.")
    elif(BridgeORRiverORHaunting.lower()=="river"):
        print("<<<---------------------Stage 3------------------------------->>>")
        print("You recongized River is full of Alligators.You wanna Cross or Go Back")
        CrossORBack=input("Choose Cross or Back")
        if(CrossORBack.lower()=="cross"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("While crossing the river,you were eaten by Alligators.\U0001F92F")
            print("You Loose.........")
            print("Had Fun!!! Play Again.")
        elif(CrossORBack.lower()=="back"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You walked miles and Dead with starving for Water.\U0001F92F")
            print("You Loose.........")
            print("Had Fun!!! Play Again.")
    elif(BridgeORRiverORHaunting.lower()=="haunting House"):
        print("<<<---------------------Stage 3------------------------------->>>")
        print("There is a psycopath in the House.You want to meet him or Go back to continue your journey")
        MeetORBack=input("Choose Meet Or Back:")
        if(MeetORBack.lower()=="meet"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You were Killed by psycopath.")
            print("You Loose.........")
            print("Had Fun!!! Play Again.")
        elif(MeetORBack.lower()=="back"):
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You walked miles and Dead with starving for Water\U0001F92F.")
            print("You Loose.........")
            print("Had Fun!!! Play Again.")
        else:
            print("Invalid option. Please select Meet or Back.")
    else:
        print("Invalid option. Please select Bridge or River or Haunting House.")
else:
    print("Invalid option. Please select Left or Right. ")
    

