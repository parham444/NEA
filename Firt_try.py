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

con_time_limit = input("Do you want to continue with the time limit you have entered? (yes/no): ")

while con_time_limit.lower() not in ["yes", "no"]:
    print(f"Invalid. {con_time_limit} is not a valid response. Please enter 'yes' or 'no'.")
    con_time_limit = input("Do you want to continue with the time limit you have entered? (yes/no): ")

while con_time_limit.lower() == "no":
    time_limit = get_user_time_limit()
    con_time_limit = input("Do you want to continue with the time limit you have entered? (yes/no): ")
    while con_time_limit.lower() not in ["yes", "no"]:
        print(f"Invalid. {con_time_limit} is not a valid response. Please enter 'yes' or 'no'.")
        con_time_limit = input("Do you want to continue with the time limit you have entered? (yes/no): ")

# budget limit:
def get_user_budget_limit():
    budget_limit = 0
    print("Here you can submit your budget limit, you can do this by entering the amount of budget that you have into two boxes of pounds and pence.")
    print("For example, if you have £20.50, you would enter 20 into the pounds box and 50 into the pence box.")
    print("Also you must enter your time limit in whole numbers only.")
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

con_budget_limit = input("Do you want to continue with the budget limit you have entered? (yes/no): ")

while con_budget_limit.lower() not in ["yes", "no"]:
    print(f"Invalid. {con_budget_limit} is not a valid response. Please enter 'yes' or 'no'.")
    con_budget_limit = input("Do you want to continue with the budget limit you have entered? (yes/no): ")

while con_budget_limit.lower() == "no":
    budget_limit = get_user_budget_limit()
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




    

# Time values are in MINUTES, cost values are in POUNDS (£)
landmarks = {
    0: {
        "name": "St Albans Cathedral",
        "categories": ["historic", "religious"],
        "time_no_ticket": 30,      # free entry; general visit browsing the nave/interior
        "time_with_ticket": 60,    # optional donation-based tower tour / guided tour adds time
        "ticket_cost": 5.00,       # estimated - optional tower tour donation, not compulsory
        "visited": False,
        "have_tickets": False
    },
    1: {
        "name": "Verulamium Park and Verulamium Lake",
        "categories": ["park", "outdoor"],
        "time_no_ticket": 40,      # free public park, walk around lake/grounds
        "time_with_ticket": 40,    # no ticketed element to the park itself
        "ticket_cost": 0.00,
        "visited": False,
        "have_tickets": False
    },
    2: {
        "name": "The Roman Theatre of Verulamium",
        "categories": ["historic", "roman"],
        "time_no_ticket": 0,       # cannot view without paying - gated site
        "time_with_ticket": 30,
        "ticket_cost": 3.00,       # confirmed via Gorhambury Estate site (adult price)
        "visited": False,
        "have_tickets": False
    },
    3: {
        "name": "Verulamium Museum",
        "categories": ["historic", "roman", "museum"],
        "time_no_ticket": 0,       # cannot view without paying - ticketed museum
        "time_with_ticket": 75,
        "ticket_cost": 10.00,      # confirmed via stalbansmuseums.org.uk (adult price)
        "visited": False,
        "have_tickets": False
    },
    4: {
        "name": "The Roman Wall of St Albans",
        "categories": ["historic", "roman", "outdoor"],
        "time_no_ticket": 15,      # free, outdoor remains viewable any time
        "time_with_ticket": 15,
        "ticket_cost": 0.00,
        "visited": False,
        "have_tickets": False
    },
    5: {
        "name": "The Hypocaust and Roman Mosaic",
        "categories": ["historic", "roman"],
        "time_no_ticket": 15,      # confirmed free to visit (stalbansmuseums.org.uk)
        "time_with_ticket": 15,
        "ticket_cost": 0.00,
        "visited": False,
        "have_tickets": False
    },
    6: {
        "name": "St Albans Clock Tower",
        "categories": ["historic"],
        "time_no_ticket": 10,      # viewing from outside, free
        "time_with_ticket": 25,    # climbing the tower has a small entry fee (seasonal)
        "ticket_cost": 1.00,       # estimated - small councils typically charge ~£1 for tower climbs
        "visited": False,
        "have_tickets": False
    },
    7: {
        "name": "Abbey Gateway (The Great Gate)",
        "categories": ["historic"],
        "time_no_ticket": 10,      # viewed from outside, free (part of school grounds)
        "time_with_ticket": 10,
        "ticket_cost": 0.00,
        "visited": False,
        "have_tickets": False
    },
    8: {
        "name": "Ye Olde Fighting Cocks Inn",
        "categories": ["historic", "food_drink"],
        "time_no_ticket": 30,      # visiting as a pub - no entry fee, time = having a drink/meal
        "time_with_ticket": 30,
        "ticket_cost": 0.00,
        "visited": False,
        "have_tickets": False
    },
    9: {
        "name": "St Albans Museum + Gallery (Old Town Hall)",
        "categories": ["museum", "art"],
        "time_no_ticket": 45,      # estimated - free entry, typical small museum browsing time
        "time_with_ticket": 45,
        "ticket_cost": 0.00,
        "visited": False,
        "have_tickets": False
    },
    10: {
        "name": "Sopwell Nunnery Ruins (Lee Hall)",
        "categories": ["historic"],
        "time_no_ticket": 15,      # free outdoor ruins site
        "time_with_ticket": 15,
        "ticket_cost": 0.00,
        "visited": False,
        "have_tickets": False
    },
    11: {
        "name": "Old Gorhambury House",
        "categories": ["historic"],
        "time_no_ticket": 10,      # ruins visible from outside only, free
        "time_with_ticket": 10,
        "ticket_cost": 0.00,
        "visited": False, 
        "have_tickets": False
    },
    12: {
        "name": "Gorhambury House",
        "categories": ["historic", "art"],
        "time_no_ticket": 0,       # private house - only accessible via guided tour
        "time_with_ticket": 90,    # estimated - stately home guided tours typically ~1.5hrs
        "ticket_cost": 12.00,      # estimated - comparable to similar small stately home tours
        "visited": False,
        "have_tickets": False
    },
    13: {
        "name": "St Michael's Church",
        "categories": ["historic", "religious"],
        "time_no_ticket": 20,      # free entry parish church
        "time_with_ticket": 20,
        "ticket_cost": 0.00,
        "visited": False, 
        "have_tickets": False
    },
    14: {
        "name": "St Peter's Church",
        "categories": ["historic", "religious"],
        "time_no_ticket": 20,      # free entry parish church
        "time_with_ticket": 20,
        "ticket_cost": 0.00,
        "visited": False,
        "have_tickets": False
    },
    15: {
        "name": "Fishpool Street Historic Area",
        "categories": ["historic"],
        "time_no_ticket": 20,      # free, walking through a historic street
        "time_with_ticket": 20,
        "ticket_cost": 0.00,
        "visited": False, 
        "have_tickets": False
    },
    16: {
        "name": "St Albans Charter Market",
        "categories": ["market", "shopping"],
        "time_no_ticket": 30,      # free open-air market, browsing time
        "time_with_ticket": 30,
        "ticket_cost": 0.00,
        "visited": False,
        "have_tickets": False
    },
    17: {
        "name": "St Albans South Signal Box",
        "categories": ["historic"],
        "time_no_ticket": 15,      # viewed from outside; open days are free/donation-based
        "time_with_ticket": 15,
        "ticket_cost": 0.00,
        "visited": False, 
        "have_tickets": False
    },
    18: {
        "name": "Redbournbury Watermill & Bakery",
        "categories": ["historic", "food_drink"],
        "time_no_ticket": 20,      # estimated - free to look around bakery/shop area
        "time_with_ticket": 45,    # guided mill tour on open days
        "ticket_cost": 4.00,       # estimated - typical small working-mill tour price
        "visited": False, 
        "have_tickets": False
    },
    19: {
        "name": "The Vintry Garden",
        "categories": ["park", "outdoor"],
        "time_no_ticket": 10,      # free small public garden
        "time_with_ticket": 10,
        "ticket_cost": 0.00,
        "visited": False, 
        "have_tickets": False
    }
}


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

        # Work out the cost/time this choice WOULD add, without committing to it yet
        if user_wants_ticket.lower() == "yes":
            added_cost = chosen_landmark["ticket_cost"] * number_of_tickets
            added_time = chosen_landmark["time_with_ticket"]
            chosen_landmark["have_tickets"] = True
        else:
            added_cost = 0.00
            added_time = chosen_landmark["time_no_ticket"]

        prospective_budget = budget_limit - added_cost
        prospective_time = time_limit - added_time

        # Check BEFORE committing - so there is nothing to revert if it fails
        if prospective_budget < 0 or prospective_time < 0:
            if prospective_budget < 0 and prospective_time < 0:
                print("This choice would exceed both your budget and time limit.")
            elif prospective_budget < 0:
                print(f"This choice would exceed your budget limit by £{abs(prospective_budget):.2f}.")
            else:
                print(f"This choice would exceed your time limit by {abs(prospective_time)} minutes.")

            print(f"Current budget limit: £{budget_limit:.2f}, Current time limit: {time_limit} minutes.")
            user_landmark_selection = input("Enter a landmark number (0-19) or 'done' to finish: ")
            continue

        # Only commit once we know it's safe
        budget_limit = prospective_budget
        time_limit = prospective_time
        user_selected_landmarks.append(user_landmark_selection)
        landmarks[user_landmark_selection]["visited"] = True

        print(f"You have selected {chosen_landmark['name']}.")
        print(f"Current budget limit: £{budget_limit:.2f}, Current time limit: {time_limit} minutes.")

        user_landmark_selection = input("Enter a landmark number (0-19) or 'done' to finish: ")


    return budget_limit, time_limit, user_selected_landmarks

budget_limit, time_limit, user_selected_landmarks = manual_landmark_selection(budget_limit, time_limit, user_selected_landmarks)

for i in user_selected_landmarks:
    if landmarks[i]["have_tickets"]:
        print(f"You have selected {landmarks[i]['name']} with a ticket.")
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
            landmark_to_remove = int(data_type_validation(landmark_to_remove, "landmark"))

            while landmark_to_remove not in user_selected_landmarks:
                print(f"Invalid. {landmark_to_remove} is not in your selected landmarks.")
                landmark_to_remove = input("Enter the number of the landmark you want to remove: ")
                landmark_to_remove = int(data_type_validation(landmark_to_remove, "landmark"))

            # Revert the budget and time for the removed landmark
            if landmarks[landmark_to_remove]["have_tickets"]:
                budget_limit += landmarks[landmark_to_remove]["ticket_cost"]
                time_limit += landmarks[landmark_to_remove]["time_with_ticket"]
            else:
                time_limit += landmarks[landmark_to_remove]["time_no_ticket"]

            user_selected_landmarks.remove(landmark_to_remove)
            landmarks[landmark_to_remove]["visited"] = False
            landmarks[landmark_to_remove]["have_tickets"] = False

            print(f"You have removed {landmarks[landmark_to_remove]['name']} from your selection.")
            print(f"Current budget limit: £{budget_limit:.2f}, Current time limit: {time_limit} minutes.")

    for i in user_selected_landmarks:
        if landmarks[i]["have_tickets"]:
            print(f"You have selected {landmarks[i]['name']} with a ticket.")
        else:
            print(f"You have selected {landmarks[i]['name']} without a ticket.")

    user_review_selection = input("Do you want to review your selected landmarks? (yes/no): ")

    while user_review_selection.lower() not in ["yes", "no"]:
        print(f"Invalid. {user_review_selection} is not a valid response. Please enter 'yes' or 'no'.")
        user_review_selection = input("Do you want to review your selected landmarks? (yes/no): ")

