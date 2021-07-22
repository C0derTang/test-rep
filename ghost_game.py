# Ghost Game
from random import randint # Sets up the randint function so that we can choose a random number
print('Ghost Game') # Prints the game title
feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = randint(1, 3)
    print('Three doors ahead. . .')
    print('A ghost behind one. . .')
    print('Which door do you open?')
    door = input('1, 2, or 3?\n')
    door_num = int(door)
    if door_num == ghost_door:
        print('GHOST!! AAAAAAAAAHHHHHHHH!!!')
        feeling_brave = False
    else:
        print('No ghost! Phew!')
        print('You enter the next room. . .')
        score = score + 1

print('Run away!')
print('Game over! You scored', score)

