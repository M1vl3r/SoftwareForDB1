import tkinter as tk
from tkinter import simpledialog, messagebox

from Climbers.Models.Climbers import Climbers

def print_records(records, field_name=None):
    result = ""
    for row, record in enumerate(records):
        if field_name:
            result += f"{row}) {record[field_name]}\n"
        else:
            result += f"{row} - {record}\n"
    return result

def show_records(records, field_name=None):
    result = print_records(records, field_name)
    tk.messagebox.showinfo("Records", result)

def add_record_dialog(climber):
    name = simpledialog.askstring("Add Record", "Enter name:")
    address = simpledialog.askstring("Add Record", "Enter address:")
    climber.add_record(name, address)

def update_record_dialog(climber):
    record_id = simpledialog.askinteger("Update Record", "Enter ID of the record to update:")
    name = simpledialog.askstring("Update Record", "Enter new name:")
    address = simpledialog.askstring("Update Record", "Enter new address:")
    climber.update_record(record_id, name, address)

def delete_record_dialog(climber):
    record_id = simpledialog.askinteger("Delete Record", "Enter ID of the record to delete:")
    climber.delete_record(record_id)

def main():
    climber = Climbers()

    root = tk.Tk()
    root.title("Climbers App")

    while True:
        choice = simpledialog.askinteger("Choose Action", "Select action:\n1. Show all records\n2. Show 'name' values\n3. Add record\n4. Update record\n5. Delete record\n0. Exit")

        if choice is None or choice == 0:
            break

        elif choice == 1:
            records = climber.get()
            show_records(records)

        elif choice == 2:
            names = climber.getOneField('name')
            show_records(names, field_name='name')

        elif choice == 3:
            add_record_dialog(climber)

        elif choice == 4:
            update_record_dialog(climber)

        elif choice == 5:
            delete_record_dialog(climber)

    root.destroy()

if __name__ == "__main__":
    main()