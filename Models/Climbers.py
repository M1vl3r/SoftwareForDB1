from Models.Model import Model


class Climbers(Model):
    __nameTable = 'Climbers'
    __name = 'name'
    __address = 'address'

    def add_record(self):
        name = input("Введите имя: ")
        address = input("Введите адрес: ")
        fields = [self.__name, self.__address]
        values = [name, address]
        super().add(self.__nameTable, fields, *values)

    def delete_record(self, record_id):
        super().delete(self.__nameTable, 'id', record_id)