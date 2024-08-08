import sqlite3

def query_data():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()

    c.execute('SELECT * FROM purchases')
    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    query_data()
