import random
import time
#-------------
global itemstate
global scene
global scene
global enemytype
global life
global enemydamage
global enemyhealth
#Displays the choices
def choices():
    print('''    Press 1 to start a new game.
    Press 2 to view credits.
    Press 3 to reset progress.
    Press 4 to go to a saved game.
    Press 5 to view stats.
    Press 6 to quit.''')
    choice = int(input())

#Choice sorter
    if choice == 1:
        print('Starting Game...')
        time.sleep(1)
        scenes()
    elif choice == 2:
        print('Made by snoozingnewt 2021 all rights reserved.')
        time.sleep(1)
        choices()
    elif choice == 3:
        money = 0
        life = 100
        itemstate = 1
        scene = 1
        scene = scene-1
        choices()
    elif choice == 4:
        thirdchoices()
    elif choice == 5:
        print('na')
        choices()
    elif choice == 6:
        exit
    else:
        print("Not a choice. Please try again.")
        choices()
    
def secondchoices():
    global life
    print('''    Press 1 to continue.
    Press 2 to quit.
    Press 3 to get your gamestate and itemstate.
    Press 4 to get your health.
    ''')
    secondchoice = int(input())
    if secondchoice == 1:
        pass
    elif secondchoice == 2:
        print("Gamestate: "+str(scene)+". Itemstate: "+str(itemstate))
        print('You have quit the game.')
    elif secondchoice == 3:
        print("Gamestate: "+str(scene)+". Itemstate: "+str(itemstate))
        secondchoices()
    elif secondchoice == 4:
        print(life)
        secondchoices()
    else:
        print("Error.")
        secondchoices()

def thirdchoices():
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    global itemstate
    global scene
    global scene
    print('''    Enter your gamestate. (A number)''')
    thirdchoice = int(input())
    print('''    Enter your itemstate. (A number)''')
    fourthchoice = int(input())

#game
    if thirdchoice % num4 == 0:
        scene = scene*7
    if thirdchoice % num3 == 0:
        scene = scene*5
    if thirdchoice % num2 == 0:
        scene = scene*3
    if thirdchoice % num1 == 0:
        scene = scene*2
    else:
        scene = 1

#item
    if fourthchoice % num4 == 0:
        itemstate = itemstate*7
    if fourthchoice % num3 == 0:
        itemstate = itemstate*5
    if fourthchoice % num2 == 0:
        itemstate = itemstate*3
    if fourthchoice % num1 == 0:
        itemstate = itemstate*2
    else:
        itemstate = 1
    scene = scene
#start
    if scene == 1:
        print("Start a new game!")
        choices()
    else:
        scene = scene
        scenes()





def scenes():
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    global scene
    global itemstate
    if scene == 0:
        time.sleep(0.5)
        print("Welcome to the tutorial.")
        print("You have different items. Armor, Sword, Staff, and if you win the game, you get an OP pass that will allow you to kill any enemy.")
        print("Here's a sword. You can try checking your itemstate now.")
        print("You now have a starter sword. It does 5 damage.")
        itemstate = 2
        secondchoices()
        print("An enemy approaches!")
        enemy()
        
        scene = num1
        secondchoices()
        scenes()
    if scene == num1:
        time.sleep(0.5)
        print("Not Bad.")
        scene = num2
        secondchoices()
        scenes()
    if scene == num2:
        time.sleep(0.5)
        print("hi world 3")
        scene = num3
        secondchoices()
        scenes()
    if scene == num3:
        time.sleep(0.5)
        print("hi world 4")
        scene = 69

    
    
def enemy():
    global enemytype
    global enemyhealth
    global reset
    if scene == 0:
        enemytype = 1
    #---
    if enemytype == 1:
        global enemydamage
        print("You are challenged by... Training Dummy!")
        enemyhealth = 10
        enemydamage = 0
        attack()
        
        
def attack():
    
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    global life
    global enemyhealth
    global reset
    global scene
    mode = input("Press a to attack, r to restart, and d to passively regain health.")
    if enemyhealth < 0 or enemyhealth == 0:
            scene = scene + num1
            scenes()
    if mode == 'a':
        if itemstate % num1 == 0:
            enemyhealth = enemyhealth-5
            print("Enemyhealth: "+ str(enemyhealth))
            counterattack()
    if mode == 'r':
        life = maxlife
        reset += 1
        enemy()
    if mode == 'd':
        life = life+liferegain
        lifetest()
        print("Enemyhealth: "+ str(enemyhealth))
        counterattack()
        
def lifetest():
    global life
    if life > maxlife:
        life = life-1
        lifetest()
    else:
        pass

def counterattack():
    global scene
    global enemydamage
    global life
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    if enemyhealth < 0 or enemyhealth == 0:
            scene = scene + num1
            scenes()
    life = life - enemydamage
    if life == 0 or life < 0:
        battleloss()
    else:
        attack()
        
def battleloss():
    print("You lose... try again?")
    deaths += 1
    scenes()
    
class actions:
    def __init__ (self, money, life, itemstate, scene):
        self.life = life
        self.money = money
        self.itemstate = itemstate
        self.scene = scene
    global itemstate
    global scene
    global scene


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


