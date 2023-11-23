import os

total_weight = 713

def get_kilo_marks():
    while True:
        point_A = int(input("Box 1 kilometer (from 1 to 7): "))
        point_B = int(input("Box 2 kilometer (from 1 to 7): "))
        point_C = int(input("Box 3 kilometer (from 1 to 7): "))

        if 1 <= point_A <= 7 and 1 <= point_B <= 7 and 1 <= point_C <= 7:
            break
        else:
            print("Enter numbers from 1 to 7")

    return point_A, point_B, point_C

def get_box_weight():
    while True:
        box1_weight = int(input(f"Box 1 weight in kilograms ({total_weight} kilograms left): "))
        box2_weight = int(input(f"Box 2 weight in kilograms ({total_weight - box1_weight} kilograms left): "))
        box3_weight = int(input(f"Box 3 weight in kilograms ({total_weight - box1_weight - box2_weight} kilograms left): "))

        if (box1_weight + box2_weight + box3_weight) == total_weight:
            break 
        else:
            print("The total weight must be 713 kilograms")

    return box1_weight, box2_weight, box3_weight

point_A, point_B, point_C = get_kilo_marks()
box1_weight, box2_weight, box3_weight = get_box_weight()            

os.system("cls")

while True:
    check_A = int(input("Kilometer mark Box 1: "))
    check_B = int(input("Kilometer mark Box 2: "))
    check_C = int(input("Kilometer mark Box 3: "))

    if check_A == point_A and check_B == point_B and check_C == point_C:
        print("All kilometer marks are correct")
        break
    else:
        point_A, point_B, point_C = get_kilo_marks()

