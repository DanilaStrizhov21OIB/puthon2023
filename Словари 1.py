def main():
    pets = {}
    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")
    
    pets[pet_name] = {
        "Вид питомца": pet_type,
        "Возраст питомца": pet_age,
        "Имя владельца": owner_name
    }

    if pet_age == 1:
        age_string = "год"
    elif 2 <= pet_age <= 4:
        age_string = "года"
    else:
        age_string = "лет"

    info = f"Это {pet_type.lower()} по кличке \"{pet_name}\". Возраст питомца: {pet_age} {age_string}. Имя владельца: {owner_name}"
    print(info)


if __name__ == "__main__":
    main()
