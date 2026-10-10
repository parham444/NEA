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
    have_tickets BOOLEAN NOT NULL,
    number_of_tickets INTEGER NOT NULL
)""")


#Query all rows from the landmarks table:
cursor.execute("SELECT * FROM landmarks")
rows = cursor.fetchall()

print("--- Current Database Contents ---")

for row in rows:
    print(row)

#Query1 : Get all landmarks name and their ticket prices:
print("---Landmark Ticket Prices---")
cursor.execute("SELECT name, ticket_cost FROM landmarks")
for name, ticket_cost in cursor.fetchall():
    print(f"{name}: £{ticket_cost:.2f}")

#Query2 : Get all landmarks that have category "historic":
print("---Historic Landmarks---")
cursor.execute("SELECT name FROM landmarks WHERE categories LIKE '%historic%'")
for name in cursor.fetchall():
    print(name[0])

#Commit changes and close connection:
#conn.commit()
conn.close()

