print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? Type" + '"left" or "right"')
cross = input()
if cross == "left":
    print("You've come to a lake. There is an island in the middle of the lake. Type" + '"wait"' + "to wait for a boat. Type" + '"swim" to swim across. ')
    wait = input()
    if wait == "wait":
        print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
        yellow = input()
        if yellow == "yellow":
            print('You found the treasure! You Win!')
        elif yellow == "red":
            print('Burned by fire. Game Over.')
        elif yellow == "blue":
            print('Eaten by beasts. Game Over.')
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")