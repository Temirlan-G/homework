import sqlite3


class Product:
    def __init__(self):
        self.connection = sqlite3.connect('HW.sqlite3')
        self.cursor = self.connection.cursor()

    def create_table(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        sql = ("create table product ( "+ str(id) +" number(10) not null, "+ str(name) +" varchar(15) not null, "+ str(price) +" integer);")
        try:
            self.cursor.execute(sql)
            print('table created')
        except sqlite3.OperationalError:
            print('table already exists')

    def insert(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        sql = ("insert into product (id, name, price) values ("+ str(id) +", \'"+ str(name) +"\',"+ str(price) +");")
        self.cursor.execute(sql)
        self.connection.commit()
        print('1 row inserted')

    def update(self, id, **kwargs):
        self.id = id
        self.name = kwargs['name']
        self.price = kwargs['price']
        sql = ("update product set name = \'" + str(kwargs['name']) + "\', price = " + str(kwargs['price']) + " where id = " + str(id))
        self.cursor.execute(sql)
        self.connection.commit()
        print('1 rows updated')

    def delete(self, id):
        self.id = id
        sql = ("delete from product where id ="+str(id))
        self.cursor.execute(sql)
        self.connection.commit()
        print('1 rows deleted')


tbl = Product()

tbl.create_table('id', 'name', 'price')

tbl.insert(1, 'Bread', 20)

tbl.insert(2, 'Milk', 45)

tbl.insert(3, 'Meat', 200)

tbl.insert(4, 'null', 'null')

tbl.update(4, name='Egg', price='10')

tbl.delete(4)
