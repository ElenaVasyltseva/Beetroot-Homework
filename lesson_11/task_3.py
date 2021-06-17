#  Product Store
#  Write a class Product that has three attributes: type, name, price
#  Then create a class ProductStore, which will have some Products and will operate with all products in the store.
#  All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
#  Tips: Use aggregation/composition concepts while implementing the ProductStore class.
#  You can also implement additional classes to operate on a certain type of product, etc.
#  Also, the ProductStore class must have the following methods:
#  add(product, amount) - adds a specified quantity of a single product
#  with a predefined price premium for your store(30 percent)
#  set_discount(identifier, percent, identifier_type=’name’) - adds a discount
#  for all products specified by input identifiers (type or name).
#  The discount must be specified in percentage
#  sell_product(product_name, amount) - removes a particular amount of products
#  from the store if available, in other case raises an error. It also increments income
#  if the sell_product method succeeds.
#  get_income() - returns amount of many earned by ProductStore instance.
#  get_all_products() - returns information about all available products in the store.
#  get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:
    def __init__(self, style, name, price):
        self.style = self.validate_data_str(style)
        self.name = self.validate_data_str(name)
        self.price = self.validate_data_int(price)
        self.amount = 0

    def validate_data_str(self, value):
        """checking string arguments """
        if len(value) > 2 and value.isalpha():
            return value
        else:
            raise ValueError('Проверьте коректность значений текстовых аргументов')

    def validate_data_int(self, value):
        """checking integer arguments """
        if type(value) == int and value > 0:
            return value
        else:
            raise ValueError('Проверьте коректность значений числовых аргументов')


class Sport(Product):
    def __init__(self, style, name, price):
        super().__init__(style, name, price)


class Food(Product):
    def __init__(self, style, name, price):
        super().__init__(style, name, price)


class Pets(Product):
    def __init__(self, style, name, price):
        super().__init__(style, name, price)


class ProductStore:
    def __init__(self):
        self.income = 0
        self.catalog = []

    def if_catalog_empty(self, value):
        """checking if list of channels is empty"""
        if len(value) == 0:
            raise ValueError('Каталог товаров пуст.')
        else:
            return value

    def validate_data_str(self, value):
        """checking string arguments """
        if len(value) > 2 and value.isalpha():
            return value
        else:
            raise ValueError('Проверьте коректность значений текстовых аргументов')

    def validate_data_int(self, value):
        """checking integer arguments """
        if type(value) == int and value > 0:
            return value
        else:
            raise ValueError('Проверьте коректность значений числовых аргументов')

    def add(self, product, amount):
        """adds product with a predefined price premium for your store(30 percent)"""
        if isinstance(product, Product):
            product.amount = self.validate_data_int(amount)
            product.price = product.price + (product.price/100*30)
            self.catalog.append(product)
        else:
            raise ValueError('Введен неверный формат продукта')

    def set_discount(self, identifier, percent, identifier_type='name'):
        """adds a discount for all products specified by input identifiers (type or name)"""
        identifier = self.validate_data_str(identifier)
        identifier_type = self.validate_data_str(identifier_type)
        percent = self.validate_data_int(percent)
        self.if_catalog_empty(self.catalog)
        if identifier_type == 'name' or 'style':
            for ins in self.catalog:
                if identifier == ins.name:
                    ins.price = ins.price - (ins.price/100*percent)
                    print(f'Цена со скидкой {ins.name}: {ins.price}')
                if identifier == ins.style:
                    ins.price = ins.price - (ins.price / 100 * percent)
                    print(f'Цена со скидкой {ins.name}: {ins.price}')
        else:
            raise ValueError('Введите коректное название и тип товара')

    def sell_product(self, product_name, amount_for_purchase):
        """removes a particular amount of products from the store if available, in other case raises an error."""
        product_name = self.validate_data_str(product_name)
        amount_for_purchase = self.validate_data_int(amount_for_purchase)
        self.if_catalog_empty(self.catalog)
        for ins in self.catalog:
            if product_name == ins.name:
                if amount_for_purchase <= ins.amount:
                    self.income += (ins.amount - amount_for_purchase)*ins.price
                    ins.amount = ins.amount - amount_for_purchase
                    print(f'''Продано {amount_for_purchase} <{product_name}>, 
доход: {amount_for_purchase*ins.price}, 
остаток: {ins.amount}''')
                elif amount_for_purchase > ins.amount:
                    raise ValueError(f'К сожалению такого количества товара нет,  в наличии: {ins.amount}')

    def get_income(self):
        """returns income"""
        print(self.income)

    def get_all_products(self):
        """returns information about all available products in the store."""
        self.if_catalog_empty(self.catalog)
        for ins in self.catalog:
            print(f'Тип товара: {ins. style}. '
                  f'Наименование: {ins.name}. '
                  f'Цена: {ins.price}. '
                  f'Количество: {ins.amount}.')

    def get_product_info(self, product_name):
        """returns a tuple with product name and amount of items in the store"""
        product_name = self.validate_data_str(product_name)
        self.if_catalog_empty(self.catalog)
        for ins in self.catalog:
            if ins.name == product_name:
                print((ins.name, ins.amount))


#  Sport
sport_1 = Sport('sport', 'cap', 200)
sport_2 = Sport('sport', 'ball', 200)
sport_3 = Sport('sport', 'boots', 1000)
#  Food
food_1 = Food('food', 'cookies', 20)
food_2 = Food('food', 'pie', 250)
food_3 = Food('food', 'biscuit', 50)
#  Pets
pets_1 = Pets('pets', 'toy', 5)
pets_2 = Pets('pets', 'food', 20)
pets_3 = Pets('pets', 'toy', 20)
#  create class instance ProductStore
store = ProductStore()
# add products in catalog
store.add(sport_1, 100)
store.add(sport_2, 50)
store.add(sport_3, 70)
store.add(food_1, 20)
store.add(food_2, 30)
store.add(food_3, 15)
store.add(pets_1, 20)
store.add(pets_2, 30)
store.add(pets_3, 15)

#  store.add(pets_3, '15')                          # test products amount validation
#  store.add(3, 15)                                 # test class instance validation


store.set_discount('sport', 10, 'name')         # set discount for sport products
# 
#
store.sell_product('pie', 15)                   # sell product
store.sell_product('ball', 25)
# store.sell_product('ball', 26)                # test
#                                    
store.get_income()                              # print income
#
store.get_all_products()                        # print information about all products

store.get_product_info('ball')
