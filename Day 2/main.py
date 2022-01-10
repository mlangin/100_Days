print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = ((float(input("What tip percentage? "))/100)+1)
final = (total * tip)/people
print(f"Each person should pay: $" + "{:.2f}".format(final))


