# -----------Q1-----------------
print("-" * 30)

def conversion(num, char):
    result = format(num, char)
    print(f"Result: {result}")
    print("This is the Octal representation of the number")    #identification

if __name__ == "__main__":
    conversion(145, "o")

print("-" * 30)

# -----------Q2-----------------

radius = 84
pi = 3.14

area = pi * (radius ** 2)
print(f"Area of the Pond: {area:.2f} square meters")

water_per_sqr_mtr = 1.4
total_water = area * water_per_sqr_mtr
print(f"Total water in the Pond: {int(total_water)} liters")

print("-" * 30)

# -----------Q3-----------------

distance = 490
time = 7 * 60

speed = distance / time
print(f"Speed: {int(speed)} meter per second")

print("-" * 30)