import sqlite3


class Library:
    def __init__(self):
        self.connection = sqlite3.connect('HW8.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        sql = ("create table library (id number(10) primary key unique, book varchar(25), author varchar(25), country varchar(15));")
        try:
            self.cursor.execute(sql)
            print('table created')
        except sqlite3.OperationalError:
            print('table already exists')

    def insert(self, id, book, author, country):
        self.id = id
        self.book = book
        self.author = author
        self.country = country
        self.cursor.execute("insert into library (id, book, library, country) values (?, ?, ?, ?);", (id, book, author, country))
        self.connection.commit()
        print('1 row inserted')

    def update(self, id, **kwargs):
        keys = []
        values = []
        for i in kwargs:
            keys.append(i)
            values.append(i)
        self.cursor.execute(f"update library set {keys[0]} = {values[0]} where id = {id}")
        self.connection.commit()
        print('1 row updated')

    def delete(self, id):
        self.id = id
        self.cursor.execute("delete from library where id = ?;", (id,))
        self.cursor.execute("delete from library_reader where id_book = ?;", (id,))
        self.connection.commit()
        print('1 row deleted')



class Reader:
    def __init__(self):
        self.connection = sqlite3.connect('HW8.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        sql = ("create table reader (id number(10) primary key unique, name varchar(25), surname varchar(25), registration_date text);")
        try:
            self.cursor.execute(sql)
            print('table created')
        except sqlite3.OperationalError:
            print('table already exists')


    def insert(self, id, name, surname, registration_date):
        self.id = id
        self.name = name
        self.surname = surname
        self.registration_date = registration_date
        self.cursor.execute("insert into reader (id, name, surname, registration_date) values (?, ?, ?, ?);", (id, name, surname, registration_date))
        self.connection.commit()
        print('1 row inserted')

    def update(self, id, **kwargs):
        keys = []
        values = []
        for i in kwargs:
            keys.append(i)
            values.append(i)
        self.cursor.execute(f"update reader set {keys[0]} = {values[0]} where id = {id}")
        self.connection.commit()
        print('1 row updated')

    def delete(self, id):
        self.id = id
        self.cursor.execute("delete from reader where id = ?;", (id,))
        self.cursor.execute("delete from library_reader where id_reader = ?;", (id,))
        self.connection.commit()
        print('1 row deleted')

    def m2m(self, table):
        self.table = table
        sql = (f"create table {str(table)} (id_book number(10), id_reader number(10), foreign key(id_book) references library(id), foreign key(id_reader) references reader(id));")
        try:
            self.cursor.execute(sql)
            print('table created')
        except sqlite3.OperationalError:
            print('table already exists')

    def link(self, id_b, id_r):
        self.id_b = id_b
        self.id_r = id_r
        self.cursor.execute("insert into library_reader (id_book, id_reader) values (?, ?);", (id_b, id_r))
        self.connection.commit()
        print('1 row inserted')


    def m2m_select(self, table1, table2, id1, id2):
        self.table1 = table1
        self.table2 = table2
        self.id1 = id1
        self.id2 = id2
        result = self.cursor.execute(f"select x.name, x.surname, y.library, y.book from {table1} x inner join library_reader z on x.{id1} = z.id_reader inner join {table2} y on z.id_book = y.{id2}").fetchall()
        return result


library = Library()
reader = Reader()

# library.create_table()
# library.insert(1, 'War and Peace', 'Leo Tolstoy', 'Russia')
# library.insert(2, 'Anna Karenina', 'Leo Tolstoy', 'Russia')
# library.insert(3, 'The Hobbit', 'John Tolkien', 'South Africa')
# library.insert(4, 'The Lord of the Rings', 'John Tolkien', 'South Africa')
# library.insert(5, 'The Count of Monte Cristo', 'Alexandre Dumas', 'France')
# library.insert(6, 'Harry Potter', 'Joanne Rowling', 'England')


# reader.create_table()
# reader.insert(1, 'Bill', 'Gates', '2021-04-21')
# reader.insert(2, 'Danny', 'Drinkwater', '2021-03-05')
# reader.insert(3, 'Vitalik', 'Buterin', '2021-02-01')
# reader.insert(4, 'Mark', 'Zuckerberg', '2021-04-01')
# reader.insert(5, 'Pavel', 'Durov', '2021-01-31')

# reader.m2m('library_reader')
# reader.link(1, 4)
# reader.link(2, 1)
# reader.link(3, 5)
# reader.link(4, 5)
# reader.link(5, 2)
# reader.link(6, 3)


joined = reader.m2m_select('reader', 'library', 'id', 'id')

for i in joined:
    print(i, '\n')

