import random
import time
def printText(sentence):
    for char in sentence:
        print(char,end='')
        time.sleep(0.04)
    print()

items=["Blunt Sword", "Sharp Bat", "Bent Pole", "Health Potion"]
inventory=[]
print("**Welcome to Dragon Destroyer**")
printText("The kingdom was once a beautiful place filled with peace and lots of happiness, until the dragons attacked.  They burned down all the beautiful things and left everybody scared for their lives.  Now, it is up to you to fight through the dragon’s forces and take down the lead dragon and bring peace and happiness back to the kingdom.  Good luck adventurer!")
direction=("n", "e", "s", "w")

running=True
while running:
    #Start in Library - East to Hallway
    item_1="Blunt Sword"
    print("You start in the Library")
    print("You have acquired", item_1)
    inventory.append(item_1)
    while direction !="e":
        print("You can't go that way!")
        direction=input("Choose a directoin - n, e, s, w: ")

    print("Moving east...")
    print("You enter the Hallway")

    #Hallway - South to the Dining Room
    print("You encounter a Small Dragon!")
    #Health System
    import random

    player_health=20
    enemy_health=15
    print("Player health:", player_health)
    print("Enemy health:", enemy_health)
    running=True
    while running:

        #Choose item from inventory
        print("Inventory: ", inventory)
        item=input("Choose an item from your inventory:")
        if item in inventory:
            if item=="Blunt Sword":
                player_attack=random.randint(3,5)
            elif item=="Sharp Bat":
                player_attack=random.randint(5,7)
            elif item=="Bent Pole":
                player_attack=random.randint(7,10)
            elif item=="Health Potion":
                player_health+=7
        else:
            print("No item picked")
            player_attack=0
            
        #Player attack
        player="You"
        print(player, "use", item)
        print(player, "deal", player_attack, "damage!")

        #Enemy health adjusted
        enemy1="Small Dragon"
        enemy_health-=player_attack
        print(enemy1, "health:", enemy_health)

        if(enemy_health <=0):
            print("You killed", enemy1)
            break
        
        #Enemy attack
        print(enemy1, "attacks!")
        enemy_attack= random.randint(3,6)
        print(enemy1, "deals", enemy_attack, "damage!")

        #Player health adjusted
        player_health-=enemy_attack
        print("Player health:", player_health)

        if(player_health <=0):
            print("You died")
            printText("You have failed in your adventure of killing the head Dragon and bringing peace and happiness back to the land")
            running=False
            
    print("You have found Sharp Bat!")
    item2="Sharp Bat"
    inventory.append(item2)
    
    while direction !="s":
        print("You can't go that way!")
        direction=input("Choose a direction = n, e, s, w: ")

    print("Moving South...")
    print("You enter the Dining Room")

    #Dining Room - East to the Throne Room
    print("You encounter a Tough Dragon!")
    #Health System
    import random

    player_health=20
    enemy_health=30
    print("Player health:", player_health)
    print("Enemy health:", enemy_health)
    running=True
    while running:

         #Choose item from inventory
        print("Inventory: ", inventory)
        item=input("Choose an item from your inventory:")
        if item in inventory:
            if item=="Blunt Sword":
                player_attack=random.randint(3,5)
            elif item=="Sharp Bat":
                player_attack=random.randint(5,7)
            elif item=="Bent Pole":
                player_attack=random.randint(7,10)
            elif item=="Health Potion":
                player_health+=7
                inventory.remove("Health Potion")
        else:
            print("No item picked")
            player_attack=0
            
        #Player attack
        player="You"
        print(player, "use", item)
        print(player, "deal", player_attack, "damage!")

        #Enemy health adjusted
        enemy2="Tough Dragon"
        enemy_health-=player_attack
        print(enemy2, "health:", enemy_health)

        if(enemy_health <=0):
            print("You killed", enemy2)
            break
        
        #Enemy attack
        print(enemy2, "attacks!")
        enemy_attack= random.randint(3,6)
        print(enemy2, "deals", enemy_attack, "damage!")

        #Player health adjusted
        player_health-=enemy_attack
        print("Player health:", player_health)

        if(player_health <=0):
            print("You died")
            printText("You have failed in your adventure of killing the head Dragon and bringing peace and happiness back to the land")
            running=False
            
    print("You have found Bent Pole!")
    print("You have found Health Potion!")
    item3="Bent Pole"
    inventory.append(item3)
    item4="Health Potion"
    inventory.append(item4)
    
    while direction !="e":
        print("You can't go that way!")
        direction=input("Choose a direction = n, e, s, w: ")

    print("Moving East...")
    print("You enter the Throne Room")

    #Throne Room - Boss room
    print("You encounter the head dragon!")
     #Health System
    import random

    player_health=20
    enemy_health=30
    print("Player health:", player_health)
    print("Enemy health:", enemy_health)
    while True:

        #Choose item from inventory
        print("Inventory: ", inventory)
        item=input("Choose an item from your inventory:")
        if item in inventory:
            if item=="Blunt Sword":
                player_attack=random.randint(3,5)
            elif item=="Sharp Bat":
                player_attack=random.randint(5,7)
            elif item=="Bent Pole":
                player_attack=random.randint(7,10)
            elif item=="Health Potion":
                player_health+=7
                inventory.remove("Health Potion")
        else:
            print("No item picked")
            player_attack=0
            
        #Player attack
        player="You"
        if item=="Health Potion":
            print(player, "heal for 7 health!")
        else:
            print(player, "use", item)
            print(player, "deal", player_attack, "damage!")

        #Enemy health adjusted
        enemy3="Head Dragon"
        enemy_health-=player_attack
        print(enemy3, "health:", enemy_health)

        if(enemy_health <=0):
            print("You killed", enemy3)
            printText("Congratulations! You have defeated the Head dragon! All the dragons are now fleeing the land, and peace and hapiness can be resotred once again.  Thank you for your help adventurer!")
            break
        
        #Enemy attack
        print(enemy3, "attacks!")
        enemy_attack= random.randint(5,9)
        print(enemy3, "deals", enemy_attack, "damage!")

        #Player health adjusted
        player_health-=enemy_attack
        print("Player health:", player_health)

        if(player_health <=0):
            print("You died")
            printText("You have failed in your adventure of killing the head Dragon and bringing peace and happiness back to the land.")
    running=False
