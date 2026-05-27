import re

def zoekop(a,s):
    result = re.findall(r'\b' + a + '+', s)
    print(a)
    print(result)
    print(len(result))
    
antwoord = input("waar zoek je naar? ")

s = "Python is Powerful and is GreatfulG"

zoekop(antwoord,s)

s = "Bla bla bla"
zoekop(antwoord,s)
