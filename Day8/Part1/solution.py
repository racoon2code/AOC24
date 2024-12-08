file_path = "C:\dev\AOC24\Day8\Part1\input.txt"

with open(file_path, 'r') as file:
        map = [line.strip() for line in file.readlines()]

def calculate_antinodes(p1, p2):
    antinodes = set()
    
    x1, y1 = p1
    x2, y2 = p2
    
    dx = x2 - x1
    dy = y2 - y1
    
    ax1 = x1 - dx
    ay1 = y1 - dy
    antinodes.add((ax1, ay1))
    
    ax2 = x2 + dx
    ay2 = y2 + dy
    antinodes.add((ax2, ay2))
    
    return antinodes

def is_within_bounds(point, grid):
    x, y = point
    
    max_y = len(grid)
    max_x = len(grid[0]) if max_y > 0 else 0
    
    
    return 0 <= x < max_x and 0 <= y < max_y



antennas = {}
for y, row in enumerate(map):
    for x, cell in enumerate(row):
        if cell != '.':
            if cell not in antennas:
                antennas[cell] = []
            antennas[cell].append((x, y))


antinodes = set()
for freq, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            p1, p2 = positions[i], positions[j]
            
            new_nodes = calculate_antinodes(p1, p2)
            antinodes.update(new_nodes)


unique_antinodes = set(node for node in antinodes if is_within_bounds(node, map))


print(len(unique_antinodes))
