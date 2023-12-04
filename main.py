from Models.Climbers import Climbers
from Models.Mountains import Mountains
from Models.Regons import Regons
from Models.Ascents import Ascents  # Добавлен новый импорт

def climbers_menu(climbers):
    while True:
        print("Climbers Table:")
        print("1. Show all records")
        print("2. Show 'name' field values")
        print("3. Add record")
        print("4. Update record")
        print("5. Delete record")
        print("0. Back to main menu")

        choice = input("Enter the action number: ")

        if choice == '0':
            break
        elif choice == '1':
            show_all_climbers(climbers)
        elif choice == '2':
            show_names(climbers)
        elif choice == '3':
            climbers.add_record()
        elif choice == '4':
            record_id = int(input("Enter the ID of the record to update: "))
            climbers.update_record(record_id)
        elif choice == '5':
            record_id = int(input("Enter the ID of the record to delete: "))
            climbers.delete_record(record_id)
        else:
            print("Invalid input. Please try again.")

def mountains_menu(mountains):
    while True:
        print("Mountains Table:")
        print("1. Show all mountains")
        print("2. Show 'name' field values")
        print("3. Add mountain")
        print("4. Update mountain")
        print("5. Delete mountain")
        print("0. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            show_all_mountains(mountains)
        elif choice == '2':
            show_names(mountains)
        elif choice == '3':
            mountains.add_record()
        elif choice == '4':
            record_id = int(input("Enter the ID of the record to update: "))
            mountains.update_record(record_id)
        elif choice == '5':
            record_id = int(input("Enter the ID of the record to delete: "))
            mountains.delete_record(record_id)
        else:
            print("Invalid input. Please try again.")

def regions_menu(regions):
    while True:
        print("Regions Table:")
        print("1. Show all records")
        print("2. Add record")
        print("3. Update record")
        print("4. Delete record")
        print("0. Back to main menu")

        choice = input("Enter the action number: ")

        if choice == '0':
            break
        elif choice == '1':
            show_all_regions(regions)
        elif choice == '2':
            regions.add_record()
        elif choice == '3':
            record_id = int(input("Enter the ID of the record to update: "))
            regions.update_record(record_id)
        elif choice == '4':
            record_id = int(input("Enter the ID of the record to delete: "))
            regions.delete_record(record_id)
        else:
            print("Invalid input. Please try again.")

def ascents_menu(ascents):
    while True:
        print("Ascents Table:")
        print("1. Show all records")
        print("2. Add record")
        print("3. Update record")
        print("4. Delete record")
        print("0. Back to main menu")

        choice = input("Enter the action number: ")

        if choice == '0':
            break
        elif choice == '1':
            show_all_ascents(ascents)
        elif choice == '2':
            ascents.add_record()
        elif choice == '3':
            record_id = int(input("Enter the ID of the record to update: "))
            ascents.update_record(record_id)
        elif choice == '4':
            record_id = int(input("Enter the ID of the record to delete: "))
            ascents.delete_record(record_id)
        else:
            print("Invalid input. Please try again.")

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

def show_all_regions(regions):
    records = regions.get('Regons')
    for i, record in enumerate(records):
        print(f"{i} - {record}")

def show_all_ascents(ascents):
    records = ascents.get('Ascents')
    for i, record in enumerate(records):
        print(f"{i} - {record}")

def main():
    climber = Climbers()
    mountain = Mountains()
    region = Regons()
    ascent = Ascents()  # Создаем объект для работы с таблицей Ascents

    while True:
        print("Select table:")
        print("1. Таблица Climbers")
        print("2. Таблица Mountains")
        print("3. Таблица Regions")
        print("4. Таблица Ascents")
        print("0. Exit")

        table_choice = input("Enter your choice: ")

        if table_choice == '0':
            break
        elif table_choice == '1':
            climbers_menu(climber)
        elif table_choice == '2':
            mountains_menu(mountain)
        elif table_choice == '3':
            regions_menu(region)
        elif table_choice == '4':  # Добавлен новый пункт
            ascents_menu(ascent)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()

#