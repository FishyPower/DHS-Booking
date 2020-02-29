import sqlite3

conn = sqlite3.connect("big_thing.db")
c = conn.cursor()

#variable 'email' as gmail

def Check_Existance(email):
    c.execute("SELECT * FROM big_thing WHERE Gmail_Account = '" + email + "'")
    bookings = c.fetchall()
    if bookings == None:
        return "New User"
    else:
        return bookings

print(Check_Existance("chiang.yuhsuan@dhs.sg"))
