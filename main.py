import os
import random

total_weight = 713

boxmark1 = random.randint(1, 3) 
boxmark2 = random.randint(3, 5) 
boxmark3 = random.randint(5, 7)

def move_boxes():
    boxmark1 = random.randint(1, 3) 
    boxmark2 = random.randint(3, 5) 
    boxmark3 = random.randint(5, 7)
    return boxmark1, boxmark2, boxmark3

def get_box_weight():
    while True:
        box1_weight = int(input(f"Box 1 weight in kilograms ({total_weight} kilograms left): "))
        box2_weight = int(input(f"Box 2 weight in kilograms ({total_weight - box1_weight} kilograms left): "))
        box3_weight = int(input(f"Box 3 weight in kilograms ({total_weight - box1_weight - box2_weight} kilograms left): "))

        if (box1_weight + box2_weight + box3_weight) == total_weight:
            break 
        else:
            print("The total weight must be 713 kilograms")

    return [box1_weight, box2_weight, box3_weight]

def check_cargo():
    while True:
        print("Enter the kilometer marks to check for cargo:")
        kilometer1 = int(input("Kilometer mark 1: "))
        kilometer2 = int(input("Kilometer mark 2: "))
        kilometer3 = int(input("Kilometer mark 3: "))

        if kilometer1 == boxmark1 and kilometer2 == boxmark2 and kilometer3 == boxmark3:
            print("Congratulations! You found all the cargo.")
            break
        else:
            print("No cargo found at the entered kilometer marks. Boxes have moved.")
            lst_boxmarks = [move_boxes()]


lst_boxmarks = [boxmark1, boxmark2, boxmark3]

lst_boxweight = get_box_weight()            

os.system("cls")

check_cargo()
