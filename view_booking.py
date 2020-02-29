import sqlite3
from hash_algo import Hash

def View_Booking(email, sort_type):
    db_name = Hash(email) + '.db'
    conn = sqlite3.connect('Database Folder\{0}'.format(db_name))
    c = conn.cursor()

    # --- Sort by time ---
    if sort_type=="time":
        bookings = c.execute('SELECT Start_Time, Meet_Who, Ref_Code FROM My_Booking ORDER BY Start_Time')
        bookings = bookings.fetchall()

    # --- Sort by event ---
    elif sort_type=="event":
        bookings = c.execute('SELECT Start_Time, Meet_Who, Ref_Code FROM My_Booking ORDER BY Ref_Code, Start_Time')
        bookings = bookings.fetchall()

    return bookings

# --- debugging purposes ---

'''if __name__=="__main__":
    print("Sort byt time: " +str( View_Booking("chiang.yuhsuan@dhs.sg", "time")))
    print("Sort byt event, then time: " + str(View_Booking("chiang.yuhsuan@dhs.sg", "event")))
'''

