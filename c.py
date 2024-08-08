import sqlite3

def calculate_average_price():
    # Connect to the SQLite database
    conn = sqlite3.connect('items.db')
    c = conn.cursor()

    # Query to calculate the average price per piece for each item from January and February 2022
    c.execute('''
        SELECT item, AVG(price_per_piece) AS average_price
        FROM purchases
        WHERE month IN ('January 2022', 'February 2022')
        GROUP BY item
    ''')
    
    results = c.fetchall()

    # Print the average price for each item
    print("Average price per piece for each item (January and February 2022):")
    for item, average_price in results:
        print(f"{item}: Rp {average_price:.2f}")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    calculate_average_price()
