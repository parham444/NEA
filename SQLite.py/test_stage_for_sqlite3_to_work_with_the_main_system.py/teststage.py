import sqlite3

def initialise_landmarks():

    conn = sqlite3.connect('landmark.db')
    cursor = conn.cursor()


    cursor.execute("SELECT COUNT(*) FROM landmarks")
    count = cursor.fetchone()[0]

    print(f"Number of landmarks in the database: {count}")

    if count == 0:
        print("Database is empty, seeding would happen here.")
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
        cursor.execute("""
    INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
    VALUES (0, 'St Albans Cathedral', 'historic, religious', 30, 60, 5.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (1, 'Verulamium Park and Verulamium Lake', 'park, outdoor', 40, 40, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (2, 'The Roman Theatre of Verulamium', 'historic, roman', 0, 30, 3.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (3, 'Verulamium Museum', 'historic, roman, museum', 0, 75, 10.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (4, 'The Roman Wall of St Albans', 'historic, roman, outdoor', 15, 15, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (5, 'The Hypocaust and Roman Mosaic', 'historic, roman', 15, 15, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (6, 'St Albans Clock Tower', 'historic', 10, 25, 1.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (7, 'Abbey Gateway (The Great Gate)', 'historic', 10, 10, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (8, 'Ye Olde Fighting Cocks Inn', 'historic, food_drink', 30, 30, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (9, 'St Albans Museum + Gallery (Old Town Hall)', 'museum, art', 45, 45, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (10, 'Sopwell Nunnery Ruins (Lee Hall)', 'historic', 15, 15, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (11, 'Old Gorhambury House', 'historic', 10, 10, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (12, 'Gorhambury House', 'historic, art', 0, 90, 12.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (13, 'St Michael''s Church', 'historic, religious', 20, 20, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (14, 'St Peter''s Church', 'historic, religious', 20, 20, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (15, 'Fishpool Street Historic Area', 'historic', 20, 20, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (16, 'St Albans Charter Market', 'market, shopping', 30, 30, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (17, 'St Albans South Signal Box', 'historic', 15, 15, 0.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (18, 'Redbournbury Watermill & Bakery', 'historic, food_drink', 20, 45, 4.00, 0, 0, 0)
        """)
        cursor.execute("""
            INSERT INTO landmarks (landmark_index, name, categories, time_no_ticket, time_with_ticket, ticket_cost, visited, have_tickets, number_of_tickets)
            VALUES (19, 'The Vintry Garden', 'park, outdoor', 10, 10, 0.00, 0, 0, 0)
        """)
        conn.commit()
        cursor.execute("SELECT * FROM landmarks")
        print(cursor.fetchall())
    else:
        print("Database already has landmarks, no seeding needed.")

    cursor.execute("SELECT * FROM landmarks")
    rows = cursor.fetchall()

    # creating an empty dictionary to store the landmarks
    landmarks = {}

    for rows in rows:
        landmark_index = int(rows[0])
        name = rows[1]
        categories = rows[2].split(", ")
        time_no_ticket = int(rows[3])
        time_with_ticket = int(rows[4])
        ticket_cost = float(rows[5])
        visited = bool(rows[6])
        have_tickets = bool(rows[7])
        number_of_tickets = int(rows[8])

        # creating a dictionary for each landmark
        landmark_dict = {
            "name": name,
            "categories": categories,
            "time_no_ticket": time_no_ticket,
            "time_with_ticket": time_with_ticket,
            "ticket_cost": ticket_cost,
            "visited": visited,
            "have_tickets": have_tickets,
            "number_of_tickets": number_of_tickets
        }

        # adding the landmark dictionary to the landmarks dictionary
        landmarks[landmark_index] = landmark_dict

    cursor.execute("SELECT * FROM landmarks WHERE landmark_index = 0")
    print(cursor.fetchone())

    return landmarks


landmarks = initialise_landmarks()

landmarks[0]["visited"] = True

def save_landmarks_to_db(landmarks):
    conn = sqlite3.connect("landmark.db")
    cursor = conn.cursor()

    for index in landmarks:
        categories_str = ", ".join(landmarks[index]["categories"])
        cursor.execute("""
            UPDATE landmarks
            SET name = ?, categories = ?, time_no_ticket = ?, time_with_ticket =?, ticket_cost = ?, visited = ?, have_tickets = ?, number_of_tickets = ?
            WHERE landmark_index = ?
            """, (landmarks[index]["name"], categories_str, landmarks[index]["time_no_ticket"], landmarks[index]["time_with_ticket"], landmarks[index]["ticket_cost"], landmarks[index]["visited"], landmarks[index]["have_tickets"], landmarks[index]["number_of_tickets"], index))

    conn.commit()
    conn.close()

save_landmarks_to_db(landmarks)


