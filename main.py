class Task():
    def __init__(self, description, date):
        # Инициализация атрибутов задачи
        self.description = description  # Описание задачи
        self.date = date  # Срок выполнения задачи
        self.completed = False  # Статус выполнения задачи (по умолчанию не выполнена)

    def mark_as_completed(self): # Отметить задачу как выполненную
        self.completed = True

    def display_task(self): # Вывод информации о задаче
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (до {self.date}) - {status}"

class TaskManager():
    def __init__(self): # Инициализация списка задач
        self.tasks = []

    def add_task(self, task): # Добавление задачи в список
        self.tasks.append(task)

    def completed_tasks(self): # Возвращает список выполненных задач
        return [task for task in self.tasks if task.completed]

    def current_tasks(self): # Возвращает список невыполненных задач
        return [task for task in self.tasks if not task.completed]

    def display_all_tasks(self): # Вывод информации обо всех задачах
        for task in self.tasks:
            print(task.display_task())

# Пример использования
task1 = Task("Сделать утреннюю зарядку", "15.08.24")
task2 = Task("Выпить кофе", "15.08.24")
task3 = Task("Купить продукты", "16.08.24")

manager = TaskManager()
manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)

print("Все задачи:")
manager.display_all_tasks()

task1.mark_as_completed()

print("\nВыполненные задачи:")
for task in manager.completed_tasks():
    print(task.display_task())

print("\nТекущие задачи:")
for task in manager.current_tasks():
    print(task.display_task())

print("\nВсе задачи:")
manager.display_all_tasks()