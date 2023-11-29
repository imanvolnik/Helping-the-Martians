import random
import os

total_weight = 713

def move_boxes():
    return random.sample(range(1, 8), 3)

def get_box_weights():
    weights = []
    remaining_weight = total_weight
    for i in range(2):
        weight = int(input(f"Enter weight of box {i+1} (remaining weight {remaining_weight}): "))
        weights.append(weight)
        remaining_weight -= weight
    weights.append(remaining_weight)
    return weights

def check_cargo(box_locations, box_weights):
    while True:
        guessed_locations = list(map(int, input("Enter guessed locations for all boxes, separated by spaces: ").split()))
        if sorted(guessed_locations) == sorted(box_locations) and sum(box_weights) == total_weight:
            os.system('cls')
            print("Congratulations! You found all the cargo!!!")
            break
        else:
            print("No cargo found at the guessed locations. The boxes have moved.")
            box_locations = move_boxes()    

box_locations = move_boxes()

box_weights = get_box_weights()

check_cargo(box_locations, box_weights)
