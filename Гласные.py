slovo = input('Введите английское слово с гласными буквами: ')

eg=slovo.count('e')

ag=slovo.count('a')

ig=slovo.count('i')

ug=slovo.count('u')

og=slovo.count('o') 

schetglas=eg+ag+ig+ug+og 

print("всего гласных",schetglas)

print("всего согласных",len(slovo)-schetglas) 

if (eg==0):

    print ("гласной e в слове нет")

else:

    print("e=",eg)

if (ug==0):

    print ("гласной u в слове нет")

else:

    print("u=",ug)

if (og==0):

    print ("гласной o в слове нет")

else:

    print("o=",og)

if (ag==0):

    print ("гласной a в слове нет")

else:

    print("a=",ag)

if (ig==0):

    print ("гласной i в слове нет")

else:

    print("i=",ig)