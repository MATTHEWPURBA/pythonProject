import sqlite3

def initialize_db():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS purchases (
            month TEXT,
            item TEXT,
            price_per_piece REAL,
            quantity INTEGER,
            total_cost REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_purchase(month, item, price_per_piece, quantity):
    total_cost = price_per_piece * quantity
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO purchases (month, item, price_per_piece, quantity, total_cost)
        VALUES (?, ?, ?, ?, ?)
    ''', (month, item, price_per_piece, quantity, total_cost))
    conn.commit()
    conn.close()

def main():
    initialize_db()

    # January 2022 purchases
    purchases_january = [
        ("Item A", 100, 3),
        ("Item B", 150, 3),
        ("Item C", 200, 3),
        ("Item D", 250, 3),
    ]
    for item, price_per_piece, quantity in purchases_january:
        add_purchase("January 2022", item, price_per_piece, quantity)

    # February 2022 purchases
    purchases_february = [
        ("Item A", 200, 4),
        ("Item B", 300, 4),
        ("Item C", 400, 4),
        ("Item D", 500, 4),
    ]
    for item, price_per_piece, quantity in purchases_february:
        add_purchase("February 2022", item, price_per_piece, quantity)

    print("Data has been successfully added.")

if __name__ == "__main__":
    main()
