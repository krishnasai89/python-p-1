# Prompt the user for input
weight = float(input("Enter weight: "))

# Ask whether the weight is in kilograms or pounds
unit = input("Kilogram or Pounds? (Kgs or Lbs): ")

if unit == "Kgs":
    weight *= 2.205  # Convert kilograms to pounds
    unit = "Lbs."
elif unit == "Lbs":
    weight /= 2.205  # Convert pounds to kilograms
    unit = "kgs."
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {weight:.2f} {unit}")
