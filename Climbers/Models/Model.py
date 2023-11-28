from Climbers.Configuration.Config import connection

class Model:
    def get(self, table):
        with connection().cursor() as cursor:
            select_all_rows = f"SELECT * FROM {table}"
            cursor.execute(select_all_rows)
            return cursor.fetchall()
        connection().close()

    def getOneField(self, table, field):
        with connection().cursor() as cursor:
            select_one_field = f"SELECT {field} FROM {table}"
            cursor.execute(select_one_field)
            return cursor.fetchall()
        connection().close()

    def add(self, table, fields, values):
        with connection().cursor() as cursor:
            placeholders = ', '.join(['%s' for _ in values])
            query = f"INSERT INTO {table} ({fields}) VALUES ({placeholders})"
            cursor.execute(query, values)
        connection().commit()
        connection().close()
        print(f"Новая запись в таблицу {table} добавлена")

    def update(self, table, update_fields, new_values, condition_field, condition_value):
        with connection().cursor() as cursor:
            set_clause = ', '.join([f"{field} = %s" for field in update_fields])
            query = f"UPDATE {table} SET {set_clause} WHERE {condition_field} = %s"
            cursor.execute(query, (*new_values, condition_value))
        connection().commit()
        connection().close()
        print(f"Запись в таблице {table} изменена")

    def delete(self, table, condition_field, condition_value):
        with connection().cursor() as cursor:
            query_delete = f"DELETE FROM {table} WHERE {condition_field} = %s"
            cursor.execute(query_delete, (condition_value,))
        connection().commit()
        connection().close()
        print("Запись удалена")