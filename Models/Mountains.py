from Models.Model import Model


class Mountains(Model):
    __nameTable = 'Mountains'
    __name = 'name'
    __height = 'height'

    def add_record(self):
        name = input("Введите имя горы: ")
        height = int(input("Введите высоту горы: "))
        region_id = int(input("Введите ID региона: "))  # Пока не ясно, как передается region_id
        fields = [self.__name, self.__height, 'region_id']
        values = [name, height, region_id]
        super().add(self.__nameTable, fields, *values)

    def update_record(self, record_id):
        name = input("Введите новое имя горы: ")
        height = int(input("Введите новую высоту горы: "))
        fields = [self.__name, self.__height]
        values = [name, height]
        super().update(self.__nameTable, fields, values, 'id', record_id)

    def delete_record(self, record_id):
        super().delete(self.__nameTable, 'id', record_id)