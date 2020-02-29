import sqlite3
from hash_algo import Hash

def New_User(email):
    db_name = Hash(email) + '.db'
    conn = sqlite3.connect('Database Folder\{0}'.format(db_name))
    c = conn.cursor()

    c.execute('CREATE TABLE My_Booking(Start_Time TEXT, Meet_Who TEXT, Ref_Code TEXT)')
    c.execute('CREATE TABLE Other_Booking(Name TEXT, Email TEXT, Start_Time TEXT, Type TEXT, Ref_Code TEXT)')

    conn.commit()
    conn.close()

