# Adventure-Game
Explore the adventure with python
1. Directory Structure
Create a directory for your project and include the following files:

Copy code
adventure_game/
│
├── README.md
├── game.py
└── .gitignore
2. README.md
Create a README.md file to describe your project. Here’s an example:

markdown
Copy code
# Adventure Game

Welcome to the Adventure Game!

This is a simple text-based adventure game where players navigate through different stages by making choices.

## How to Play

1. Run the game script `game.py`.
2. Follow the prompts to make choices and progress through the game.
3. Try different paths to discover all possible outcomes!

## Requirements

- Python 3.x

## Running the Game

To run the game, navigate to the project directory and use the following command:

```bash
python game.py
scss
Copy code

### 3. `game.py`

This is your main Python script. Copy the code you’ve written into this file.

```python
print("Welcome to the Adventure Game !!!")
name = input("Hey! What's your name? ")
print(f"Welcome {name}!\n There are some rules in this game\n--Your intuition Matters")
print("<<------------------Stage 1------------------->>")
print(f"stage 1: {name}, you are on a dirt road. It's so uncomfortable for you...")
print("\U0001F630")
print("You need to escape from this.")
answer = input("Choose Left \U0001F448 or Right \U0001F449: ")
if answer.lower() == "left":
    print("<<<---------------------Stage 2------------------------------->>>")
    print("You chose Left")
    print("After walking a mile you found a forest and a mountain.\nYou have to choose one to continue your journey.")
    ForestORMountain = input("Choose Forest or Mountain: ")
    if ForestORMountain.lower() == "forest":
        print("<<<---------------------Stage 3------------------------------->>>")
        print("You chose Forest.")
        print("You came across a Lion. Do you want to fight with it or go back?")
        FightORBack = input("Choose Fight or Back: ")
        if FightORBack.lower() == "fight":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("Unfortunately, you were eaten by the Lion.\U0001F981")
            print("You Lose..........")
            print("Had Fun!!! Play Again.")
        elif FightORBack.lower() == "back":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You walked miles and died of starvation for water\U0001F92F.")
            print("You Lose.........")
            print("Had Fun!!! Play Again.")
        else:
            print("Invalid Option. Please choose Fight or Back.")
    elif ForestORMountain.lower() == "mountain":
        print("<<<---------------------Stage 3------------------------------->>>")
        print("You recognized the mountain height is more than 1000 meters.\nYou should climb or go back to continue your journey.")
        ClimbORBack = input("Choose Climb or Back: ")
        if ClimbORBack.lower() == "climb":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You climbed far but died because of less oxygen supply\U0001F92F.")
            print("You Lose.........")
            print("Had Fun!!! Play Again.")
        elif ClimbORBack.lower() == "back":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You walked miles and died of starvation for water\U0001F92F.")
            print("You Lose.........")
            print("Had Fun!!! Play Again.")
        else:
            print("Invalid Option. Please choose Climb or Back.")
    else:
        print("Invalid Option. Please choose Forest or Mountain.")
elif answer.lower() == "right":
    print("<<<---------------------Stage 2------------------------------->>>")
    print("You chose Right")
    print("You came across a Bridge, a River, and a Haunting House. You should choose one to continue your journey.")
    BridgeORRiverORHaunting = input("Choose Bridge or River or Haunting House: ")
    if BridgeORRiverORHaunting.lower() == "bridge":
        print("<<<---------------------Stage 3------------------------------->>>")
        print("You recognized there is a Stranger standing on the bridge. Do you want to meet him or refuse and go back?")
        MeetORRefuse = input("Choose Meet or Refuse: ")
        if MeetORRefuse.lower() == "meet":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You met the stranger, and he gave you a golden box.\U0001F929")
            print("You WON!!!\nCongratulations\n","\U0001F973"*3)
            print("Had Fun???\n Play Again..")
        elif MeetORRefuse.lower() == "refuse":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You refused the stranger, and he didn't give you a golden box.")
            print("You Lose.........")
            print("Had Fun!!! Play Again.")
        else:
            print("Invalid option. Please select Meet or Refuse.")
    elif BridgeORRiverORHaunting.lower() == "river":
        print("<<<---------------------Stage 3------------------------------->>>")
        print("You recognized the river is full of alligators. Do you want to cross or go back?")
        CrossORBack = input("Choose Cross or Back: ")
        if CrossORBack.lower() == "cross":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("While crossing the river, you were eaten by alligators.\U0001F92F")
            print("You Lose.........")
            print("Had Fun!!! Play Again.")
        elif CrossORBack.lower() == "back":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You walked miles and died of starvation for water.\U0001F92F")
            print("You Lose.........")
            print("Had Fun!!! Play Again.")
        else:
            print("Invalid option. Please select Cross or Back.")
    elif BridgeORRiverORHaunting.lower() == "haunting house":
        print("<<<---------------------Stage 3------------------------------->>>")
        print("There is a psychopath in the house. Do you want to meet him or go back to continue your journey?")
        MeetORBack = input("Choose Meet or Back: ")
        if MeetORBack.lower() == "meet":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You were killed by the psychopath.")
            print("You Lose.........")
            print("Had Fun!!! Play Again.")
        elif MeetORBack.lower() == "back":
            print("<<<---------------------Stage 4------------------------------->>>")
            print("You walked miles and died of starvation for water\U0001F92F.")
            print("You Lose.........")
            print("Had Fun!!! Play Again.")
        else:
            print("Invalid option. Please select Meet or Back.")
    else:
        print("Invalid option. Please select Bridge or River or Haunting House.")
else:
    print("Invalid option. Please select Left or Right.")
4. .gitignore
Create a .gitignore file to specify files and directories that Git should ignore. For this project, you might not need to ignore much, but a basic .gitignore file can look like this:

markdown
Copy code
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
5. Initialize Git Repository
Navigate to your project directory and initialize a Git repository:

bash
Copy code
cd adventure_game
git init
Add your files to the repository:

bash
Copy code
git add .
Commit your changes:

bash
Copy code
git commit -m "Initial commit of adventure game"
6. (Optional) Publish to GitHub
Create a new repository on GitHub, and follow the instructions provided to push your local repository to GitHub.

For example:

bash
Copy code
git remote add origin https://github.com/yourusername/adventure_game.git
git push -u origin master
