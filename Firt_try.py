# SQLite implementation for Python:
import sqlite3
import pygame

def initialise_landmarks():

    conn = sqlite3.connect('landmark.db')
    cursor = conn.cursor()


    cursor.execute("SELECT COUNT(*) FROM landmarks")
    count = cursor.fetchone()[0]


    if count == 0:
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

    conn.close()

    return landmarks

# Time values are in MINUTES, cost values are in POUNDS (£)
landmarks = initialise_landmarks()


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



#Settings
categories = ["historic", "religious", "park", "outdoor", "roman", "museum", "art", "food_drink", "market", "shopping"]

user_preferred_categories = {}


# time limit
def data_type_validation(parameter, location):
    while not parameter.isdigit():
        print(f"Invalid. {parameter} is not a a whole number or its not even a positive number")
        print("try again")
        if location == "hours":
            parameter = input("Enter the number of hours you have (0-23): ")
        elif location == "minutes":
            parameter = input("Enter the number of minutes you have (0-59): ")
        elif location == "landmark":
            parameter = input("Enter a landmark number (0-19): ")
        elif location == "pounds":
            parameter = input("Enter your budget limit in pounds (£): ")
        elif location == "pence":
            parameter = input("Enter your budget limit in pence (0-99): ")
        elif location in categories:
            parameter = input(f"Please rank {location} from 0 to 5: ")
        elif location == "landmark_selection":
            parameter = input("Enter a landmark number (0-19): ")
        elif location == "tickets":
            parameter = input("How many tickets do you want to purchase? you cannot purchase more than 6 tickets for a landmark: ")
        elif location == "manual_landmark":
            parameter = input("Try again: ")
    return parameter

print("Welcome to the St Albans Landmarks Explorer!")
def get_user_time_limit():
    time_limit =0
    print("Here you can submit your time limit, you can do this by entering the time you have into two boxes of hours and minutes.")
    print("For example, if you have 2 hours and 30 minutes, you yould enter 2 into ther hours box and 30 into the minutes box.")
    print("Also you must enter your time limit in whole numbers only.")
    print("You are not allowed to enter negative numbers or numbers greater than 23 for the hours box and 59 for the minutes box.")
    hours_box_time_limit = input("Enter the number of hours you have: ")
    minutes_box_time_limit = input("Enter the number of minutes you have: ")

    hours_box_time_limit = int(data_type_validation(hours_box_time_limit, "hours"))
    while  hours_box_time_limit >23:
        print(f"invalid. {hours_box_time_limit} is not in the range of 0-23 for the hours box")
        print("Try again")
        hours_box_time_limit = input("Enter the number of hours you have: ")
        hours_box_time_limit = int(data_type_validation(hours_box_time_limit, "hours"))

    minutes_box_time_limit = int(data_type_validation(minutes_box_time_limit, "minutes"))
    while  minutes_box_time_limit >59:
        print(f"invalid. {minutes_box_time_limit} is not in the range of 0-59 for the minutes box")
        print("Try again")
        minutes_box_time_limit = input("Enter the number of minutes you have: ")
        minutes_box_time_limit = int(data_type_validation(minutes_box_time_limit, "minutes"))

    while hours_box_time_limit == 0 and minutes_box_time_limit == 0:
        print("Invalid. You cannot enter 0 hours and 0 minutes as your time limit.")
        print("Try again")
        hours_box_time_limit = input("Enter the number of hours you have: ")
        minutes_box_time_limit = input("Enter the number of minutes you have: ")

        hours_box_time_limit = int(data_type_validation(hours_box_time_limit, "hours"))
        while  hours_box_time_limit >23:
            print(f"invalid. {hours_box_time_limit} is not in the range of 0-23 for the hours box")
            print("Try again")
            hours_box_time_limit = input("Enter the number of hours you have: ")
            hours_box_time_limit = int(data_type_validation(hours_box_time_limit, "hours"))

        minutes_box_time_limit = int(data_type_validation(minutes_box_time_limit, "minutes"))
        while  minutes_box_time_limit >59:
            print(f"invalid. {minutes_box_time_limit} is not in the range of 0-59 for the minutes box")
            print("Try again")
            minutes_box_time_limit = input("Enter the number of minutes you have: ")
            minutes_box_time_limit = int(data_type_validation(minutes_box_time_limit, "minutes"))

    time_limit += (hours_box_time_limit * 60) + minutes_box_time_limit

    print(f"Your time limit is {hours_box_time_limit} hours and {minutes_box_time_limit} minutes.")

    return time_limit

time_limit = get_user_time_limit()
initial_time_limit = time_limit

con_time_limit = input("Do you want to continue with the time limit you have entered? (yes/no): ")

while con_time_limit.lower() not in ["yes", "no"]:
    print(f"Invalid. {con_time_limit} is not a valid response. Please enter 'yes' or 'no'.")
    con_time_limit = input("Do you want to continue with the time limit you have entered? (yes/no): ")

while con_time_limit.lower() == "no":
    time_limit = get_user_time_limit()
    initial_time_limit = time_limit
    con_time_limit = input("Do you want to continue with the time limit you have entered? (yes/no): ")
    while con_time_limit.lower() not in ["yes", "no"]:
        print(f"Invalid. {con_time_limit} is not a valid response. Please enter 'yes' or 'no'.")
        con_time_limit = input("Do you want to continue with the time limit you have entered? (yes/no): ")

# budget limit:
def get_user_budget_limit():
    budget_limit = 0
    print("Here you can submit your budget limit, you can do this by entering the amount of budget that you have into two boxes of pounds and pence.")
    print("For example, if you have £20.50, you would enter 20 into the pounds box and 50 into the pence box.")
    print("Also you must enter your budget limit in whole numbers only.")
    pounds_box_budget_limit = input("Enter your budget limit in pounds (£): ")
    pence_box_budget_limit = input("Enter your budget limit in pence (0-99): ")

    # Validate the input for pounds and pence
    pounds_box_budget_limit = int(data_type_validation(pounds_box_budget_limit, "pounds"))
    pence_box_budget_limit = int(data_type_validation(pence_box_budget_limit, "pence"))


    while  pence_box_budget_limit > 99:
        print(f"Invalid. {pence_box_budget_limit} is not a valid amount for pence. It must be between 0 and 99.")
        pence_box_budget_limit = input("Enter your budget limit in pence (0-99): ")
        pence_box_budget_limit = int(data_type_validation(pence_box_budget_limit, "pence"))

    # Convert the budget to a single value in pounds
    budget_limit = pounds_box_budget_limit + (pence_box_budget_limit / 100)

    print(f"Your budget limit is £{budget_limit:.2f}")

    return budget_limit

budget_limit = get_user_budget_limit()
initial_budget_limit = budget_limit

con_budget_limit = input("Do you want to continue with the budget limit you have entered? (yes/no): ")

while con_budget_limit.lower() not in ["yes", "no"]:
    print(f"Invalid. {con_budget_limit} is not a valid response. Please enter 'yes' or 'no'.")
    con_budget_limit = input("Do you want to continue with the budget limit you have entered? (yes/no): ")

while con_budget_limit.lower() == "no":
    budget_limit = get_user_budget_limit()
    initial_budget_limit = budget_limit
    con_budget_limit = input("Do you want to continue with the budget limit you have entered? (yes/no): ")
    while con_budget_limit.lower() not in ["yes", "no"]:
        print(f"Invalid. {con_budget_limit} is not a valid response. Please enter 'yes' or 'no'.")
        con_budget_limit = input("Do you want to continue with the budget limit you have entered? (yes/no): ")


# User preferred categories
print("Now you can rank your preferred categories from 0 to 5.")
print("0 = Not interested, 1 = Slightly interested, 2 = Moderately interested, 3 = Interested, 4 = Very interested, 5 = Extremely interested")
print("You will be asked to rank each category one by one. if you dont want to rank a category, you can enter 0 for that category.")

for category in categories:
    rank = input(f"Please rank {category} from 0 to 5: ")
    rank = int(data_type_validation(rank, category))
    while rank > 5:
        print(f"Invalid. {rank} is not in the range of 0-5 for the category {category}.")
        print("Try again")
        rank = input(f"Please rank {category} from 0 to 5: ")
        rank = int(data_type_validation(rank, category))
    print(f"You ranked {category} as {rank}.")
    user_preferred_categories[category] = rank

for category in user_preferred_categories:
    print(f"{category}: {user_preferred_categories[category]}")

con_user_preferred_categories = input("Do you want to change the category rankings you have entered? (yes/no): ")

while con_user_preferred_categories.lower() not in ["yes", "no"]:
    print(f"Invalid. {con_user_preferred_categories} is not a valid response. Please enter 'yes' or 'no'.")
    con_user_preferred_categories = input("Do you want to change the category rankings you have entered? (yes/no): ")

while con_user_preferred_categories.lower() == "yes":                                                                                                                  
    print("Which category would you like to change the ranking for?")
    category_to_change = input(f"Please enter the category name from the following list: {', '.join(user_preferred_categories.keys())}: ")

    while category_to_change.lower() not in user_preferred_categories:
        print(f"Invalid. {category_to_change} is not a valid category name.")
        category_to_change = input(f"Please enter the category name from the following list: {', '.join(user_preferred_categories.keys())}: ")

    new_rank = input(f"Please enter the new rank for {category_to_change.lower()} from 0 to 5: ")

    new_rank = int(data_type_validation(new_rank, category_to_change.lower()))
    while new_rank > 5:
        print(f"Invalid. {new_rank} is not in the range of 0-5 for the category {category_to_change.lower()}.")
        print("Try again")
        new_rank = input(f"Please enter the new rank for {category_to_change.lower()} from 0 to 5: ")
        new_rank = int(data_type_validation(new_rank, category_to_change.lower()))

    print(f"You changed the rank for {category_to_change.lower()} to {new_rank}.")
    user_preferred_categories[category_to_change.lower()] = new_rank

    for i in user_preferred_categories:
        print(f"{i}: {user_preferred_categories[i]}")
    con_user_preferred_categories = input("Do you want to change the category rankings you have entered? (yes/no): ")

print("Thank you for providing your preferences and limitations. We will now use this information to suggest landmarks that match your interests, time limit, and budget limit.")







distances = [
    [0.0, 0.5, 0.9, 0.8, 0.6, 0.7, 0.1, 0.1, 0.2, 0.2, 0.9, 2.6, 2.8, 0.8, 0.6, 0.4, 0.2, 0.7, 4.1, 0.1], 
    [0.5, 0.0, 0.4, 0.3, 0.2, 0.1, 0.5, 0.4, 0.3, 0.6, 1.3, 2.1, 2.3, 0.3, 1.0, 0.4, 0.6, 1.1, 3.8, 0.5], 
    [0.9, 0.4, 0.0, 0.2, 0.5, 0.4, 0.8, 0.8, 0.7, 0.8, 1.6, 1.8, 2.0, 0.1, 1.2, 0.3, 0.8, 1.5, 3.4, 0.8], 
    [0.8, 0.3, 0.2, 0.0, 0.3, 0.2, 0.7, 0.7, 0.5, 0.7, 1.5, 1.9, 2.1, 0.1, 1.1, 0.2, 0.7, 1.4, 3.5, 0.7], 
    [0.6, 0.2, 0.5, 0.3, 0.0, 0.1, 0.6, 0.5, 0.4, 0.7, 1.4, 2.1, 2.3, 0.4, 1.1, 0.4, 0.7, 1.2, 3.8, 0.6], 
    [0.7, 0.1, 0.4, 0.2, 0.1, 0.0, 0.6, 0.5, 0.3, 0.7, 1.4, 2.0, 2.2, 0.3, 1.1, 0.4, 0.7, 1.2, 3.7, 0.6], 
    [0.1, 0.5, 0.8, 0.7, 0.6, 0.6, 0.0, 0.2, 0.3, 0.1, 0.9, 2.5, 2.7, 0.7, 0.5, 0.3, 0.1, 0.7, 4.0, 0.1], 
    [0.1, 0.4, 0.8, 0.7, 0.5, 0.5, 0.2, 0.0, 0.2, 0.2, 0.9, 2.5, 2.7, 0.7, 0.6, 0.3, 0.2, 0.7, 4.0, 0.1], 
    [0.2, 0.3, 0.7, 0.5, 0.4, 0.3, 0.3, 0.2, 0.0, 0.4, 1.0, 2.4, 2.6, 0.6, 0.8, 0.3, 0.3, 0.8, 3.9, 0.3], 
    [0.2, 0.6, 0.8, 0.7, 0.7, 0.7, 0.1, 0.2, 0.4, 0.0, 0.8, 2.6, 2.8, 0.8, 0.4, 0.4, 0.1, 0.6, 4.1, 0.1], 
    [0.9, 1.3, 1.6, 1.5, 1.4, 1.4, 0.9, 0.9, 1.0, 0.8, 0.0, 3.4, 3.6, 1.5, 0.9, 1.2, 0.8, 0.6, 4.9, 0.8], 
    [2.6, 2.1, 1.8, 1.9, 2.1, 2.0, 2.5, 2.5, 2.4, 2.6, 3.4, 0.0, 0.5, 1.7, 2.9, 2.0, 2.6, 3.3, 4.1, 2.5], 
    [2.8, 2.3, 2.0, 2.1, 2.3, 2.2, 2.7, 2.7, 2.6, 2.8, 3.6, 0.5, 0.0, 1.9, 3.1, 2.2, 3.1, 3.5, 4.3, 2.7], 
    [0.8, 0.3, 0.1, 0.1, 0.4, 0.3, 0.7, 0.7, 0.6, 0.8, 1.5, 1.7, 1.9, 0.0, 1.2, 0.2, 0.8, 1.4, 4.0, 0.7], 
    [0.6, 1.0, 1.2, 1.1, 1.1, 1.1, 0.5, 0.6, 0.8, 0.4, 0.9, 2.9, 3.1, 1.2, 0.0, 0.8, 0.4, 0.6, 4.0, 0.5], 
    [0.4, 0.4, 0.3, 0.2, 0.4, 0.4, 0.3, 0.3, 0.3, 0.4, 1.2, 2.0, 2.2, 0.2, 0.8, 0.0, 0.4, 1.1, 3.5, 0.3], 
    [0.2, 0.6, 0.8, 0.7, 0.7, 0.7, 0.1, 0.2, 0.3, 0.1, 0.8, 2.6, 3.1, 0.8, 0.4, 0.4, 0.0, 0.6, 4.1, 0.3], 
    [0.7, 1.1, 1.5, 1.4, 1.2, 1.2, 0.7, 0.7, 0.8, 0.6, 0.6, 3.3, 3.5, 1.4, 0.6, 1.1, 0.6, 0.0, 4.7, 0.6], 
    [4.1, 3.8, 3.4, 3.5, 3.8, 3.7, 4.0, 4.0, 3.9, 4.1, 4.9, 4.1, 4.3, 4.0, 4.0, 3.5, 4.1, 4.7, 0.0, 4.0], 
    [0.1, 0.5, 0.8, 0.7, 0.6, 0.6, 0.1, 0.1, 0.3, 0.1, 0.8, 2.5, 2.7, 0.7, 0.5, 0.3, 0.3, 0.6, 4.0, 0.0] 
]

# start of Travelling salesman problem implementation:

def travelling_salesman_problem(starting_node, user_selected_landmarks):
    #stage one:
    placeholder = starting_node
    remaining_landmarks = user_selected_landmarks.copy()
    remaining_landmarks.remove(starting_node)

    route_so_far = [starting_node]

    walking_time = 0.0
    total_distance = 0.0

    while remaining_landmarks:
        closest_landmark = None
        closest_distance = float('inf')

        for landmark in remaining_landmarks:
            distance = distances[placeholder][landmark]
            if distance < closest_distance:
                closest_distance = distance
                closest_landmark = landmark

        route_so_far.append(closest_landmark)
        placeholder = closest_landmark
        remaining_landmarks.remove(closest_landmark)

        total_distance += closest_distance

    walking_time = total_distance / 3.1 * 60  # Convert distance to time in minutes (assuming average walking speed of 3.1 mph)


    return route_so_far, total_distance, walking_time

#parts 1 and 2:

#for i in range (20):
    #print(f"{i} : {landmarks[i]}")

#node1 = int(input("Enter a landmark number (0-19): "))
#while node1 < 0 or node1 > 19:
    #print(f"Invalid. {node1} is not in the range of 0-19")
    #print("Try again")
    #node1 = int(input("Enter a landmark number (0-19): "))
    
#print(f"you selected: {landmarks[node1]}")

#node2 =int(input("Enter a landmark number (0-19): "))
#while node2 < 0 or node2 > 19:
    #print(f"Invalid. {node2} is not in the range of 0-19")
    #print("Try again")
    #node2 = int(input("Enter a landmark number (0-19): "))

#print(f"you selected: {landmarks[node2]}")

#print("Calculating the distance between the two landmarks...")

#print(f"the distance between {landmarks[node1]} to {landmarks[node2]} is {distances[node1][node2]} miles")

# @@@ part 3 and 4:

#for i in range (20):
    #print(f"{i} : {landmarks[i]}")


#def data_type_validation(node1):
#    while not node1.isdigit():
#        print(f"Invalid. {node1} is not a a whole number or its not even a number")
#        print("try again")
#        node1 = input("Enter a landmark number (0-19): ")
#    return node1

#node1 = input("Enter a landmark number (0-19): ")
#node1 =data_type_validation(node1)
#node1 = int(node1)

#while node1 < 0 or node1 > 19:
#    print(f"Invalid. {node1} is not in the range of 0-19")
#    print("Try again")
#    node1 = input("Enter a landmark number (0-19) : ")
#    node1 = data_type_validation(node1)
#    node1 = int(node1)
    
#print(f"you selected: {landmarks[node1]}")

#if node1 == 0:
#    closest_distance_neighbour = distances[node1][1]
#    closest_landmark = landmarks[1]
#else:
#    closest_distance_neighbour = distances[node1][0]
#    closest_landmark = landmarks[0]

#for i in landmarks:
#    if i == node1:
#        continue 

#    if distances[node1][i] < closest_distance_neighbour:
#        closest_distance_neighbour = distances[node1][i]
#        closest_landmark = landmarks[i]
#        
#print(f"The closest landmark to {landmarks[node1]} is {closest_landmark} with a distance of {closest_distance_neighbour} miles.")

# ~~~~SPRINT 2~~~~:

for i in range (20):
    if landmarks[i]["visited"] == True:
        print(f"{i} : (THIS IS A VISITED LANDMARK) Landmark name = {landmarks[i]["name"]}, Categories = {", " .join(landmarks[i]["categories"])}, Time without ticket = {landmarks[i]["time_no_ticket"]} minutes, Time with ticket = {landmarks[i]["time_with_ticket"]} minutes, Ticket cost = £{landmarks[i]["ticket_cost"]:.2f} ")
    else:
        print(f"{i} : Landmark name = {landmarks[i]["name"]}, Categories = {", " .join(landmarks[i]["categories"])}, Time without ticket = {landmarks[i]["time_no_ticket"]} minutes, Time with ticket = {landmarks[i]["time_with_ticket"]} minutes, Ticket cost = £{landmarks[i]["ticket_cost"]:.2f} ")

###### Iteration 3
user_selected_landmarks = []

def manual_landmark_selection(budget_limit, time_limit, user_selected_landmarks):

    route_so_far = []
    total_distance = 0.0
    walking_time = 0.0

    print("Now you can select a landmark to visit by entering its corresponding number (0-19).")
    print("Enter 'done' once you want to stop selecting landmarks.")

    user_landmark_selection = input("Enter a landmark number (0-19): ")

    while user_landmark_selection.lower() == "done" and not user_selected_landmarks:
        print("You have not selected any landmarks yet. You must select at least one before finishing.")
        user_landmark_selection = input("Enter a landmark number (0-19): ")

    while user_landmark_selection.lower() != "done":

        user_landmark_selection = int(data_type_validation(user_landmark_selection, "landmark"))

        while user_landmark_selection > 19:
            print(f"Invalid. {user_landmark_selection} is not in the range of 0-19")
            user_landmark_selection = input("Enter a landmark number (0-19): ")
            user_landmark_selection = int(data_type_validation(user_landmark_selection, "landmark"))

        if user_landmark_selection in user_selected_landmarks:
            print(f"You have already selected {landmarks[user_landmark_selection]['name']}. Please choose a different landmark.")
            user_landmark_selection = input("Enter a landmark number (0-19) or 'done' to finish: ")
            continue

        chosen_landmark = landmarks[user_landmark_selection]

        if chosen_landmark["ticket_cost"] == 0.00:
            user_wants_ticket = "no"
            number_of_tickets = 0
        else:
            user_wants_ticket = input(f"Do you want to visit {chosen_landmark['name']} with a ticket? (yes/no): ")
            while user_wants_ticket.lower() not in ["yes", "no"]:
                print(f"Invalid. {user_wants_ticket} is not a valid response. Please enter 'yes' or 'no'.")
                user_wants_ticket = input(f"Do you want to visit {chosen_landmark['name']} with a ticket? (yes/no): ")

            if user_wants_ticket.lower() == "yes":
                number_of_tickets = input(f"How many tickets do you want? (max 6): ")
                number_of_tickets = int(data_type_validation(number_of_tickets, "tickets"))
                while number_of_tickets > 6 or number_of_tickets < 1:
                    print(f"Invalid. You cannot purchase {number_of_tickets} tickets.")
                    number_of_tickets = input(f"How many tickets do you want? (max 6): ")
                    number_of_tickets = int(data_type_validation(number_of_tickets, "tickets"))
            else:
                number_of_tickets = 0

        # Work out the cost/time this choice would add, BEFORE touching the real totals
        if user_wants_ticket.lower() == "yes":
            added_cost = chosen_landmark["ticket_cost"] * number_of_tickets
            added_time = chosen_landmark["time_with_ticket"]
        else:
            added_cost = 0.00
            added_time = chosen_landmark["time_no_ticket"]

        # --- Tentatively commit, so the TSP function can see this landmark ---
        user_selected_landmarks.append(user_landmark_selection)
        landmarks[user_landmark_selection]["visited"] = True
        chosen_landmark["have_tickets"] = (user_wants_ticket.lower() == "yes")
        chosen_landmark["number_of_tickets"] = number_of_tickets

        # Recalculate the WHOLE route fresh, now that it includes the new landmark
        route_so_far, total_distance, walking_time = travelling_salesman_problem(
            user_selected_landmarks[0], user_selected_landmarks
        )

        prospective_budget = budget_limit - added_cost
        prospective_time = (time_limit - added_time) - walking_time

        # --- Check ---
        if prospective_budget < 0 or prospective_time < 0:
            if prospective_budget < 0 and prospective_time < 0:
                print("This choice would exceed both your budget and time limit.")
            elif prospective_budget < 0:
                print(f"This choice would exceed your budget limit by £{abs(prospective_budget):.2f}.")
            else:
                print(f"This choice would exceed your time limit by {abs(prospective_time)} minutes.")

            # --- Roll back the tentative commit (nothing else needs reverting) ---
            user_selected_landmarks.remove(user_landmark_selection)
            landmarks[user_landmark_selection]["visited"] = False
            landmarks[user_landmark_selection]["have_tickets"] = False
            landmarks[user_landmark_selection]["number_of_tickets"] = 0

            print(f"Current budget limit: £{budget_limit:.2f}, Current time limit: {time_limit} minutes.")
            user_landmark_selection = input("Enter a landmark number (0-19) or 'done' to finish: ")
            continue

        # --- Only now commit the real budget/time ---
        budget_limit = prospective_budget
        time_limit = time_limit - added_time   # walking is never stored here; it's recalculated fresh each round

        print(f"You have selected {chosen_landmark['name']}.")
        print(f"Current budget limit: £{budget_limit:.2f}")
        print(f"Time remaining after accounting for walking: {time_limit - walking_time} minutes.")
        print(f"Current route: {', '.join([landmarks[i]['name'] for i in route_so_far])}")
        print(f"Total Distance: {total_distance} miles, Walking Time: {walking_time} minutes.")

        user_landmark_selection = input("Enter a landmark number (0-19) or 'done' to finish: ")

    return budget_limit, time_limit, user_selected_landmarks

budget_limit, time_limit, user_selected_landmarks = manual_landmark_selection(budget_limit, time_limit, user_selected_landmarks)

for i in user_selected_landmarks:
    if landmarks[i]["have_tickets"]:
        print(f"You have selected {landmarks[i]['name']} with {landmarks[i]["number_of_tickets"]} ticket(s).")
    else:
        print(f"You have selected {landmarks[i]['name']} without a ticket.")

print("Now you can review your selected landmarks and make any changes if needed.")

user_review_selection = input("Do you want to review your selected landmarks? (yes/no): ")

while user_review_selection.lower() not in ["yes", "no"]:
    print(f"Invalid. {user_review_selection} is not a valid response. Please enter 'yes' or 'no'.")
    user_review_selection = input("Do you want to review your selected landmarks? (yes/no): ")

while user_review_selection.lower() == "yes":
    opperation = input("Do you want to add or remove a landmark? (add/remove): ")

    while opperation.lower() not in ["add", "remove"]:
        print(f"Invalid. {opperation} is not a valid response. Please enter 'add' or 'remove'.")
        opperation = input("Do you want to add or remove a landmark? (add/remove): ")

    if opperation.lower() == "add":
        budget_limit, time_limit, user_selected_landmarks = manual_landmark_selection(budget_limit, time_limit, user_selected_landmarks)
    else:
        if len(user_selected_landmarks) == 1:
            print("You have only one landmark selected. You cannot remove it as you must have at least one landmark selected.")
        else:
            print("Here are your currently selected landmarks:")
            for i in user_selected_landmarks:
                print(f"{i} : {landmarks[i]['name']}")

            landmark_to_remove = input("Enter the number of the landmark you want to remove: ")
            landmark_to_remove = int(data_type_validation(landmark_to_remove, "manual_landmark"))

            while landmark_to_remove not in user_selected_landmarks:
                print(f"Invalid. {landmark_to_remove} is not in your selected landmarks.")
                landmark_to_remove = input("Enter the number of the landmark you want to remove: ")
                landmark_to_remove = int(data_type_validation(landmark_to_remove, "manual_landmark"))

            # Revert the budget and time for the removed landmark
            if landmarks[landmark_to_remove]["have_tickets"]:
                budget_limit += landmarks[landmark_to_remove]["ticket_cost"] * landmarks[landmark_to_remove]["number_of_tickets"]
                time_limit += landmarks[landmark_to_remove]["time_with_ticket"]
            else:
                time_limit += landmarks[landmark_to_remove]["time_no_ticket"]

            user_selected_landmarks.remove(landmark_to_remove)
            landmarks[landmark_to_remove]["visited"] = False
            landmarks[landmark_to_remove]["have_tickets"] = False
            landmarks[landmark_to_remove]["number_of_tickets"] = 0

            print(f"You have removed {landmarks[landmark_to_remove]['name']} from your selection.")

            # Recalculate the route after removal (Currently, the starting node is assumed to be the first in the list, also current time limit does not include walking time, so we need to recalculate it)

            route_so_far, total_distance, walking_time = travelling_salesman_problem(user_selected_landmarks[0], user_selected_landmarks)
            print(f"Updated route: {', '.join([landmarks[i]['name'] for i in route_so_far])}")
            print(f"Current budget limit: £{budget_limit:.2f}, Time remaining after accounting for walking: {time_limit - walking_time} minutes.")
            print(f"Total Distance: {total_distance} miles, Walking Time: {walking_time} minutes.")
            
    for i in user_selected_landmarks:
        if landmarks[i]["have_tickets"]:
            print(f"You have selected {landmarks[i]['name']} with a ticket.")
        else:
            print(f"You have selected {landmarks[i]['name']} without a ticket.")

    user_review_selection = input("Do you want to review your selected landmarks? (yes/no): ")

    while user_review_selection.lower() not in ["yes", "no"]:
        print(f"Invalid. {user_review_selection} is not a valid response. Please enter 'yes' or 'no'.")
        user_review_selection = input("Do you want to review your selected landmarks? (yes/no): ")

#saving the selected landmarks to the database
save_landmarks_to_db(landmarks)


# working with travelling salesman:

route_so_far, total_distance, walking_time = travelling_salesman_problem(user_selected_landmarks[0], user_selected_landmarks)





# storing landmark grid references as a Python dictionary

landmark_positions = {
    0: ("E", 6),
    1: ("D", 3),
    2: ("E", 3),
    3: ("D", 4),
    4: ("C", 6),
    5: ("D", 6),
    6: ("E", 7),
    7: ("F", 7),
    8: ("E", 8),
    9: ("F", 8),
    10: ("G", 4),
    11: ("F", 4),
    12: ("H", 5),
    13: ("G", 7),
    14: ("G", 9),
    15: ("G", 8),
    16: ("D", 9),
    17: ("D", 10),
    18: ("G", 1),
    19: ("A", 12)
}

# converting landmark grid references to pixel coordinates

margin = 50  

def convert_to_pixels():
    pixel_positions = {}
    for key in landmark_positions:
        letter, number = landmark_positions[key]
        x_pixel = (ord(letter) - ord('A')) * 50 + margin
        y_pixel = number * 50 + margin
        pixel_positions[key] = (x_pixel, y_pixel)
    return pixel_positions
        

pixel_positions = convert_to_pixels()

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((880, 700))
font = pygame.font.SysFont(None, 20)
legend_x =450
legend_y = 50

info_x = 450
info_y = 620

background_color = (30, 45, 80)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    for key in range(len(route_so_far) - 1):
            start_key = route_so_far[key]
            end_key = route_so_far[key + 1]
            start_pos = pixel_positions[start_key]
            end_pos = pixel_positions[end_key]
            pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 3) # colour for the route lines

    for key in pixel_positions:
        x, y = pixel_positions[key]
        if key == user_selected_landmarks[0]:
            pygame.draw.circle(screen, (255, 215, 0), (x, y), 10) # colour for the first selected landmark
        elif key in user_selected_landmarks[1:]:
            pygame.draw.circle(screen, (135, 206, 235), (x, y), 10) # colour for the landmarks in the list except the first one
        else:
            pygame.draw.circle(screen, (85, 85, 165), (x, y), 10) # colour for the landmarks not in the list

        text_surface = font.render(str(key), True, (30, 45, 80))
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    line_spacing = 25 
    for index in landmarks:
        name = landmarks[index]["name"]
        if index == route_so_far[0]:
            text_surface = font.render(f"{index}: {name}, {'(with ticket)' if landmarks[index]['have_tickets'] else '(without ticket)'}", True, (255, 215, 0)) # colour for the first selected landmark
        elif index in route_so_far[1:]:
            text_surface = font.render(f"{index}: {name}, {'(with ticket)' if landmarks[index]['have_tickets'] else '(without ticket)'}", True, (135, 206, 235)) # colour for the landmarks in the list except the first one
        else:
            text_surface = font.render(f"{index}: {name}", True, (255, 255, 255)) # colour for the landmarks not in the list
        screen.blit(text_surface, (legend_x, legend_y + index * line_spacing))

    distance_text = font.render(f"Total Distance: {total_distance :.2f} miles", True, (255, 126, 95))
    time_text = font.render(f"Time of journey: {(initial_time_limit - time_limit + walking_time):.2f} minutes", True, (234, 162, 85))
    budget_text = font.render(f"Cost: £{(initial_budget_limit - budget_limit):.2f}", True, (147, 197, 114))

    screen.blit(distance_text, (info_x, info_y))
    screen.blit(time_text, (info_x, info_y + line_spacing))
    screen.blit(budget_text, (info_x, info_y + 2 * line_spacing))

    pygame.display.flip()


pygame.quit()






