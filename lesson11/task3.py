'''Task 3
Product Store
Write a class Product that has three attributes: (type, name, price)
Then create a class ProductStore, which will have some Products and will operate with all products in the store.
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.
Also, the ProductStore class must have the following methods:
add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified
by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available,
in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.'''
from typing import Dict, Any
class Product():
    '''Клас создания продукта'''
    def __init__(self, type_, name, price):
        '''Инициализируем атрибуты продуката: тип, имя, цена'''

        self.type_ = type_
        self.name = name
        self.price = price

    def __str__(self):
        '''Возвращает описание продукта'''
        return f'Product class object. TYPE: {self.type_}, NAME: {self.name}, PRICE: {self.price}'

class Store:

    def __init__(self):
        self.__income = 0
        self.store = {}

    def add_product(self, product, amount):
        name_ = product.name
        self.store[name_] = {'p': product, 'a': amount}

    def show(self):
        print(self.store)
        return self.store

    def set_discount(self, filtrvalue, type_, discount):
        products = []
        for v in self.store.values():
            attrval = getattr(v['p'], type_)
            if str(filtrvalue) in str(attrval):
                v['p'].price = v['p'].price * discount

    def sell_product(self, name: str, qvi: int):
        if name not in self.store:
            raise ValueError('not in store')

        v = self.store[name]
        if qvi <= 0:
            raise ValueError('не достаточно товара')

        if v['a'] >= qvi:
            v['a'] -= qvi
            self.__income += v['p'].price * qvi

    @property
    def income(self):
        return self.__income


if __name__ == '__main__':
    myStore = Store()
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Sport', 'Adidas', 250)
    myStore.add_product(p, 4)
    myStore.add_product(p2, 15)
    st = myStore.show()
    myStore.set_discount('Adidas', 'name', 0.5)
    myStore.sell_product('Adidas', 2)
    print(myStore.income)


