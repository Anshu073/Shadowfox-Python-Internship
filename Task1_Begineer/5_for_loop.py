# ---Q1: Dice Rolling Simulation---
print("-" * 80)

import random

# rolls = []
# for i in range(20):
#     temp = random.randint(1, 6)
#     rolls.append(temp)
rolls = [random.randint(1, 6) for _ in range(20)]

print(f"Dice Rolls: {rolls}")

count_6 = 0
count_1 = 0
two_sixes_in_row = 0

for i in range(len(rolls)):
    if rolls[i] == 6:
        count_6 += 1
    if rolls[i] == 1:
        count_1 += 1
    if i > 0 and rolls[i] == 6 and rolls[i - 1] == 6:
        two_sixes_in_row += 1

print(f"Number of 6s rolled: {count_6}")
print(f"Number of 1s rolled: {count_1}")
print(f"Two 6s in a row (country): {two_sixes_in_row}")

print("-" * 30)

# ---Q2: Jumping Jacks Workout---

total_jacks = 100
completed = 0

for i in range(10):  # max 10 sets of 10
    completed += 10
    print(f"You did {completed} jumping jacks.")

    if completed >= total_jacks:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
    remaining = total_jacks - completed
    if remaining > 0:
        print(f"{remaining} jumping jacks remaining.")

print("-" * 30)