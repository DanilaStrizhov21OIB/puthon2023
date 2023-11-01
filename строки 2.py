text = input("Введите строку: ")
cleaned_text = ""
for i in range(len(text)):
    if text[i] == " ":
        if i+1 < len(text) and text[i+1] == " ":
            continue
    cleaned_text += text[i]
print("Очищенная строка:", cleaned_text)
