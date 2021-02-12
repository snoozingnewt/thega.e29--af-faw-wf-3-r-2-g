import random
import time
#-------------
global itemstate
global scene
global scene
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
    print('''    Press 1 to continue.
    Press 2 to quit.
    Press 3 to get your gamestate and itemstate.
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

def thirdchoices():
    num1 = 2
    num2 = 3
    num3 = 5
    num4 = 7
    global itemstate
    global scene
    global scene
    print('''    Enter your gamestate.''')
    thirdchoice = int(input())
    print('''    Enter your itemstate.''')
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
    if scene == 0:
        time.sleep(0.5)
        print("hi world 1")
        scene = num1
        secondchoices()
        scenes()
    if scene == num1:
        time.sleep(0.5)
        print("hi world 2")
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

    
    




class actions:
    def __init__ (self, money, life, itemstate, scene):
        self.life = life
        self.money = money
        self.itemstate = itemstate
        self.scene = scene
    global itemstate
    global scene
    global scene



money = 0
life = 100
itemstate = 1
scene = 0
choices()


