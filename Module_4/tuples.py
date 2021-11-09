footballTeams = ("Chargers", "Chiefs", "Broncos", "Raiders", "Steelers", 
                "Browns", "Ravens", "Bengals", "Bills", "Dolphins", 
                "Patriots", "Jets", "Rams", "49ers","Seahawks", "Cardinals")

print(footballTeams)
for team in footballTeams:
    print(f"The {team} are an American NFL football team!")
    
        

reverseTeams = list(footballTeams)
reverseTeams.reverse()

print(reverseTeams)
for rTeam in reverseTeams:
    print("The " + rTeam + " are an American NFL football team!")
    
        
