# Travis Nickerson
# February 10th, 2021
# Module 8
# Goal: Miles to Kilometers Calculator with try excpetions for user input

# create a while loop and set to True to test try/exception block
while True:
    try:
        # user input of Miles
        miles = float(input('Please enter the number of miles: '))
        # check if input is negative
        if miles < 0:
            raise ValueError

        # Calcualates Miles -> Kilometers and prints miles and Kilometers    
        def milesToKilometers(miles):
            """ Miles -> Kilometer Calculator """
            kilometers = (miles * 1.609344)
            print(f'Miles: {miles:.2f}')
            print(f'Kilometers: {kilometers:.2f}')
        # calling function with parameter of miles from user input
        milesToKilometers(miles)
        break
    
    # checks if user input is not a valid number
    except ValueError:
        print('Opps! Please try agin with a valid number!')
    # if user input is not a valid number, program will loop back to the try 
    #  block and keep calling function until a valid number is entered
