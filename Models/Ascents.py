from Models.Model import Model

class Ascents(Model):
    __nameTable = 'Ascents'
    __id = 'id'
    __finish_time = 'finish_time'
    __mountain_id = 'mountain_id'
    __name = 'name'
    __start_time = 'start_time'

    def add_record(self):
        finish_time = input("Enter finish time: ")
        mountain_id = int(input("Enter mountain ID: "))
        name = input("Enter name: ")
        start_time = input("Enter start time: ")

        fields = [self.__finish_time, self.__mountain_id, self.__name, self.__start_time]
        values = [finish_time, mountain_id, name, start_time]

        super().add(self.__nameTable, fields, *values)

    def update_record(self, record_id):
        finish_time = input("Enter new finish time: ")
        mountain_id = int(input("Enter new mountain ID: "))
        name = input("Enter new name: ")
        start_time = input("Enter new start time: ")

        update_fields = [self.__finish_time, self.__mountain_id, self.__name, self.__start_time]
        new_values = [finish_time, mountain_id, name, start_time]

        super().update(self.__nameTable, update_fields, new_values, self.__id, record_id)

    def delete_record(self, record_id):
        super().delete(self.__nameTable, self.__id, record_id)