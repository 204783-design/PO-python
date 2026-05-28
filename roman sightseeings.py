import re

def zoekop(a,s):
    result = re.findall(r'\b' + a + '+', s)
    #https://www.geeksforgeeks.org/python/re-findall-in-python/
    print(a)
    print(result)
    print(len(result))
    
antwoord = input("waar zoek je naar? ")

s = "Het Pantheon is een antieke tempel in Rome, die herbouwd is in de 2e eeuw n.Chr. Het is een herbouw van een eerder pantheon op deze plaats, dat in 80 n.Chr. door brand werd verwoest. Pantheon (Grieks: πάς pas = elke / θεός theos = god) betekent '(gewijd aan) alle goden’. Het Pantheon is een van de best bewaard gebleven Romeinse gebouwen ter wereld. Dit dankt het gebouw aan het feit dat het in de 7e eeuw werd omgevormd tot kerk en continu in gebruik is gebleven en onderhouden. Het Pantheon is nog steeds in gebruik als rooms-katholieke kerk en is gewijd aan de Heilige Maria en de martelaren. Het heeft de kerkelijke eretitel basilica minor."
zoekop(antwoord,s)
#https://nl.wikipedia.org/wiki/Pantheon_(Rome)

s = "Het Flavisch Amfitheater (Latijn: Amphitheatrum Flavium), beter bekend als het Colosseum, gebouwd in de 1e eeuw na Chr. te Rome, was het grootste amfitheater in het Romeinse Rijk. Het Colosseum werd gebouwd door de Flavische keizers. De bouw startte op initiatief van keizer Vespasianus en werd gefinancierd uit de krijgsbuit van de plundering van Jeruzalem in 70. De bouw begon in de eerste jaren van de heerschappij van Vespasianus, waarschijnlijk in 70-72. Mogelijk werkten Joodse slaven aan het enorme amfitheater, maar hier is geen historisch bewijs voor. Na de voltooiing in 80 werd het ingewijd door keizer Titus, de oudste zoon van keizer Vespasianus. De spelen bij de opening duurden 100 dagen. De dichter Martialis wijdde er een bundeltje van 33 epigrammen aan. Titus' opvolger en jongere broer Domitianus voegde nog een verdieping toe, benevens een aantal gangen en vertrekken onder de arena, die nu zichtbaar zijn."
zoekop(antwoord,s)
#https://nl.wikipedia.org/wiki/Colosseum

s = "De Trevifontein (Italiaans: Fontana di Trevi) is de grootste en bekendste fontein van Rome. De fontein is circa 26 meter hoog en ongeveer 22 meter breed. Zij is gelegen aan een pleintje, het Piazza di Trevi. De fontein is gebouwd in opdracht van paus Clemens XII. Ze is getekend door Bernini en ruim 50 jaar later gebouwd door de architect Nicola Salvi, in de stijl van de late barok. De bouw duurde van 1732 tot 1762. De fontein is tegen de achtergevel van het Palazzo Poli gebouwd. In het keizerrijk was het de gewoonte om een monument op te richten op plaatsen waar water vanuit nieuwe bronnen Rome binnenkwam."
zoekop(antwoord,s)
#https://nl.wikipedia.org/wiki/Trevifontein

s = "De Sint-Pietersbasiliek (Italiaans: Basilica di San Pietro) is een katholieke kerk en basilica major aan het Sint-Pietersplein in Vaticaanstad. De kerk werd tussen 1506 en 1626 gebouwd in late-renaissance- en barokarchitectuur op de plaats van het vroegere Circus van Nero in Rome, waar volgens de overlevering de apostel en eerste paus, Petrus, gekruisigd en begraven werd. Het is een belangrijk bedevaartsoord voor katholieken en geldt als de eerste van de zeven pelgrimskerken van Rome. De Sint-Pietersbasiliek was de grootste kerk ter wereld tot 1989, toen ze in grootte werd overtroffen door de Basilique Notre-Dame de la Paix in Yamoussoukro, de hoofdstad van Ivoorkust (zie Lijst van grootste kerken)."
zoekop(antwoord,s)
# https://nl.wikipedia.org/wiki/Sint-Pietersbasiliek

s = "De Spaanse Trappen in Rome verbinden de Piazza di Spagna met de Pincio-heuvel, en voeren naar de 16de-eeuwse kerk Trinità dei Monti. Samen met de Trevifontein behoren ze tot de meest bekende stadsgezichten van Rome. Tegelijk worden ze gerekend tot de mooiste voorbeelden van de late barok in deze stad."
zoekop(antwoord,s)
#https://nl.wikipedia.org/wiki/Spaanse_Trappen

s = "De Villa Borghese is een openbaar park in de Italiaanse hoofdstad Rome. Het 80 hectare grote park biedt naast de landschappelijk aangelegde tuinen diverse musea, villa's, paviljoenen en sculpturen. Het landgoed is sinds 1580 (als een kleine wijngaard) in het bezit geweest van de familie Borghese en werd in het begin van de zeventiende eeuw door aankoop van aangrenzende landerijen en wijngaarden uitgebreid tot de huidige omvang. Het park werd in 1605 in opdracht van kardinaal Scipione Borghese, neef van Paus Paulus V en mecenas van de schilder/beeldhouwer Gian Lorenzo Bernini, aangelegd op de heuvel van Pinciano. Het belangrijkste bouwwerk, dat in 1633 werd voltooid, is de Villa Borghese Pinciana. Naast het hoofdgebouw, het Casino Nobile, dat was bestemd voor de kunstcollectie van de familie en sinds 1903 fungeert als het nationale museum Galleria Borghese, bestond het complex nog uit het Casino dell'Uccelliera, de volière, en het Casino dei Giuochi d'Acqua, nu de oranjerie. In de negentiende eeuw werd het park getransformeerd in een Engels landschapspark. Het volledige bezit van de familie Borghese kwam in 1901 in staatsbezit. De tuinen zijn in 1903 aangekocht door de gemeente Rome en sindsdien toegankelijk voor het publiek."
zoekop(antwoord,s)
#https://nl.wikipedia.org/wiki/Villa_Borghese

