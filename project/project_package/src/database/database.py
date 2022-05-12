import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('users.db')
        self.cursor = self.con.cursor()
        self.create_users_table()

    def create_users_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, username varchar(12) NOT NULL, password varchar(50), photo_source varchar(50))")
        self.con.commit()

    def create_user(self, username, password, photo_source):
        self.cursor.execute("INSERT INTO users(username, password, photo_source) VALUES(?, ?, ?)", (username, password, photo_source))
        self.con.commit()

        created_user = self.cursor.execute("SELECT id, username, password, photo_source FROM users WHERE username = ? and password = ? and photo_source=?",
                                           (username,password,photo_source)).fetchall()
        return created_user[-1]

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
