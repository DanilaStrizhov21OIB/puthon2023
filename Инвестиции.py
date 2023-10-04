summa=int(input("Минимальная сумма инвестиций - "))
maikl=int(input("Cколько долларов у Майкла - "))
ivan=int(input("Сколько долларов у Ивана - "))
if (maikl>=summa) and (ivan>=summa):
    print("Обоим хватает")
elif (maikl>=summa) and (ivan<=summa):
    print("Майку хватит")
elif (maikl<=summa) and (ivan>=summa):
    print("Ивану хватит")
elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)>=summa):
    print("Если скинутся то хватит")
elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)<=summa):
    print("Оба не могут вложиться")