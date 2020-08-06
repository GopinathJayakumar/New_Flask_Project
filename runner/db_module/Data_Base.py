import sqlite3
from runner.db_module.TestData import Register_DB


class DataBaseFile:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_connection(self):
        con = sqlite3.connect(self.file_name)
        print('Create Connection')
        return con

    def create_table(self, con, table_name):
        con.execute(''' CREATE TABLE IF NOT EXISTS ''' + table_name +
                    '''(F_name TEXT NOT NULL, 
                        L_name TEXT NOT NULL, 
                        Email TEXT NOT NULL,
                        Pwd TEXT NOT NULL) '''
                    )
        print('Create Table')

    def insert_records(self, con, table_name, obj):
        data = ''' INSERT INTO ''' + table_name + '''('F_name','L_name', 'Email', 'Pwd') 
                    VALUES(?, ?, ?, ?)'''
        con.execute(data, (obj.f_name, obj.l_name, obj.email, obj.pwd))
        con.commit()
        print('inserted records')

    def fetch_records(self, con, qr):
        data = con.execute(qr)
        return data

    def close_connect(self, con):
        con.close()
        print('DataBase closed')


if __name__ == "__main__":
    db_obj = DataBaseFile('demo_123.db')
    con = db_obj.get_connection()
    db_obj.create_table(con, 'register')
    obj = Register_DB(f_name ='balaji', l_name ='M', email = 'balaji@gmail.com', pwd ='12345')
    db_obj.insert_records(con, "register", obj)
    db_obj.close_connect(con)
