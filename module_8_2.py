def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        if isinstance(numbers, dict):
            numbers = numbers.values()
        for number in numbers:
            try:
                result += number
            except TypeError as exp:
                print(f'В numbers записан некорректный тип данных - {number}')
                incorrect_data += 1
        return (result, incorrect_data)
    except TypeError:
        return  None

def calculate_average(numbers):
    try:
        if isinstance(numbers, dict):
            numbers = numbers.values()
        result, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data
        try:
            return result / count
        except ZeroDivisionError:
            average = 0
        return average
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип

print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3

print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция

print(f'Результат 4: {calculate_average({"a":1, "b":2, "c":3, "d":4})}') # Всё должно работать