# Travis Nickerson
# February 9th 2021
# Module 7
# Goal: To have a user input an initial investment and an interest rate and calculate how 
# long in years it takes to double the initial investment


# User inputs of Initial Investment and Interest Rate
initialValue = int(input("Plese enter an Initial Investment in Dollars: "))
interestRate = float(input("Please enter an Interest Rate, (0 - 100): "))

# Convert interest rate into a decimal for calcualtions
interstRateConvert = float(interestRate / 100)
# Calculate the target number of double the Initial Value
doubleValue = initialValue * 2
# Set our variable to True. This is our condition check for our while loop
notDoubled = True

# Set years variable so we can incriment it in our while loop to keep track of years
years = 0

# Initialize while loop
while notDoubled:
    # recalculate initialValue for each loop to add the new amount at end of each year
    initialValue = (initialValue * interstRateConvert) + initialValue
    # incriment year to keep track of each year passed
    years += 1
    # print each years money value
    print(f'Year {years}: {initialValue:.2f}')
    # once we hit >= our doubleValue we exit the loop by declaring variable notDoubled = False
    if initialValue >= doubleValue:
        notDoubled = False

# Print out how many years it takes to Double our initial investment 
print(f'It is going to take you {years} years to double your initial investment at a {interestRate}% interest rate!')


