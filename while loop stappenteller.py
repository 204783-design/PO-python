stappendoel = 25000

behaalde_stappen = -150

# we blijven deze vraag stellen totdat de persoon het minimaal aantal stappen heeft verteld
while behaalde_stappen < 0:
    behaalde_stappen = int(input("wat is het aantal stappen dat je vandaag hebt gezet? "))
    
    if behaalde_stappen < 0:
        print("je kan geen negatief aantal stappen zetten. Voer daarom een positief getal in voor je stappenteller.")

#Dan gaan we kijken of je je stappendoel ook werkelijk hebt behaald
if behaalde_stappen >= stappendoel:
    print("Heel goed gedaan! Je hebt je stappendoel voor de dag behaalt. Wees trots op jezelf!")
else:
    overgebleven_stappen = stappendoel - behaalde_stappen
    print("Je hebt je stappendoel voor de dag helaas nog niet behaalt, maar zet m op!")
    print("Je hoeft nog maar", overgebleven_stappen, "stappen zetten om je doel te behalen. Ga door!.")
    #Als laatst vertellen we hoeveel stappen er nog gezet moeten worden op een positieve manier