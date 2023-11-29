import os
import random

total_weight = 713

def create_boxmarks():
    while True:
        boxmark1 = random.randint(1, 3) 
        boxmark2 = random.randint(3, 5) 
        boxmark3 = random.randint(5, 7)
        if boxmark1 != boxmark2 and boxmark2 != boxmark3:
            break
    return [boxmark1, boxmark2, boxmark3]
    

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

        if kilometer1 == lst_boxmarks[0] and kilometer2 == lst_boxmarks[1] and kilometer3 == lst_boxmarks[2]:
            print("Congratulations! You found all the cargo.")
            break
        else:
            print("No cargo found at the entered kilometer marks. Boxes have moved.")

lst_boxmarks = create_boxmarks()
print(lst_boxmarks)

lst_boxweight = get_box_weight()            

os.system("cls")

