# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл
# с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
# Все данные в строке разделены запятой с пробелами.

# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# Инкапсулированный атрибут __file_name = 'products.txt'.
# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
# и возвращает единую строку со всеми товарами из файла __file_name.
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        str_products = f"{self.name}, {self.weight}, {self.category}"
        return str_products


class Shop:
    __file_name = "products.txt"

    def get_product(self):
        file = open(self.__file_name, "r+")
        # Режим «r+» открывает файл на чтение и запись.
        # Но в отличие от режимов «w+» и «a+», файл не будет создан, если он не существует,
        # и запись будет производиться с начала файла, без очистки существующих данных.
        products_shop = file.read()
        file.close()
        return products_shop

    def add(self, *products):
        file_get = self.get_product()
        for i in products:
            if self.get_product().find(f'{i.name},') == -1:
                file = open(self.__file_name, "a")
                # Режим «a» также открывает файл на запись, но в отличие от режима «w», он
                # добавляет данные в конец файла,
                # не удаляя существующие. Если файл не существует, он будет создан
                file.write(f"{i}\n")
                file.close()
            else:
                print(f"Продукт {i.name} уже есть в магазине")

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

#s1.add(p1, p2, p3)

#print(s1.get_products())

print(s1.get_product())
