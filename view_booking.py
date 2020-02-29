import sqlite3
from hash_algo import Hash

def View_Booking(email):
    db_name = Hash(email) + '.db'
    conn = sqlite3.connect('Database Folder\{0}'.format(db_name))
    c = conn.cursor()

    bookings = c.execute('SELECT Start_Time, Meet_Who, Ref_Code FROM My_Booking')
    bookings = bookings.fetchall()

    # --- Sort by time ---

    # --- Missing Code ---

    # --- Sort by Time ---

    return bookings
