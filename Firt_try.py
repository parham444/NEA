
landmarks = {
    0: "St Albans Cathedral",
    1: "Verulamium Park and Verulamium Lake",
    2: "The Roman Theatre of Verulamium",
    3: "Verulamium Museum",
    4: "The Roman Wall of St Albans",
    5: "The Hypocaust and Roman Mosaic",
    6: "St Albans Clock Tower",
    7: "Abbey Gateway (The Great Gate)",
    8: "Ye Olde Fighting Cocks Inn",
    9: "St Albans Museum + Gallery (Old Town Hall)",
    10: "Sopwell Nunnery Ruins (Lee Hall)",
    11: "Old Gorhambury House",
    12: "Gorhambury House",
    13: "St Michael's Church",
    14: "St Peter's Church",
    15: "Fishpool Street Historic Area",
    16: "St Albans Charter Market",
    17: "St Albans South Signal Box",
    18: "Redbournbury Watermill & Bakery",
    19: "The Vintry Garden"
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

# part 3 and 4:

for i in range (20):
    print(f"{i} : {landmarks[i]}")

node1 = input("Enter a landmark number (0-19): ")
while not node1.isdigit():
    print(f"Invalid. {node1} is not a a whole number or its not even a number")
    print("try again")
    node1 = input("Enter a landmark number (0-19): ")

node1 = int(node1)
while node1 < 0 or node1 > 19:
    print(f"Invalid. {node1} is not in the range of 0-19")
    print("Try again")
    node1 = int(input("Enter a landmark number (0-19): "))
    
print(f"you selected: {landmarks[node1]}")

if node1 == 0:
    closest_distance_neighbour = distances[node1][1]
    closest_landmark = landmarks[1]
else:
    closest_distance_neighbour = distances[node1][0]
    closest_landmark = landmarks[0]

for i in landmarks:
    if i == node1:
        continue 

    if distances[node1][i] < closest_distance_neighbour:
        closest_distance_neighbour = distances[node1][i]
        closest_landmark = landmarks[i]
        
print(f"The closest landmark to {landmarks[node1]} is {closest_landmark} with a distance of {closest_distance_neighbour} miles.")
