print("Als je naar het strand gaat moet je eerst naar het metro station lopen, je gaat dan met de metro en trein naar een locatie. Vanaf die locatie moet je naar het strand lopen. Als je klaar bent met het starnd moet je terug naar de locatie lopen dan ga je met de trein en metro weer terug en dan weer naar je accomodatie. Dit zijn veel stappen, maar dit kan je berken als je de volgende vragen invult.")
a = input("hoeveel stappen naar het metro station?")
b = input("hoeveel stappen naar het strand?")
c = input("hoeveel stappen naar de locatie?")
d = input("hoeveel stappen vanaf het station naar de accomodatie?")
stappen = int(a) + int(b) + int(c) + int(d)

print("Je hebt "+str(stappen)+" stappen gelopen")