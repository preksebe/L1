nrBlocuri=int(input("Introduceti numarul de blocuri"))
inaltime=0
ultimulStrat=0;
if(nrBlocuri/2. > nrBlocuri/2):
    nrBlocuri=nrBlocuri-nrBlocuri/2+1
    ultimulStrat=nrBlocuri/2+1
else:
    nrBlocuri=nrBlocuri-nrBlocuri/2
    ultimulStrat=nrBlocuri/2
inaltime=1
while(nrBlocuri>0):

    if(nrBlocuri-ultimulStrat-1>=0):

        nrBlocuri=nrBlocuri-ultimulStrat
        inaltime+=1

    else:
        nrBlocuri=0
print(inaltime)