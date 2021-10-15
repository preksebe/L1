import sys


print('''
Salut!
Numele meu este: Antal Vladut!
Sunt student la Univ. Tehnică din Iași, Facultatea IEEIA, grupa 6303.
''')

print("20","10","2000",sep='-')

print("antal.vladut",end="@")

f=open("demofile.txt","w")

sys.stdout=f;
print("AM reusit")
