# Lesson 3: OOP Principles
# 2. E-commerce Product Catalog System

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Specifications: {self.specs}")


class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")


# Example usage
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()

my_phone = Electronic("456", "Smartphone", 499.99, "6-inch display, 128GB storage")
my_phone.display_info()

my_shirt = Clothing("789", "Casual Shirt", 39.99, "Large")
my_shirt.display_info()
