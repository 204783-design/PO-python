vragen_en_antwoorden = []
stop = False
while stop == False:
    print("\n1. voeg een vraag en antwoord toe")
    print("2. geef een vraag/ antwoord terug")
    print("3. stoppen")
    
    keuze = int(input("kies een optie:"))
    
    if keuze == 1:
        vraag = input("Typ de vraag:")
        antwoord = input("Typ het antwoord:")
        
        combinatie = [vraag, antwoord]
        vragen_en_antwoorden.append(combinatie)
        
        print("Vraag en antwoord toegevoegd!")
        
    elif keuze == 2:
        if len(vragen_en_antwoorden) == 0:
            print("Er zijn nog geen vragen en antwoorden")
        else:
                print("jouw vragen:")
                for i in range(len(vragen_en_antwoorden)):
                    print(i, " -", vragen_en_antwoorden[i][0])
                    
                    index = int(input("Welk nummer wil je terugkrijgen?"))
                    
                    print("Vraag:", vragen_en_antwoorden[index-1][0])
                    print("anwoord:", vragen_en_antwoorden[index-1][1])
                          
    elif keuze == 3:
        print("Tot ziens!")
        stop = True
    else:
        print("ongeldige keuze.")
            