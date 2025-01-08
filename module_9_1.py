def apply_all_func(int_list, *functions):
    if not isinstance(int_list, list):
        raise TypeError(f"Функция работает только со списками, такова судьба")

    for i in int_list:
        if not isinstance(i, (int, float)):
            raise TypeError(f"В списке некорректный тип данных: {i} (нужны только числа)")

    for func in functions:
        if not callable(func):
            raise TypeError(f"Передан некорректный объект: {func} (нужна функция)")

    results = {}
    for func in functions:
        try:
            results[func.__name__] = func(int_list)
        except Exception as e:
            results[func.__name__] = f"Ошибка выполнения: {e}"

    return results


print(apply_all_func([6, 20, 15, 9], max, min))

print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
