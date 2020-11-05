import random
import sys

"""
Title: Rolebattle
Author: John Paul Bunn

Welcome to Rolebattle!
In this game you have the chance to take on the virtuous power of your favorite fantasy heroes! 
Wage war against a barrage of monsters in this turn based fighting game!

In this game, you get to choose a power, and you will fight 1-on-1 with a villainous creature! 
Will you defeat your monster?
Good luck!

"""




#GAME START STATS
playerSpeed = 3
distance = random.randint(1, 5)
actionEconomy = 2
actions = (["1", "2", "3", "4"])
playerImmobile = False
playerHealth = 50
playerAC = 10
actionEconomy = 2
monsterHealth = 20
monsterAC = 10
monsterImmobile = False
monsterActionEconomy = 2
FairyHide = 0
power = "brute"

#ACTIONS LIST
def actionSelection():
    global actions
    global playerSpeed
    playerImmobile == True
    
    print("\nChoose from your list of actions! \n")
    print("~~~~~~~~~~")
    print(actions[0])
    print(actions[1])
    print(actions[2])
    print(actions[3])
                                         
    print("Move Forward")
    print("Move Backward")
    if (playerImmobile == True):
        print("\nEscape")
    
    print("Game Exit")
    print("~~~~~~~~~~")

#Player-Action
def Action(option, power, monster):
    global playerImmobile
    global playerSpeed
    global actionEconomy
    global distance

    
    dealt = 0
    action = option.lower()
    attackroll = random.randint(1, 20)
        

            
    #End the game from the console
    if (action == "game exit"):
        sys.exit("Game ended")
            
    #Escape immobility/grapple
    elif ((action == "escape") and (playerImmobile == True)):
        actionEconomy -= 1
        playerImmobile = False
        playerSpeed = 3
        
    #Move forwad (close distance)
    elif ((action == "move forward") and (playerSpeed != 0) and (playerImmobile == False) and (distance > 1)):
        print("Successfully moved forward.")
        distance -= 1
        playerSpeed -= 1
        
    #Move backward (open distance
    elif ((action == "move backward") and (playerSpeed != 0) and (playerImmobile == False) and (distance >= 1)):
        #If they move backward within Attack of Opportunity range
        if (distance == 1):
            monsterAO(monster)
        print("Successfully moved backward.")
        distance += 1
        playerSpeed -= 1
        
    #Brute actions
    elif (power.lower() == "brute"):
        #SLASH
        if (action == "slash"):
            #If the target is within range
            if (distance == 1):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll >= monsterAC):
                    dealt = random.randint(1, 12)
                    print("Your attack hit, and dealt " + str(dealt) + " damage!")
                #If the attack misses
                else:
                    print("You swung valiantly, but you missed your target.")
            #If the target is out of range
            else:
                print("You are too far away.")
                
        #SHOVE        
        elif (action == "shove"):
            #If the target is within range
            if (distance == 1):
                actionEconomy -= 1
                #If the attack hits
                if ((attackroll+2) >= monsterAC):
                    distance += 2
                    print("You manage to shove the " + monster + "! It's pushed back 2 spaces.")
                #If the attack misses
                else:
                    print("You wrestled valiantly, but you missed your target.")
            #If the target is out of range
            else:
                print("You are too far away.")
                
        #CHARGE
        elif (action == "charge"):
            #If the target is within range
            if (distance > 1):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll-2 >= monsterAC):
                    dealt = random.randint(1, 15) + 5
                    distance = 1
                    print("Your charge hit, and dealt " + str(dealt) + " damage!")
                #If the attack misses
                else:
                    print("You gored valiantly, but you missed your target.")
            #If the target is out of range
            else:
                print("You are too close to charge!")
                
        #GRAPPLE
        elif (action == "grapple"):
            #If the target is within range
            if (distance == 1):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll+3 >= monsterAC):
                    monsterSpeed = 0
                    monsterImmobile = True
                    print("You grab hold of the " + monster + "! It can no longer move away unless it escapes your grapple.")
                #If the attack misses
                else:
                    print("You wrestled valiantly, but you missed your target.")
            #If the target is out of range
            else:
                print("You are too far away.")
        else:
            print("That is not a valid action.")
    
    #Mage actions
    elif (power.lower() == "mage"):
        
        #BLAZE
        if (action == "blaze"):
        #If the target is within range
            if ((distance == 1) or (distance == 2)):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll >= monsterAC):
                    dealt = random.randint(1, 10)
                    print("Your attack hit, and dealt " + str(dealt) + " blazing damage!")
                #If the attack misses
                else:
                    print("Your spell was elegant, but the monster held its will.")
            #If the target is out of range
            else:
                print("You are too far away.")  
                
        #DROWN
        elif (action == "drown"):
        #If the target is within range
            if (distance > 1):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll+2 >= monsterAC):
                    monsterSpeed=0
                    monsterImmobile = True
                    print("You encase the " + monster + " in a sphere of water! it is immobile until it escapes.")
                #If the attack misses
                else:
                    print("Your spell was elegant, but the monster held its will.")
            #If the target is out of range
            else:
                print("You are too close to cast this spell.")
                
        #GROUND-POUND
        elif (action == "ground-pound"):
        #If the target is within range
            if (9 > distance > 2):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll-2 >= monsterAC):
                    dealt = random.randint(1, 20)
                    print("Your attack hit, and dealt " + str(dealt) + " elemental damage!")
                #If the attack misses
                else:
                    print("Your spell was elegant, but the monster held its will.")
            #If the target is out of range
            else:
                print("You are too close to cast this spell.")
        
        #GUST
        elif (action == "gust"):
        #If the target is within range
            if (distance > 1):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll >= monsterAC):
                    dealt = random.randint(1, 8)
                    distance += 2
                    print("Your volley of wind struck true, and you dealt " + str(dealt) + " damage to the " + monster + "! It's also pushed 2 spaces back!")
                #If the attack misses
                else:
                    print("Your spell was elegant, but the monster held its will.")
            #If the target is out of range
            else:
                print("You are too close to cast this spell.")
        else:
            print("That is not a valid action.")
    #Marksman actions
    elif (power.lower() == "marksman"):
        
        #BURST
        if (action == "burst"):
        #If the target is within range
            if (1 < distance < 4):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll+2 >= monsterAC):
                    dealt = random.randint(1, 10)
                    print("Your bullet struck true. You dealt " + str(dealt) + " damage to the " + monster + "!")
                #If the attack misses
                else:
                    print("Was worth a shot, buckaroo.")
            #If the target is out of range
            else:
                if (distance == 1):
                    print("You are too close to make this shot.")
                else:
                    print("You are too far to make this shot.")
        
        #HILT-BASH
        elif (action == "hilt-bash"):
        #If the target is within range
            if (distance == 1):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll-1 >= monsterAC):
                    dealt = random.randint(1, 8)
                    print("Your bash struck true. You dealt " + str(dealt) + " damage to the " + monster + "!")
                #If the attack misses
                else:
                    print("Was worth a shot, buckaroo.")
            #If the target is out of range
            else:
                print("You are too far to make this attack.")
                
        #SNIPE
        elif (action == "snipe"):
        #If the target is within range
            if (8 > distance > 3):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll-2 >= monsterAC):
                    dealt = random.randint(5, 20)
                    print("Your signature round struck true. You dealt " + str(dealt) + " damage to the " + monster + "!")
                #If the attack misses
                else:
                    print("Was worth a shot, buckaroo.")
            #If the target is out of range
            else:
                if (distance <= 3):
                    print("You are too close to make this attack.")
                else:
                    print("You are too far to make this attack.")
        
        #COUCH-GUN
        elif (action == "couch-gun"):
        #If the target is within range
            if (distance == 1 or distance == 2):
                actionEconomy -= 1
                #If the attack hits
                if (attackroll+1 >= monsterAC):
                    dealt = random.randint(1, 3)
                    distance += 2
                    print("Your couch-round struck true. You dealt " + str(dealt) + " damage to the " + monster + ", and pushed it back 2 spaces!")
                #If the attack misses
                else:
                    print("Was worth a shot, buckaroo.")
            #If the target is out of range
            else:
                print("You are too far to make this shot.")
        else:
            print("That is not a valid action.")
    else:
        print("Invalid")
    
    #After the action
    return(dealt)
    
def playerAO(power, monster):
        global monsterAC
        dealt = 0
        attackroll = random.randint(1, 20)

        #If the player is a Brute, Slash at the target as an AO
        if (power.lower() == "brute"):
            if (attackroll >= monsterAC):
                dealt = random.randint(1, 12)
                print("Your attack hit as the " + monster + " stepped away, and dealt " + str(dealt) + " damage!")
                #If the attack misses
            else:
                print("You swung valiantly at the " + monster + " as it stepped away, but you missed your target.")
                
        #If the player is a Mage, make a Blaze attack as an AO
        elif (power.lower() == "mage"):
            if (attackroll >= monsterAC):
                dealt = random.randint(1, 10)
                print("Your attack hit as the " + monster + " stepped away, and dealt " + str(dealt) + " blazing damage!")
            #If the attack misses
            else:
                print("Your spell was elegant, but the " + monster + " held its will despite your opportunuty.")
                
        #If the player is a Marksman, make a Hilt-bash attack as an AO
        elif (power.lower() == "marksman"):
            if (attackroll-1 >= monsterAC):
                dealt = random.randint(1, 8)
                print("Your bash struck true. You dealt " + str(dealt) + " damage to the " + monster + " as it stepped away!")
            #If the attack misses
            else:
                print("Was worth a shot, buckaroo, but you missed your attack as the " + monster + " stepped away.")
        
        

        
        
#Monster actions

def monsterAction(monster):
    global monsterImmobile
    global monsterHealth
    global monsterActionEconomy
    global distance
    global playerAC
    global playerImmobile
    global FairyHide
    global power
    
    dealt = 0
    attackroll = random.randint(1, 20)
    monsterActionEconomy -= 1
    monstermove = 0
        
        
#Zombie AI
    if (monster == "Zombie"):
        #If the Zombie is not immobile, reset its speed
        if (monsterImmobile == False):
            monsterSpeed = 2
            
        #If the Zombie is not within melee range, move forward.
        for item in range(distance):            
            if ((distance > 1) and (monsterSpeed != 0) and (monsterImmobile == False)):
                monsterSpeed -= 1
                distance -= 1
                monstermove += 1
            else:
                break
        #If the monster moved forward, alert the player
        if (monstermove > 0):
            print("The Zombie charges forward.")
            monstermove = 0
        
            #If the player is in melee range
        if (distance == 1):
            #Bite or Grapple
            if (playerImmobile == True):
                MeleeAttackChoice = "Bite"
            else:
                MeleeAttackChoice = random.choice(["Bite", "Grapple"])
            #Grapple
            if (MeleeAttackChoice == "Grapple"):
                if (attackroll+1 >= playerAC):
                    playerSpeed = 0
                    playerImmobile = True
                    print("The Zombie grappled you! You can't move unless you break the grapple!")
                else:
                    print("The Zombie attempted to grapple you, but you were too dexterous.")  
            #Bite
            else:
                if (attackroll >= playerAC):
                    dealt = random.randint(1, 10)
                    print("The Zombie bit you! It dealt " + str(dealt) + " damage...")
                else:
                    print("The Zombie attempted to bite you, but you were too dexterous.")
                #If the Zombie is outside of melee range and is immobile, attempt to break the immobility
        elif ((distance > 1) and (monsterSpeed == 0)):
            if (attackroll > playerAC):
                monsterImmobile = False
                monsterSpeed = 2
            #If the Zombie is low on health, and is outside of melee range, regenerate a little
        elif (monsterHealth < 30):
            if (attackroll > 12):
                monsterHealth += 5
                print("The Zombie regenerated a lost limb!")
        else:
            #If the player is outside of melee range and the Zombie is not low on health
            if (attackroll-2 >= playerAC):
                dealt = random.randint(1, 8)
                print("The Zombie tossed a rock at you! It dealt " + str(dealt) + " damage...")
            else:
                print("The Zombie attempted to toss a rock at you, but you managed to see it coming.")
                
    #Goblin AI
    elif (monster == "Goblin"):
        #If the Goblin is not immobile, reset its speed
        if (monsterImmobile == False):
            monsterSpeed = 4
        #Reset the AC gained from taunt.
        monsterAC = 9
        #Randomly determine whether to move forwards, backwards, or not at all
        GoblinMoveFactor = random.choice([1, 2, 3])
        #Move backwards fully
        if (GoblinMoveFactor == 1):
            if ((distance == 1) and (monsterSpeed != 0)):
                playerAO(power, monster)
            distance += monsterSpeed
            monsterSpeed = 0
            print("The Goblin ran backwards, giggling!")
        #Move forward as much as possible
        elif (GoblinMoveFactor == 2):
            for item in range(distance):            
                if ((distance > 1) and (monsterSpeed != 0)):
                    monsterSpeed -= 1
                    distance -= 1
                    monstermove += 1
                else:
                    break
            if (monstermove > 0):
                print("The Goblin dashes forward.")
        #If the player is in melee range, slash
        if (distance == 1):
            if (attackroll-1 >= playerAC):
                dealt = random.randint(1, 8)
                print("The Goblin slashed its claws at you! It dealt " + str(dealt) + " damage...")
            else:
                print("The Goblin attempted to claw at you, but you were too dexterous.")
        #If the Goblin is immobile and not in melee range, attempt to break the immobility
        elif ((distance > 2) and (monsterSpeed == 0)):
            if (attackroll > playerAC):
                monsterImmobile = False
                monsterSpeed = 4
        #If the Goblin is within medium distance, taunt
        elif (4 > distance > 1):
            monsterAC += 4
            print("The Goblin taunts and jeers at you! It throws you off, making the Goblin harder to hit.")
        else:
            if (attackroll+2 >= playerAC):
                dealt = random.randint(1, 10)
                print("The Goblin slung a rock at you! It dealt " + str(dealt) + " damage...")
            else:
                print("The Goblin attempted sling a rock at you, but you were too dexterous.")
        
    #Fairy AI
    else:
        #If the Fairy is not immobile, reset its speed
        if (monsterImmobile == False):
            monsterSpeed = 3
        #Reset the AC gained by hiding.
        monsterAC = 15
        FairyHide -= 1
        #Randomly determine whether to move forwards, backwards, or not at all
        FairyMoveFactor = random.choice([1, 2, 3])
        #Move backwards fully
        if (FairyMoveFactor == 1 and (monsterSpeed != 0)):
            if (distance == 1):
                playerAO()
            distance += monsterSpeed
            monsterSpeed = 0
            print("The Fairy floats backward, fluttering cheerfully!")
        #Move forward as much as possible
        elif (FairyMoveFactor == 2 and distance > 1):
            for item in range(distance):
                if ((distance > 1) and (monsterSpeed != 0) and (monsterImmobile == False)):
                    monsterSpeed -= 1
                    distance -= 1
                    monstermove += 1
                else:
                    break
            if (monstermove > 0):
                print("The Fairy rushes forward.")
                monstermove = 0
        
        #If the player is within medium distance and the Fairy is immobile, attempt to break the immobility
        elif ((distance > 2) and (monsterSpeed == 0)):
            if (attackroll > playerAC):
                monsterImmobile = False
                monsterSpeed = 3
        #If the player is within medium distance, use Freeze
        elif (distance == 2):
            if (attackroll >= playerAC):
                playerSpeed = 0
                playerImmobile = True
                print("The Fairy froze you! You can't move until you escape the chilling barrier!.")
            else:
                print("The Fairy tried to freeze you, but you shook it off.")
        #Otherwise, if the Fairy has less than or equal to 20 health, it isn't immobilized, and didn't hide the last few turns, hide
        elif ((monsterHealth <= 20) and (FairyHide < 1) and (monsterImmobile == False)):
            monsterActionEconomy -= 1
            monsterAC += 2
            FairyHide = 2
            print("The Fairy skurried off to hide! It'll be even harder to hit it now... it could be anywhere!")
        else:
            if (attackroll >= playerAC):
                dealt = random.randint(1, 10)
                print("The Fairy set you ablaze! You took " + str(dealt) + "firey damage!")
            else:
                print("The Fairy tried to set you ablaze, but you're too cool for that.")
    return(dealt)

#Monster Attack of Opportunity (AO)
def monsterAO(monster):
    global playerAC
    global playerHealth
    
    dealt = 0
    attackroll = random.randint(1, 20)

    #If the monster is a Zombie, make a bite attack as an AO
    if (monster == "Zombie"):
        if (attackroll >= playerAC):
            dealt = random.randint(1, 10)
            print("The Zombie bit you as you stepped away! It dealt " + str(dealt) + " damage...")
        else:
            print("The Zombie attempted to bite you as you stepped away, but you were too dexterous.")
            
    #If the monster is a Goblin, make a slash attack as an AO
    elif (monster == "Goblin"):
        if (attackroll-1 >= playerAC):
            dealt = random.randint(1, 8)
            print("The Goblin slashed its claws at you as you stepped away! It dealt " + str(dealt) + " damage...")
        else:
            print("The Goblin attempted to claw at you as you stepped away, but you were too dexterous.")
            
    #If the monster is a Fairy, make a blaze attack as an AO
    elif (monster == "Fairy"):
        if (attackroll >= playerAC):
            dealt = random.randint(1, 10)
            print("The Fairy set you ablaze! You took " + str(dealt) + "firey damage!")
        else:
            print("The Fairy tried to set you ablaze, but you're too cool for that.")
    playerHealth -= dealt
        
#GAME INFO
def info(monster):
    print("You are " + str(distance) + " spaces away from the " + monster)
    print("You currently have " + str(playerHealth) + " health left.")
    print("Currently immobile? " + str(playerImmobile) + "\n")

# Main Game begin                                                                                                                                                    
def RoleBattle():
    global actions
    global playerAC
    global playerHealth
    global playerImmobile
    global playerSpeed
    global actionEconomy
    global monsterAC
    global monsterHealth
    global monsterActionEconomy
    
    

    Gamebegin = raw_input("Welcome to Rolebattle!\nIn this game you have the chance to take on the virtuous power of your favorite fantasy heroes!\nWage war against a barrage of monsters in this turn based fighting game!\nIn this game, you get to choose a power, and you will fight 1-on-1 with a villainous creature! \nWill you defeat your monster?\nGood luck!\n (The following video totally wasn't pirated for the sake of an epic theme song: https://www.youtube.com/watch?v=0VFrvgKWV70) \n Press enter to continue")

#Choose Power
    power = raw_input("Choose your fighting style! \nBrute, Mage, Marksman, or Random \n")
    if ((power.lower() != "brute") and (power.lower() != "mage") and (power.lower() != "marksman")):
        power = random.choice(["Brute", "Mage", "Marksman"])
        
    #BRUTE
    if (power.lower() == "brute"):
        actions = (["Slash --- Range: 1, DMG: High", "Shove --- Range: 1, Special: Push", "Charge --- Range: >1, DMG: Very high", "Grapple --- Range: 1, Special: Immobilize",])
        playerHealth = 100
        playerAC = 18    
        
    #MAGE
    elif (power.lower() == "mage"):
        actions = ["Blaze --- Range: 1-2, DMG: High", "Drown --- Range: >1, Special: Immobilize", "Ground-pound --- Range: 4-7, DMG: Very high", "Gust --- Range: >1, Special: Push"]
        playerHealth = 50
        playerAC = 12
        
    #MARKSMAN
    elif (power.lower() == "marksman"):
        print(actions[0])
        actions = ["Burst --- Range: 2-3, DMG: High", "Hilt-bash --- Range: 1, DMG: Medium", "Snipe --- Range: 4-7, DMG: Very high", "Couch-gun --- Range: 1-2, DMG: Low, Special: Push"]
        playerHealth = 75
        playerAC = 15

        
#Monster-types
    monster = random.choice(["Zombie", "Goblin", "Fairy"])
    
    #ZOMBIE
    if (monster == "Zombie"):
        monsterActions = ["Bite", "Grapple", "Regenerate", "Toss"]
        monsterHealth = 60
        monsterAC = 10
        monsterSpeed = 3
        monsterActionEconomy = 2
    #GOBLIN
    elif (monster == "Goblin"):
        monsterActions = ["Slash", "Slingshot", "Taunt"]
        monsterHealth = 35
        monsterAC = 9
        monsterSpeed = 4
        monsterActionEconomy = 2
    #FAIRY
    else:
        monsterActions = ["Blaze", "Freeze", "Hide"]
        monsterHealth = 25
        monsterAC = 15
        monsterSpeed = 5
        monsterActionEconomy = 2
        
        

    

    
#GAME BEGIN
    #While the player's health and the monster's health are above 0
    while ((playerHealth > 0) and (monsterHealth > 0)):
        #While the player has actions to use
        while (actionEconomy > 0 and playerHealth > 0):
            actionSelection()
            info(monster)
            monsterHealth -= Action(raw_input("Action: \n"), power, monster)
        print("\n")
        while ((monsterActionEconomy > 0) and (monsterHealth > 0)):
            playerHealth -= monsterAction(monster)
        actionEconomy = 2
        monsterActionEconomy = 2
        #If the player is not immobile, reset their speed
        if (playerImmobile == False):
            playerSpeed = 3
    
    if (playerHealth > monsterHealth):
        print("~~~~~\nCongratulations! you defeated the " + monster + ".\n~~~~~")
    else:
        print("~~~~~\nYou have been vanquished by the " + monster + ".\n~~~~~")
RoleBattle()