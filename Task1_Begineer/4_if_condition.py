# -----------Q1-----------------
print("-" * 30)

height = float(input("Enter Height in meters: "))
weight = float(input("Enter Weight in KGs: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")

print("-" * 30)

# -----------Q2-----------------

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a City name: ")

if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print("City not found!")

print("-" * 30)

# -----------Q3-----------------

city1 = input("Enter the first City; ")
city2 = input("Enter the second City: ")


def get_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in India:
        return "India"
    else:
        None

country1 = get_country(city1)
country2 = get_country(city2)

if country1 == country2 and country1 is not None:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country!")

print("-" * 30)