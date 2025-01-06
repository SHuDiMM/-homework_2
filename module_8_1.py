def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as exp:
        return f"{a}{b}"



print(add_everything_up(123.4568, 'строка'))

print(add_everything_up('яблоко', 4215))

print(add_everything_up(123.456, 7))

