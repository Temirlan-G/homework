import sqlite3


class Author:
    def __init__(self):
        self.connection = sqlite3.connect('HW7.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        sql = ("create table library (id number(10) primary key unique, name varchar(25), surname varchar(25), country varchar(15));")
        try:
            self.cursor.execute(sql)
            print('table created')
        except sqlite3.OperationalError:
            print('table already exists')

    def insert(self, id, name, surname, country):
        self.id = id
        self.name = name
        self.surname = surname
        self.country = country
        self.cursor.execute("insert into library (id, name, surname, country) values (?, ?, ?, ?);", (id, name, surname, country))
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
        sql = ("delete from library where id ="+str(id))
        self.cursor.execute(sql)
        self.connection.commit()
        print('1 row deleted')


class Post:
    def __init__(self):
        self.connection = sqlite3.connect('HW7.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        sql = ("create table reader (id number(10) primary key unique, title varchar(25), description varchar(25), post_year integer, author_id integer, foreign key (author_id) references library(id));")
        try:
            self.cursor.execute(sql)
            print('table created')
        except sqlite3.OperationalError:
            print('table already exists')

    def insert(self, id, title, description, post_year, author_id):
        self.id = id
        self.title = title
        self.description = description
        self.post_year = post_year
        self.author_id = author_id
        self.cursor.execute("insert into reader (id, title, description, post_year, author_id) values (?, ?, ?, ?, ?);", (id, title, description, post_year, author_id))
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
        sql = ("delete from reader where id ="+str(id))
        self.cursor.execute(sql)
        self.connection.commit()
        print('1 row deleted')

    def link(self, table1, table2, id1, id2):
        self.table1 = table1
        self.table2 = table2
        self.id1 = id1
        self.id2 = id2
        result = self.cursor.execute(f"select x.name, x.surname, y.title, y.post_year, x.country from {table1} x inner join {table2} y on x.{id1} = y.{id2}").fetchall()
        return result


author = Author()
post = Post()

# library.create_table()

# library.insert(1, 'Leo', 'Tolstoy', 'Russia')
# library.insert(2, 'John', 'Tolkien', 'South Africa')
# library.insert(3, 'Alexandre', 'Dumas', 'France')
# library.insert(4, 'Joanne', 'Rowling', 'England')


# reader.create_table()
# reader.insert(1, 'Harry Potter', 'Magic school', 2001, 4)
# reader.insert(2, 'Anna Karenina', 'Novel about love', 1875, 1)
# reader.insert(3, 'The Lord of the Rings', 'Fantasy and adventure', 1954, 2)
# reader.insert(4, 'The Hobbit', 'Fantasy and adventure', 1937, 2)
# reader.insert(5, 'The Count of Monte Cristo', 'Historical and adventure', 1844, 3)
# reader.insert(6, 'War and Peace', 'Historical', 1969, 1)

joined = post.link('library', 'reader', 'id', 'author_id')

for i in joined:
    print(i, '\n')
