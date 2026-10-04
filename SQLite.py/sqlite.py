# SQLite implementation for Python:
import sqlite3

conn = sqlite3.connect('landmark.db')

cursor = conn.cursor()

# Create a table for landmarks
cursor.execute(""" CREATE TABLE IF NOT EXISTS landmarks (
    landmark_index INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    categories TEXT NOT NULL,
    time_no_ticket TEXT NOT NULL,
    time_with_ticket TEXT NOT NULL,
    ticket_cost REAL NOT NULL,
    visited BOOLEAN NOT NULL,
    have_ticket BOOLEAN NOT NULL,
    number_of_tickets INTEGER NOT NULL
)""")

#Query all rows from the landmarks table:
cursor.execute("SELECT * FROM landmarks")
rows = cursor.fetchall()

print("--- Current Database Contents ---")

for row in rows:
    print(row)

#Commit changes and close connection:
#conn.commit()
conn.close()
