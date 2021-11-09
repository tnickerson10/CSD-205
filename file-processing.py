# Travis Nickerson
# Feb 27th 2021
# Module 10 Assignment
# Goal: Have user crete a directory and a file name. Save the file
# name in the directory and have user input Name, address, phone number
# and save that info into the .txt file they named. Then print
# info to terminal

# import OS Library
import os

# Define local path
path = os.getcwd()
print(path)
# Prompt user input
userDirectory = input('Please enter the directory you would like to save this file to: ')
userFile = input('Please enter the name of the file you are creating (dont include .txt): ')
name = input('What is your name? ')
address = input('What is your address? ')
phoneNumber = input('What is your phone number? ')

# Create .txt file form user input
newFile = f'{userFile}.txt'

# Create new directory path from user input and local path
newDirectory = f'{path}/{userDirectory}'
os.chdir(path)

# Create Directory to Desktop
os.makedirs(newDirectory)

# Open and write to .txt file that was created by user
with open(f'{newDirectory}/{newFile}', 'w') as f:
    f.write(f'{name}, {address}, {phoneNumber}')
# Open and read .txt file and save contents to a variable to call
with open(f'{newDirectory}/{newFile}') as nf:
    dataInput = nf.read()

# Print users name, address, phone number to terminal
print()
print(dataInput)




