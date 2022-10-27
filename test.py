liste=["ulrik", "per", "espen",]
navn=input("skriv in et navn: ")
for i in liste:
    if navn in i:
        print (i)
    else:
        print("navnet er ikke i listen")