class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return "В магазине пусто"

    def add(self, *products):
        existing_products = {}

        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                for line in file:
                    name, weight, category = line.strip().split(", ")
                    existing_products[(name, category)] = float(weight)
        except FileNotFoundError:
            pass

        with open(self.__file_name, "w", encoding="utf-8") as file:
            for product in products:
                key = (product.name, product.category)
                if key in existing_products:
                    existing_products[key] += product.weight
                    print(
                        f"Продукт {product.name} уже был в магазине, его общий вес теперь равен {existing_products[key]}.")
                else:
                    existing_products[key] = product.weight

            for (name, category), weight in existing_products.items():
                file.write(f"{name}, {weight}, {category}\n")


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
