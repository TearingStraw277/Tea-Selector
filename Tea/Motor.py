import sqlite3

def database(name):
    conn = sqlite3.connect("Tea.db")
    cur = conn.cursor()
    cur.execute(f"Select * FROM Tea Where Name = \"{name}\"")

    rows = cur.fetchall()
    for row in rows:
        return row

