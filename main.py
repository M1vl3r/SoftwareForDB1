from Models.Climbers import Climbers
from Models.Mountains import Mountains


def climber_menu(climbers):
    while True:
        print("Таблица Climbers:")
        print("1. Показать все записи")
        print("2. Показать значения поля 'name'")
        print("3. Добавить запись")
        print("4. Обновить запись")
        print("5. Удалить запись")
        print("0. Вернуться в главное меню")

        choice = input("Введите номер действия: ")

        if choice == '0':
            break
        elif choice == '1':
            show_all_climbers(climbers)
        elif choice == '2':
            show_names(climbers)
        elif choice == '3':
            climbers.add_record()
        elif choice == '4':
            record_id = int(input("Введите ID записи, которую нужно изменить: "))
            climbers.update_record(record_id)
        elif choice == '5':
            record_id = int(input("Введите ID записи, которую нужно удалить: "))
            climbers.delete_record(record_id)
        else:
            print("Неверный ввод. Попробуйте еще раз.")


def mountain_menu(mountains):
    while True:
        print("Таблица Mountains:")
        print("1. Показать все горы")
        print("2. Показать значения поля 'name'")
        print("3. Добавить гору")
        print("4. Обновить гору")
        print("5. Удалить гору")
        print("0. Вернуться в главное меню")

        choice = input("Введите ваш выбор: ")

        if choice == '0':
            break
        elif choice == '1':
            show_all_mountains(mountains)
        elif choice == '2':
            show_names(mountains)
        elif choice == '3':
            mountains.add_record()
        elif choice == '4':
            record_id = int(input("Введите ID записи, которую нужно изменить: "))
            mountains.update_record(record_id)
        elif choice == '5':
            record_id = int(input("Введите ID записи, которую нужно удалить: "))
            mountains.delete_record(record_id)
        else:
            print("Неверный ввод. Попробуйте еще раз.")


def show_all_climbers(climbers):
    records = climbers.get('Climbers')
    for i, record in enumerate(records):
        print(f"{i} - {record}")


def show_names(climbers):
    names = climbers.getOneField('Climbers', 'name')
    for i, name in enumerate(names):
        print(f"{i} - {name['name']}")


def show_all_mountains(mountains):
    records = mountains.get('Mountains')
    for i, record in enumerate(records):
        print(f"{i} - {record}")


def show_names(mountains):
    names = mountains.getOneField('Mountains', 'name')
    for i, name in enumerate(names):
        print(f"{i} - {name['name']}")


def main():
    climber = Climbers()
    mountain = Mountains()

    while True:
        print("Выберите таблицу:")
        print("1. Таблица Climbers")
        print("2. Таблица Mountains")
        print("0. Выход")

        table_choice = input("Введите ваш выбор: ")

        if table_choice == '0':
            break
        elif table_choice == '1':
            climber_menu(climber)
        elif table_choice == '2':
            mountain_menu(mountain)
        else:
            print("Неверный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    main()