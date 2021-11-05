from random import randint

randomNumber=randint(0, 20)
guessedNumber=int(input("Ghiceste un numar intre 0 si 20:"))
nrIncercari=1
while guessedNumber != randomNumber :
    if guessedNumber< randomNumber:
        print("Prea mic")
    elif guessedNumber> randomNumber:
        print("Prea mare")
    guessedNumber=int(input("Mai incearca\n"))
    nrIncercari+=1
if(guessedNumber==randomNumber):
    print("felicitari ai avut ",nrIncercari, "incercari iar numarul a fost ",randomNumber)