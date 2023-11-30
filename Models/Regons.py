from Models.Model import Model  # Add this line to import the Model class

class Regons(Model):
    __nameTable = 'Regons'
    __id = 'id'
    __country = 'country'
    __region = 'regions'

    def add_record(self):
        country = input("Введите страну: ")
        region = input("Введите регион: ")
        fields = [self.__country, self.__region]
        values = [country, region]
        super().add(self.__nameTable, fields, *values)

    def update_record(self, record_id):
        country = input("Введите новую страну: ")
        region = input("Введите новый регион: ")
        fields = [self.__country, self.__region]
        values = [country, region]
        super().update(self.__nameTable, fields, values, self.__id, record_id)

    def delete_record(self, record_id):
        super().delete(self.__nameTable, self.__id, record_id)