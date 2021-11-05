text=input("scrieti un text")

for letter in text:
    if(((letter>='A' and letter<='Z' ) or (letter>='a' and letter <='z')) and letter != 'A' and letter != 'E'and letter != 'O'and letter != 'U'
    and letter != 'I'and letter != 'a'and letter != 'e'and letter != 'o'and letter != 'u'and letter != 'i'):
        print(letter,"\n")
