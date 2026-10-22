# Stage 2: storing landmark grid references as a Python dictionary

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

# Stage 3: converting landmark grid references to pixel coordinates
def convert_to_pixels():
    for key in landmark_positions:
        letter, number = landmark_positions[key]
        x_pixel = (ord(letter) - ord('A')) * 50
        y_pixel = number * 50
        landmark_positions[key] = (x_pixel, y_pixel)

convert_to_pixels()
# test it
print(landmark_positions)
