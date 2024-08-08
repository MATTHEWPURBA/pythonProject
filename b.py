import sqlite3

def calculate_total_cost():
    # Connect to the SQLite database
    conn = sqlite3.connect('items.db')
    c = conn.cursor()

    # Query to calculate the total cost for January 2022
    c.execute("SELECT SUM(total_cost) FROM purchases WHERE month = 'January 2022'")
    january_total = c.fetchone()[0]

    # Query to calculate the total cost for February 2022
    c.execute("SELECT SUM(total_cost) FROM purchases WHERE month = 'February 2022'")
    february_total = c.fetchone()[0]

    # Calculate the overall total cost
    overall_total = (january_total if january_total else 0) + (february_total if february_total else 0)

    # Print the results with 'Rp' instead of '$'
    print(f"Total cost for January 2022: Rp {january_total if january_total else 0:.2f}")
    print(f"Total cost for February 2022: Rp {february_total if february_total else 0:.2f}")
    print(f"Overall total cost for January and February 2022: Rp {overall_total:.2f}")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    calculate_total_cost()
