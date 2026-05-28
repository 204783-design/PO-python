paklijst = ["zonnebrand", "zwemkleding", "broek", "zonnebril", "wandelschoenen", "oplader", "paspoort", "vliegticket", "sieraden", "kleine reis flesjes", "shampoo", "conditioner"]

x = input("Wat heb je mee?	")

if x in paklijst:
    print("het zit in de paklijst")
    
elif type(x) is not str:
    print("voer geen getal in")
else:
    print("kijk of je er ruimte voor hebt, laat het anders thuis liggen.")
#https://www.geeksforgeeks.org/python/check-if-element-exists-in-list-in-python/
    

           
           