import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }},
    2: {
        "Каа": {
            "Вид питомца": "Желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def create():
    last = collections.deque(pets, maxlen=1)[0]

def read():
    pass

def update():
    pass

def delete():
    pass

def get_pet(ID):
    if ID in pets.keys():
        return pets[ID]
    else:
        return False

def get_suffix(age):
    if age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

def pets_list():
    for pet in pets.values():
        for name, info in pet.items():
            print(f"{info['Вид питомца']} по кличке {name}. Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}")


def main():
    while True:
        command = input("Введите команду (create, read, update, delete, list, stop): ")
        if command == "stop":
            break
        elif command == "create":
            create()
        elif command == "read":
            # read()
            ID = int(input("Введите ID питомца: "))
            pet_info = get_pet(ID)
            if pet_info:
                for name, info in pet_info.items():
                    print(f"{info['Вид питомца']} по кличке {name}. Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}")
            else:
                print("Питомец с указанным ID не найден")
        elif command == "update":
            # update()
            pass
        elif command == "delete":
            # delete()
            pass
        elif command == "list":
            pets_list()
        else:
            print("Некорректная команда")

if __name__ == "__main__":
    main()
