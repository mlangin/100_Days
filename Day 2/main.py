print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = (float(input("What tip percentage? "))/100)
conv= 1.0 + tip
final = (total * conv)/people
print(f"Each person should pay: $" + "{:.2f}".format(final))


