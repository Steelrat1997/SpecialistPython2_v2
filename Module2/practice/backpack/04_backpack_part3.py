class Item:
    def __init__(self, name, weight, cost ):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name}  вес: {self.weight}, цена: {self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []  # Предметы, которые хранятся в рюкзаке

    def show_items(self):
        for n, item in enumerate(self.items, 1):
            print(n, item.show())

    def sum_weight(self):
        # summar = 0
        # for item in self.items:
        #     summar += item.weight
        # return summar
        return sum([item.weight for item in self.items])

    def add_item(self, item: Item):
        if self.sum_weight() + item.weight <= self.max_weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжёлый")
    
    def add_items(self, items):
        if items:
            min_weight = 1000000
            for item in items:
                if item.weight < min_weight:
                    min_weight = item.weight
                    min_weight_item = item
            items.remove(min_weight_item)
            self.add_item(min_weight_item)
            self.add_items(items)

        # TODO: реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        #  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы
        

    def sum_cost(self):
        return sum([item.cost for item in self.items])


# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=30)

# # Пытаемся добавлять предметы в рюкзак
# backpack.add_item(item1)
# backpack.add_item(item2)
# backpack.add_item(item3)
# backpack.add_item(item4)
# # TODO: Если предмет не помещается в рюкзак по весу - вывести сообщение "Предмет {name} слишком тяжелый",
# #  и сам предмет не должен быть добавлен в рюкзак.
# #  Если предмет помещает, то добавляем его в рюкзак.


items = [item1, item2, item3, item4]
backpack.add_items(items)

backpack.show_items()
