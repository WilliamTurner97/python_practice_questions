weight = input("weight:")
unit = (input("lb or kg:")).lower()
if unit == "lb":
    converted = float(weight)/2.2
    print(f"you are {converted} kg")
else:
    converted = (float(weight) * 2.2)
    print(f"your are {converted} pounds")