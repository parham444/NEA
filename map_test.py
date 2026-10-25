import pygame

user_selected_landmark = [5, 0, 13, 2] # placeholder test list
route_so_far = user_selected_landmark # placeholder for the route so far

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
} # placeholder for the landmarks dictionary

time_limit = 30  # minutes
budget_limit = 100  # pounds
total_distance = 5  # miles
initial_time_limit = 1000
initial_budget_limit = 1000


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
screen = pygame.display.set_mode((800, 700))
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
        if key == user_selected_landmark[0]:
            pygame.draw.circle(screen, (255, 215, 0), (x, y), 10) # colour for the first selected landmark
        elif key in user_selected_landmarks[1:]:
            pygame.draw.circle(screen, (135, 206, 235), (x, y), 10) # colour for the landmarks in the list except the first one
        else:
            pygame.draw.circle(screen, (85, 85, 165), (x, y), 10) # colour for the landmarks not in the list

        text_surface = font.render(str(key), True, (30, 45, 80))
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    line_spacing = 25 
    for index, name in landmarks.items():
        if index == route_so_far[0]:
            text_surface = font.render(f"{index}: {name}", True, (255, 215, 0)) # colour for the first selected landmark
        elif index in route_so_far[1:]:
            text_surface = font.render(f"{index}: {name}", True, (135, 206, 235)) # colour for the landmarks in the list except the first one
        else:
            text_surface = font.render(f"{index}: {name}", True, (255, 255, 255)) # colour for the landmarks not in the list
        screen.blit(text_surface, (legend_x, legend_y + index * line_spacing))

    distance_text = font.render(f"Total Distance: {total_distance} miles", True, (255, 126, 95))
    time_text = font.render(f"Time of journey: {initial_time_limit - time_limit} minutes", True, (234, 162, 85))
    budget_text = font.render(f"Cost: £{initial_budget_limit - budget_limit}", True, (147, 197, 114))

    screen.blit(distance_text, (info_x, info_y))
    screen.blit(time_text, (info_x, info_y + line_spacing))
    screen.blit(budget_text, (info_x, info_y + 2 * line_spacing))

    pygame.display.flip()


pygame.quit()




