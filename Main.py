def legg_inn():
    ansatt=[]
    print ("legg in ny annsatt valgt")
    fornavn =input("skriv inn fornavn: ")
    etternavn =input("skriv inn etternavn: ")
    ansatt.append(fornavn)
    ansatt.append(etternavn)
    ansatte.append(ansatt)
ansatte=[]
def list_ut():
    print (ansatte)
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
    elif valg== "4":
        list_ut()

    else:
        print ("Feil")
