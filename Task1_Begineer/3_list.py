# ---List operations---
print("-" * 80)

justice_league = ["Superman", "Batman", "Wonder Women", "Flash", "Aquaman", "Green Lantern"]

#Task 1: 
print(f"Number of members: {len(justice_league)}")

print("-" * 80)

#Task 2:
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(f"After adding new members: {justice_league}")

print("-" * 80)

# Task 3:
justice_league.remove("Wonder Women")
justice_league.insert(0, "Wonder Women")
print(f"After making wonder women leader: {justice_league}")

print("-" * 80)

#Task 4:
justice_league.remove("Green Lantern")
flash_indx = justice_league.index("Flash")
justice_league.insert(flash_indx + 1, "Green Lantern")
print(f"After separating Aquaman and Flash: {justice_league}")

print("-" * 80)

#Task 5:
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"New team: {justice_league}")

print("-" * 80)

#Task 6:
justice_league.sort()
print(f"Sorted team (new leader is at index 0): {justice_league}")
print(f"New leader: {justice_league[0]}")

print("-" * 80)