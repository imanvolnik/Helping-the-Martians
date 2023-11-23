import os

while True:
    point_A = int(input("Box 1 kilometer (from 1 to 7): "))
    point_B = int(input("Box 2 kilometer (from 1 to 7): "))
    point_C = int(input("Box 3 kilometer (from 1 to 7): "))

    if (1<=point_A<=7) and (1<=point_B<=7) and ((1<=point_C<=7)):
        break
    else:
        print("Enter numbers from 1 to 7")    


total_weight = 713

while True:
    box1_weight = int(input(f"Box 1 weight in kilograms ({total_weight} kilograms left): "))
    box2_weight = int(input(f"Box 2 weight in kilograms ({total_weight - box1_weight} kilograms left): "))
    box3_weight = int(input(f"Box 3 weight in kilograms ({total_weight - box1_weight - box2_weight} kilograms left): "))

    if (box1_weight +box2_weight + box3_weight) == total_weight:
        break 
    else:
        print("The total weight must be 713 kilograms")

