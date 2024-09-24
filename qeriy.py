import mysql.connector

class Mysql:
    def __init__(self):
        self.connect()
        self.create_databas()
        self.create_table()
    def connect(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Your parol enter"
        )
        self.cursor = self.mydb.cursor()
        
    def create_databas(self):
        self.cursor.execute("create database if not exists Sklad")
        self.cursor.execute("use Sklad")

    def create_table(self):
        self.cursor.execute("""create table if not exists retsep(id int auto_increment primary key,
                            name varchar(500),
                            maxsulot varchar(500),
                            usuli varchar(500))""")

    def insert(self,dates):
        try:
            temp = """insert into retsep (name, maxsulot, usuli) values (%s,%s,%s)"""
            self.cursor.execute(temp,dates)
            self.mydb.commit()
            return True
        except:
            return False
    def drop_data(self,del_taom):
        try:
            query = "delete from retsep where name = %s"
            self.cursor.execute(query,(del_taom,))
            self.mydb.commit()
            return True
        except:
            return False
    def edit_data(self):
        pass

    def search_m(self):
        pass

    def search_r(self,nomi):
        try:
            self.cursor.execute(f'select * from retsep where name = "{nomi}"')
            temp = self.cursor.fetchall()
            return temp
        except:
            return False
    def all_data(self):
        self.cursor.execute("select * from retsep")
        temp = self.cursor.fetchall()
        return temp
    
    def update(self, row_id, new_name, new_maxsulot, new_usuli):
        try:
            temp = """UPDATE retsep 
                  SET name = %s, maxsulot = %s, usuli = %s 
                  WHERE id = %s"""
            self.cursor.execute(temp, (new_name, new_maxsulot, new_usuli, row_id))
            self.mydb.commit()
            return True
        except:
            return False

