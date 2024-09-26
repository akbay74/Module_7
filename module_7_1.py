import os.path

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        prod = f'{self.name}, {self.weight}, {self.category}'
        return prod


class Shop:

    __file_name = 'products.txt'

    def __init__(self):
        if not(os.path.isfile(self.__file_name)):
            file = open(self.__file_name, 'w')
            file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        content = file.read()
        for i in products:
            if i.name in content:
                print(f'Продукт {i} уже есть в магазине')
            else:
                file.write(f'{i}\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
