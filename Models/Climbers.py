from Models.Model import Model

class Climbers(Model):
    __nameTable = 'Climbers'
    __name = 'name'
    __address = 'address'

    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    def add_record(self):
        name = input("Введите имя: ")
        address = input("Введите адрес: ")
        fields = f"{self._Climbers__name}, {self._Climbers__address}"
        values = (name, address)
        super().add(self.__nameTable, fields, values)
        print("Новая запись добавлена")

    def delete_record(self, record_id):
        try:
            record_id = int(record_id)
        except ValueError:
            print("Некорректный ввод. ID должен быть числом.")
            return

        records = self.get()
        record_ids = [record['id'] for record in records]

        if record_id not in record_ids:
            print(f"Записи с ID {record_id} не существует.")
            return

        self.delete(self.__nameTable, 'id', record_id)
        print(f"Запись с ID {record_id} удалена.")

    def update_record(self, record_id):
        try:
            record_id = int(record_id)
        except ValueError:
            print("Некорректный ввод. ID должен быть числом.")
            return

        records = self.get()
        record_ids = [record['id'] for record in records]

        if record_id not in record_ids:
            print(f"Записи с ID {record_id} не существует.")
            return

        # Получение новых значений для обновления
        new_name = input("Введите новое имя: ")
        new_address = input("Введите новый адрес: ")

        # Обновление записи
        update_fields = [self.__name, self.__address]
        new_values = [new_name, new_address]

        self.update(self.__nameTable, update_fields, new_values, 'id', record_id)
        print(f"Запись с ID {record_id} обновлена.")