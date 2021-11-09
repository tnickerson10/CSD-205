# Travis Nickerson
# February 4th 2021
# Dicitonaries
# Goal: To print a dictionary and prompt the user to chose a team (Key) and then print 
# the asscoiated city (Value) into a string of where the team is from.

# Dictionary of football teams
footballTeams = {
    'Chargers': 'Los Angeles',
    'Chiefs': 'Kansas City',
    'Raiders': 'Los Vegas',
    'Broncos': 'Denver',
    'Bears': 'Chicago',
    'Bengals': 'Cincinnati',
    'Packers': 'Green Bay',
    'Patriots': 'New England',
    'Seahawks': 'Seattle',
    'Lions': 'Detroit',
    'Jaguars': 'Jacksonville',
    'Buccaneers': 'Tampa Bay',
                 }

# Loop through the dictionary and print each team (Key)
for team in footballTeams.keys():
    print(team)

# Prompt the user to select a team from the list available
selection = input("Please choose a team from the list above: ")
# Make the user selection titlecased for dictionary in case user input is lowercase
casedSelection = selection.title()

# print user key (team) selection and the associated value (city) in a string
print(f'The team you chose, the {casedSelection} , are from the city of {footballTeams[casedSelection]}!')

