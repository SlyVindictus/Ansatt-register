def Rediger_ansatt():
    print ("Rediger ansatt")
    
def legg_inn():
    print ("legg in ny annsatt valgt")
    fornavn =input("skriv inn fornavn: ")
run=True
while run:
    print ("1. Legg inn ny annsatt")
    print ("2. Rediger ansatt")
    print ("3. Slett ansatt")
    print ("4. List ut alle ansatte")
    print ("5. Avslutt")

    valg=input("velg hva som du vil gjøre: ")
    print(valg)
    if valg== "1":
        legg_inn()
    else:
        print ("Feil")
    
    valg=input("rediger ansatt")
    print(valg)
    if valg== "2":
        rediger_ansatt()
    else:
        print ("Feil")