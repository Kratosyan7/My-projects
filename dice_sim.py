import random

def dice_simulator():
    num_dice = int(input("Enter the number of dice: "))
    rolls = []

    for _ in range(num_dice):
        roll = random.randint(1, 6)
        rolls.append(roll)

    print("Rolls:", rolls)

dice_simulator()