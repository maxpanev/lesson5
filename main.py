class Store:
    def __init__(self, name, address):
        self.name = name          # Название магазина
        self.address = address    # Адрес магазина
        self.items = {}           # Пустой словарь для товаров и их цен

    def add_item(self, item_name, price):
        """Добавляет товар и его цену в словарь items."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из словаря items."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из магазина.")
        else:
            print(f"Товар '{item_name}' не найден в магазине.")

    def get_item_price(self, item_name):
        """Возвращает цену товара, если он есть в словаре, иначе None."""
        return self.items.get(item_name)

    def display_items(self):
        """Выводит список всех товаров и их цен."""
        for item_name, price in self.items.items():
            print(f"{item_name}: {price} руб за кг")

    def update_price(self, item_name, new_price):
        """Обновляет цену товара, если он есть в словаре, иначе выводит предупреждение."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"\nЦена на {item_name} обновлена до {new_price} руб за кг.")
        else:
            print(f"Товар '{item_name}' не найден в магазине.")

    def delete_item(self, item_name):
        """Удаляет товар по названию и выводит предупреждение, если его нет."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"\nТовар '{item_name}' успешно удален.")
        else:
            print(f"Товар '{item_name}' не найден в магазине.")

# Пример использования

my_store = Store("Овощи и Фрукты", "ул. Пушкина 123")
my_store2 = Store("Мебельный", "ул. Лермонтова 456")
my_store3 = Store("Товары для дома", "ул. Есенина 78")

# Добавляем товары в магазин
my_store.add_item("Яблоки", 75)
my_store.add_item("Бананы", 150)

my_store2.add_item("Диван-кровать", 46300)
my_store2.add_item("Кресло для отдыха", 16490)

my_store3.add_item("Телевизор Samsung", 52900)
my_store3.add_item("Стиральная машина LG F2356945", 33990)

print("Доступные товары:")
my_store.display_items()

# Обновляем цену на Яблоки
my_store.update_price("Яблоки", 80)

# Попытка обновить цену на товар, которого нет в списке
my_store.update_price("Апельсины", 120)

# Получаем цену товара Яблоки
apple_price = my_store.get_item_price("Яблоки")
print(f"\nЦена яблок: {apple_price} руб за кг")

# Попытка получить цену товара, которого нет в магазине
orange_price = my_store.get_item_price("Апельсины")
if orange_price is None:
    print("Апельсинов в магазине нет.")
else:
    print(f"Цена апельсинов: {orange_price} руб за кг")

# Удаляем товар Яблоки
my_store.delete_item("Бананы")

# Попытка удалить товар, которого нет
my_store.delete_item("Апельсины")

print("\nДоступные товары:")
my_store.display_items()