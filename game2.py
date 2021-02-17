#imports
import time

#Displays the choices
def choices():
    print('''    Press 1 to start a new game.
    Press 2 to view credits.
    Press 3 to reset progress.
    Press 4 to go to a saved game.
    Press 5 to view stats.
    Press 6 to quit.''')
    choice = input()
    
#Main Menu Choice
    if choice.isnumeric() == False:
        print("Not a choice. Please try again.")
        choices()
    else:
        #Start Game
        if int(choice) == 1:
            print('Starting Game...')
            time.sleep(1)
            scenes()
        #Credits
        elif int(choice) == 2:
            print('Made by snoozingnewt 2021 all rights reserved.')
            time.sleep(1)
            choices()
        #Reset
        elif int(choice) == 3:
            money = 0
            life = 100
            itemstate = 1
            scene = 1
            scene = scene-1
            choices()
        #Import Saved Game
        elif int(choice) == 4:
            thirdchoices()
        #View Stats
        elif int(choice) == 5:
            print('Deaths: '+deaths)
            print('Itemstate: WIP ')
            print('Gamestate: WIP')
            choices()
        #Quit
        elif int(choice) == 6:
            exit
        #Else
        else:
            print("Not a choice. Please try again.")
            choices()
#In-game choices
def secondchoices():
    global life
    print('''    Press 1 to continue.
    Press 2 to quit.
    Press 3 to get your gamestate and itemstate.
    Press 4 to get your health.
    ''')
    secondchoice = input()
    if secondchoice.isnumeric() == False:
        print("Not a choice. Please try again.")
        secondchoices()
    #Continue
    if int(secondchoice) == 1:
        pass
    #Quit
    elif int(secondchoice) == 2:
        print("Gamestate: "+str(scene)+". Itemstate: "+str(itemstate))
        print('You have quit the game.')
        exit
    #Stats
    elif int(secondchoice) == 3:
        print("Gamestate: "+str(scene)+". Itemstate: "+str(itemstate))
        secondchoices()
    elif int(secondchoice) == 4:
        print(life)
        secondchoices()
    #Else
    else:
        print("Error.")
        secondchoices()
#Save choices
def thirdchoices():
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    global itemstate
    global scene
    scene = 1
    global thirdchoice
    print('''    Enter your gamestate. (A number)''')
    #Inputs
    firstthirdchoice = input()
    if firstthirdchoice.isnumeric() == False:
        print("Not a choice. Please try again.")
        thirdchoices()
    else:
        thirdchoice = int(firstthirdchoice)
    print('''    Enter your itemstate. (A number)''')
    ffourthchoice = input()
    if ffourthchoice.isnumeric() == False:
        print("Not a choice. Please try again.")
        thirdchoices()
    else:
        fourthchoice = int(ffourthchoice)
    #Determines scene
    scenesave()
    #Determines items
    itemstate = 1
    for i in range(1,13):
        if fourthchoice % (num4**i) == 0:
            itemstate = itemstate*7
        if fourthchoice % (num3**i) == 0:
            itemstate = itemstate*5
        if fourthchoice % (num2**i) == 0:
            itemstate = itemstate*3
        if fourthchoice % (num1**i) == 0:
            itemstate = itemstate*2

    #If loading a game that just started
    if scene == 0:
        print("Start a new game!")
        choices()
    #Else
    else:
        scenes()

#Determines Scene
def scenesave():
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    global scene
    global thirdchoice
    if thirdchoice % num4 == 0:
        scene = scene*7
    if thirdchoice % num3 == 0:
        scene = scene*5
    if thirdchoice % num2 == 0:
        scene = scene*3
    if thirdchoice % num1 == 0:
        scene = scene*2
    else:
        scene = 0


#Different scenes of the game
def scenes():
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    global scene
    global itemstate
    #Scene 0
    if scene == 0:
        time.sleep(0.5)
        print("Welcome to the tutorial.")
        continues()
        print("You have different items. Armor, Sword, Staff, and if you win the game, you get an OP pass that will allow you to kill any enemy.")
        continues()
        print("Here's a sword. You can try checking your itemstate now.")
        print('''Alert! /!\ You now have a starter sword. It does 5 damage.''')
        itemstate = num1
        secondchoices()
        print("An enemy approaches!")
        enemy()
        secondchoices()
        scene = num1
        scenes()
    #Scene 1
    if scene == num1:
        time.sleep(0.5)
        print("Not Bad.")
        print("Now let me fight you, to see if you're worthy.")
        print("Before I do so, here's a better sword. You'll need it and a lot of good luck to win.")
        itemstate = num1**2
        print("An enemy approaches!")
        enemy()
        secondchoices()
        scene = num2
        scenes()
    #Scene 2
    if scene == num2:
        time.sleep(0.5)
        print("hi world 3")
        secondchoices()
        scene = num3
        scenes()
    #Scene 3
    if scene == num3:
        time.sleep(0.5)
        print("hi world 4")
        scene = 10918981029384981293489817395709278934

    
#Spawns in enemies
def enemy():
    num1 = 2
    global enemytype
    global enemyhealth
    global reset
    global enemydamage
    #Which enemy is spawned is determined here
    if scene == 0:
        enemytype = 1
    elif scene == num1:
        enemytype = 2
    #Different Enemies
    if enemytype == 1:
        print("You are challenged by... Training Dummy!")
        enemyhealth = 10
        enemydamage = 0
        attack()
    elif enemytype == 2:
        print("You are challenged by... The Narrator!")
        enemyhealth = 100
        enemydamage = 6
        attack()
        
        
#Player attack      
def attack():
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    global life
    global enemyhealth
    global reset
    global scene
    global maxlife
    global enemydamage
    mode = input("Press a to attack, r to restart, and d to passively regain health.")
    #If enemy is dead
    if enemyhealth < 0 or enemyhealth == 0:
        life = maxlife
        enemydamage = 0
        print("You Win!")
        exit
    #If you attack
    elif mode == 'a':
        if itemstate % num1**2 == 0:
            enemyhealth = enemyhealth-7
            print("Enemyhealth: "+ str(enemyhealth))
            print("Life: "+str(life))
            counterattack()
        elif itemstate % num1 == 0:
            enemyhealth = enemyhealth-5
            print("Enemyhealth: "+ str(enemyhealth))
            print("Life: "+str(life))
            counterattack()
    #If you restart
    elif mode == 'r':
        life = maxlife
        reset += 1
        enemy()
    #If you heal
    elif mode == 'd':
        life = life+liferegain
        lifetest()
        print("Enemyhealth: "+ str(enemyhealth))
        print("Life: "+str(life))
        counterattack()
    #Else
    else:
        print("Invalid. Try again.")
        attack()
#Tests to see if your life is higher than your maximum life
def lifetest():
    global life
    if life > maxlife:
        life = life-1
        lifetest()
    else:
        pass
#Enemy attack
def counterattack():
    global scene
    global enemydamage
    global life
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    life = life - enemydamage
    #If you kill the enemy
    if enemyhealth < 0 or enemyhealth == 0:
        life = maxlife
        enemydamage = 0
        print("You Win!")
        exit
    #If the enemy kills you
    elif life == 0 or life < 0:
        battleloss()
    #If none of that happens and the battle is still going
    else:
        attack()
#If you die
def battleloss():
    global deaths
    print("You lose... try again?")
    deaths += 1
    scenes()
#Continue
def continues():
    willitcontinue = input("Press any key except q to continue. q will quit the game.")
    if willitcontinue == 'q':
        exit
    else:
        pass
    



#Variables 
reset = 0
money = 0
liferegain = 5
maxlife = 100
life = 100
itemstate = 1
scene = 0
deaths = 0
choices()
enemytype = 0


