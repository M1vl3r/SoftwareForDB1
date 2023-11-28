from Models.Climbers import Climbers

def main():
    climber = Climbers()

    while True:
        print("\nВыберите действие:")
        print("1. Вывести все записи")
        print("2. Вывести значения поля 'name'")
        print("3. Добавить запись")
        print("4. Обновить запись")
        print("5. Удалить запись")
        print("0. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '0':
            break

        elif choice == '1':
            records = climber.get()
            print_records(records)

        elif choice == '2':
            names = climber.getOneField('name')
            print_records(names, field_name='name')

        elif choice == '3':
            climber.add_record()

        elif choice == '4':
            record_id = input("Введите ID записи, которую нужно изменить: ")
            climber.update_record(record_id)

        elif choice == '5':
            record_id = input("Введите ID записи, которую нужно удалить: ")
            climber.delete_record(record_id)

        else:
            print("Некорректный ввод. Пожалуйста, выберите существующий вариант.")

def print_records(records, field_name=None):
    for row, record in enumerate(records):
        if field_name:
            print(row, ')', record[field_name])
        else:
            print(row, ' - ', record)

if __name__ == "__main__":
    main()