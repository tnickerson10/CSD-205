# Travis Nickerson
# January 27th 2021
# Module 5 Assignment 
# Goal: Obtain company information, required cable needed and the cost for 
#       the cable including bulk discounts.


# Welcome message and User Input of Company name
print("Welcome to Nickerson Cables\n")
companyName = input("What is your company Name?")
print("Welcome " + companyName + "!\n")

# Prompt of cable required by user
lenOfCable = float(input("How many feet of cable do youu need?"))
print()

# Standard and Bulk pricing 

# cable <= 100 feet
priceStandard = lenOfCable * 0.87
#cable between 100 and 249 feet
price100Feet = lenOfCable * 0.80
#cable between 250 and 499 feet
price250Feet = lenOfCable * 0.70
#cable greater >= 500 feet
price500Feet = lenOfCable * 0.50

# Pricing calculations according to length of cable and discounts/ savings
if lenOfCable <= 100:
    print(f"The total of your order will be ${priceStandard:.2f} for {lenOfCable:.2f} feet of cable.\n")
elif lenOfCable <= 250:
    print(f"The total of your order will be ${price100Feet:.2f} for {lenOfCable:.2f} feet of cable.\n")
    print("Your Discount: $0.07/ft")
    print(f"Your Savings: ${priceStandard - price100Feet:.2f}\n")
elif lenOfCable <= 500:
    print(f"The total of your order will be ${price250Feet:.2f} for {lenOfCable:.2f} feet of cable.\n")
    print("Your Discount: $0.17/ft")
    print(f"Your Savings: ${priceStandard - price250Feet:.2f}\n")
else:
    print(f"The total of your order will be ${price500Feet:.2f} for {lenOfCable:.2f} feet of cable.\n")
    print("Your Discount: $0.37/ft")
    print(f"Your Savings: ${priceStandard - price500Feet:.2f}\n")

# Thank you reciept
print(f"Thank you {companyName} for your order!")