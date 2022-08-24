import sqlite3

class db:
    def __init__(self, dbName):
        self.dbName = dbName
        self.conn = sqlite3.connect(f'{self.dbName}.db')
        self.cur = self.conn.cursor()

    # создание таблицы
    def createTable(self, tableName, **kwargs):
        columns = ''
        for key, value in kwargs.items():
            columns += f'{key} {value}, '
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {tableName} ({columns[:-2]});
        """)
        self.conn.commit()

    # вставить значения для всех столбцов
    def insert(self, tableName, *args):
        columns = '?, ' * len(args)
        self.cur.execute(f"INSERT INTO {tableName} VALUES({columns[:-2]});", tuple(args))
        self.conn.commit()

    # обновить данные
    def update(self, tableName, column, newValue, condition):
        self.cur.execute(f"UPDATE {tableName} SET {column} = ? where {condition}", (newValue,))
        self.conn.commit()

    # получение данных из таблицы с условием
    def get(self, tableName, column, condition):
        self.cur.execute(f"SELECT {column} FROM {tableName} WHERE {condition}")
        result = self.cur.fetchone()
        if result:
            return result[0]
        return result

    # удаление таблицы
    def delete(self, tableName):
        self.cur.execute(f"DROP TABLE {tableName}")
        self.conn.commit()




