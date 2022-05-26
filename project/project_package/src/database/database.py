import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('main_data_base.db')
        self.cursor = self.con.cursor()
        self.create_users_table()
        self.create_plants_table()

    def create_users_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, username varchar(12) NOT NULL, password varchar(50), photo_source varchar(50))")
        self.con.commit()

    def create_user(self, username, password, photo_source):
        self.cursor.execute("INSERT INTO users(username, password, photo_source) VALUES(?, ?, ?)", (username, password, photo_source))
        self.con.commit()

        created_user = self.cursor.execute("SELECT id, username, password, photo_source FROM users WHERE username = ? and password = ? and photo_source=?",
                                           (username,password,photo_source)).fetchall()
        return created_user[-1]

    def create_plants_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS plants(id integer PRIMARY KEY AUTOINCREMENT, email varchar(50), plant_name varchar(12) NOT NULL, species varchar(50), first_water varchar(50), color varchar(50), room varchar (50), notes varchar(50), last_water varchar(50), picture varchar(50))")
        self.con.commit()

    def create_plant(self, email, plant_name, species, first_water, color, room, notes, last_water, picture):
        self.cursor.execute("INSERT INTO plants(email, plant_name, species, first_water, color, room, notes, last_water, picture) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (email, plant_name, species, first_water, color, room, notes, last_water, picture))
        self.con.commit()

        created_plant = self.cursor.execute("SELECT id, email, plant_name, species, first_water, color, room, notes, last_water, picture FROM plants WHERE email = ? AND plant_name = ? and species = ? and first_water=? and color=? and room=? and notes=? and last_water=? and picture=?",
                                           (email, plant_name, species, first_water, color, room, notes, last_water, picture)).fetchall()
        return created_plant[-1]

    def get_plant(self, name_, email):
        plant = self.cursor.execute("SELECT id, plant_name, species, first_water, color, room, notes, last_water, picture FROM plants WHERE plant_name=? AND email=?", (name_, email)).fetchall()
        if len(plant) == 0:
            return None
        return plant[-1]

    def get_plants(self):
        plant = self.cursor.execute("SELECT id, plant_name, species, first_water, color, room, notes, last_water, picture FROM plants").fetchall()
        return plant

    def delete_plants(self, id):
        self.cursor.execute("DELETE FROM plants WHERE id=?", (id,))
        self.con.commit()

    def get_users(self):
        users = self.cursor.execute("SELECT id, username, password FROM users").fetchall()
        return users

    def get_usernames(self):
        usernames = self.cursor.execute("SELECT username FROM users").fetchall()
        return usernames

    def get_users_password(self, username):
        password = self.cursor.execute("SELECT password FROM users where username = ?", (username,)).fetchall()
        if not password:
            return None
        return password[-1]

    def delete_user(self, userid):
        self.cursor.execute("DELETE FROM users WHERE id=?", (userid,))
        self.con.commit()

    def close_db_connection(self):
        self.con.close()

    def water_plant(self, plant_name, newData):
        update = self.cursor.execute("UPDATE plants SET last_water = ? WHERE plant_name = ?", (newData, plant_name))
        self.con.commit()