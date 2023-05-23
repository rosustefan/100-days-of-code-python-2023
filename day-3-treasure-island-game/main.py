print('''
*******************************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
     
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
crossroad_choice = input("You're at a crossroad. Do you want to go `left` or `right`?\n").lower()

if crossroad_choice == 'left':
    lake_choice = input("There's an island in the middle of the lake. Type `wait` to wait for a boat or `swim` to swim to the across.\n").lower()
    if lake_choice == 'wait':
        door_choice = input("You arrive at a house on the island. It has three doors: one red, one blue, and one yellow. Type which door colour you'll open:\n").lower()
        if door_choice == 'red':
            print('Congrats! You found a pirate\'s treasure! You win!')
        elif door_choice == 'blue':
            print('The blue skies await you. You just hacked by a madman :-(')
        elif door_choice == 'yellow':
            print('You woke up. It was all just a dream. Or was it? #matrix')
        else:
            print('That door colour is nowhere to be found. Better luck next time!')
    else:
        print('Game Over.')
else:
    print('Game Over.')
