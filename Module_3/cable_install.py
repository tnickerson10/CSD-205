print("Welcome to Nickerson Cables")

companyName = input("What is your company Name?")

print("Welcome " + companyName + "!")

lenOfCable = float(input("How many feet of cable do youu need?"))

price = lenOfCable * 0.87

print(f"The total of your order will be ${price:.2f} for {lenOfCable:.2f} feet of cable")
print(f"Thank you {companyName} for you order!")