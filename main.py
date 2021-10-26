choose_conversion = input("Weight (W) or Height (H): ")
weight = "W"
height = "H"

if choose_conversion == weight:
    weight = float(input("Weight: "))
    unit = input("(K)g or (L)bs: ")
    if unit.upper() == "K":
        converted = weight / 0.45
        print("Weight in Lbs: " + str(converted))
    else:
        converted = weight * 0.45
        print("Weight in Kgs: " + str(converted))

elif choose_conversion == height:
    height = float(input("Height: "))
    unit = input("Inch(In) or Centimeters (cm): ")
    if unit == "In":
        converted = height * 2.54
        print("Height in cm: " + str(converted))
    else:
        converted = height / 2.54
        print("Height in In: " + str(converted))

print("Done.")
