# Bewegungsrichtungen und Rotationen
DIRECTIONS = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
ROTATE_RIGHT = {'^': '>', '>': 'v', 'v': '<', '<': '^'}


def parse_map(map_data):
    width, height = len(map_data[0]), len(map_data)
    for y in range(height):
        for x in range(width):
            if map_data[y][x] in DIRECTIONS:
                return x, y, map_data[y][x]
    raise ValueError("Keine Startposition für den Wachmann gefunden!")


def simulate_guard(map_data):
    
    x, y, direction = parse_map(map_data)
    visited_positions = set()
    height, width = len(map_data), len(map_data[0])  # Größe der Karte
    steps = 0  # Schrittzähler

    
    while True:
        steps += 1
        if steps > 10000:  # Abbruchbedingung für Debugging
            print("Schleife läuft zu lange.")
            break

        # Prüfen, ob die aktuelle Position außerhalb der Karte liegt
        if not (0 <= x < width and 0 <= y < height):
            print(f"Wachmann hat die Karte bei Schritt {steps} verlassen.")
            break

        
        visited_positions.add((x, y))
        print(f"Schritt {steps}: Position ({x}, {y}), Richtung {direction}")

        
        dx, dy = DIRECTIONS[direction]
        nx, ny = x + dx, y + dy

        # Prüfen, ob die nächste Position ein Hindernis ist
        if 0 <= nx < width and 0 <= ny < height and map_data[ny][nx] == '#':
            # Hindernis: Drehen
            direction = ROTATE_RIGHT[direction]
        else:
            # Vorwärts bewegen
            x, y = nx, ny
    return len(visited_positions)


def load_map_from_file(filename):
    with open(filename, 'r') as file:
        map_data = [line.strip() for line in file.readlines()]
    
    
    max_width = max(len(line) for line in map_data)
    map_data = [line.ljust(max_width, ' ') for line in map_data]
    return map_data


if __name__ == "__main__":
    try:
        map_input = load_map_from_file("input.txt") 
        visited_count = simulate_guard(map_input)
        print("Anzahl der besuchten Positionen:", visited_count)
    except Exception as e:
        print("Fehler:", str(e))
