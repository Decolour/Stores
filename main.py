class Store():
    def __init__(self, name, adress):
        self.items = []
        self.name = name
        self.adress = adress

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def delete_item(self, name):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                break

    def get_price(self, name):
        for item in self.items:
            if item['name'] == name:
                price = item['price']
                print(f' Цена на {name} составляет {item["price"]}')
                return item['price']

        return None

    def update_price(self, name, price):
        for item in self.items:
            if item['name'] == name:
                item['price'] = price
                print(f"Цена на товар {name} обновлена на {price} рублей.")
                break



StoreA = Store("Продмаг", "Ватутина 15")
StoreA.add_item("Хлеб", 50)
StoreA.add_item("Молоко", 100)
StoreA.add_item("Колбаса", 200)
StoreA.add_item("Сыр", 150)

StoreB = Store("Хозмаг", "Ватутина 17")
StoreB.add_item("Вантуз", 50)
StoreB.add_item("Белизна", 100)
StoreB.add_item("Голубизна", 200)
StoreB.add_item("Ёршик", 150)

StoreC = Store("Аптека", "Ватутина 19")
StoreC.add_item("Корвалол", 50)
StoreC.add_item("Септусин", 100)
StoreC.add_item("Амфетамин", 200)
StoreC.add_item("Креатин", 150)

StoreC.update_price("Корвалол", 150)
StoreC.delete_item("Амфетамин")
StoreC.get_price("Септусин")