def custom_write(file_name, strings):
    file = open(file_name, "w", encoding="utf-8")
    strings_positions = {}

    for i in strings:
        string_number = strings.index(i) + 1
        position = file.tell()
        file.write(f"{i}\n")
        strings_positions[(string_number, position)] = i

    file.close()

    return strings_positions


info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
