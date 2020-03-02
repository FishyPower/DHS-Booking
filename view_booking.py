import sqlite3
from hash_algo import Hash

def View_Booking(email, sort_type):
    db_name = Hash(email) + '.db'
    conn = sqlite3.connect('Database Folder\{0}'.format(db_name))
    c = conn.cursor()

    # --- Sort by time ---
    if sort_type=="time":
        bookings = c.execute('SELECT Start_Time, End_Time, Meet_Who, Ref_Code FROM My_Booking ORDER BY Start_Time')
        bookings = bookings.fetchall()
        for i in range(len(bookings)-1):
            if bookings[i][-1] == bookings[i+1][-1] and bookings[i][1] == bookings[i+1][0]:
                bookings[i+1][0] == bookings[i][0]
                bookings.pop(i)
        return bookings

    # --- Sort by event ---
    elif sort_type=="event":
        bookings = c.execute('SELECT Start_Time, End_Time, Meet_Who, Ref_Code FROM My_Booking ORDER BY Ref_Code, Start_Time')
        bookings = bookings.fetchall()
        events = [] # --- "3D" array ---
        prev_refcode = ""
        for booking in bookings:
            if(len(events)==0 or booking[2]!=prev_refcode): # --- start adding a new event ---
                events.append([booking])
            else:  # --- continuing adding more bookings of the same event --
                events[-1].append(booking)
            prev_refcode = events[-1][-1][-1]
        for j in range(len(events)):
            for i in range(len(events[j])-1):
            if events[j][i][-1] == events[j][i+1][-1] and events[j][i][1] == events[j][i+1][0]:
                events[j][i+1][0] == events[j][i][0]
                events[j].pop(i)
        return events
        

# --- debugging purposes ---
'''if __name__=="__main__":
    print("Sort byt time: " +str( View_Booking("chiang.yuhsuan@dhs.sg", "time")))
    print("Sort byt event, then time: " + str(View_Booking("chiang.yuhsuan@dhs.sg", "event")))
'''
