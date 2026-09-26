"""
Problem #61: SQLite CRUD Operations
Date: 2026-09-26

CRUD over SQLite with a users table:
- Insert a new user
- Fetch all users
- Delete a user by ID
- Update a user's last name

"""




import sqlite3


    
sqliteConnection = sqlite3.connect("sql.db")
cur = sqliteConnection.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
sqliteConnection.commit()




def Insert(userid, fname, lname, gender):
    try:
        user = (userid,fname,lname,gender)
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);",user)
        sqliteConnection.commit()
        return True
    
    except sqlite3.Error as e:
        print(f"DB error: {e}")
        return False
    
def Fetch():
    try:
        cur.execute("SELECT * FROM users;")
        result = cur.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"DB error: {e}")
        return False
    

def Delete(userid):
    try:
        cur.execute(f"DELETE FROM users WHERE userid='{userid}';")
        sqliteConnection.commit()
        return True
    except sqlite3.Error as e:
        print(f"DB error: {e}")
        return False


def Update(userid,lname):
    try:
        cur.execute(f"UPDATE users SET lname = '{lname}' where userid = '{userid}'")
        sqliteConnection.commit()
        return True
    except sqlite3.Error as e:
        print(f"DB error: {e}")
        return False