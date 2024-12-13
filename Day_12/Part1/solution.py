def read_input(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def get_neighbors(x, y, grid):
    rows, cols = len(grid), len(grid[0])
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors

def flood_fill(grid, visited, x, y, plant_type):
    stack = [(x, y)]
    visited.add((x, y))
    area = 0
    perimeter = 0

    while stack:
        cx, cy = stack.pop()
        area += 1

        for nx, ny in get_neighbors(cx, cy, grid):
            if grid[nx][ny] == plant_type:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
            else:
                perimeter += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                perimeter += 1

    return area, perimeter

def calculate_fence_cost(grid):
    visited = set()
    total_cost = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                plant_type = grid[x][y]
                area, perimeter = flood_fill(grid, visited, x, y, plant_type)
                cost = area * perimeter
                total_cost += cost

    return total_cost

def main():
    grid = read_input("input.txt")
    total_cost = calculate_fence_cost(grid)
    print(total_cost)

if __name__ == "__main__":
    main()