import os
import random

total_weight = 713

def create_boxmarks():
    while True:
        boxmark1 = random.randint(1, 7) 
        boxmark2 = random.randint(1, 7) 
        boxmark3 = random.randint(1, 7)
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

lst_boxmarks = create_boxmarks()
print(f"The kilometer box marks are {lst_boxmarks}")

lst_boxweight = get_box_weight()            

os.system("cls")
