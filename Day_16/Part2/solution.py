import heapq
from collections import defaultdict

# Define directions and their movement offsets
DIRECTIONS = ['N', 'E', 'S', 'W']
DX = {'N': -1, 'E': 0, 'S': 1, 'W': 0}
DY = {'N': 0, 'E': 1, 'S': 0, 'W': -1}

def parse_input(file_path):
    with open(file_path, 'r') as f:
        grid = [line.strip() for line in f]
    start, end = None, None
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)
    return grid, start, end

def heuristic(x, y, end_x, end_y):
    """Manhattan distance heuristic."""
    return abs(x - end_x) + abs(y - end_y)

def find_lowest_score(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = start
    end_x, end_y = end

    pq = [(0, start_x, start_y, 'E')] 
    costs = defaultdict(lambda: float('inf'))
    costs[(start_x, start_y, 'E')] = 0
    backtrack = defaultdict(list)
    
    while pq:
        cost, x, y, direction = heapq.heappop(pq)

        if cost > costs[(x, y, direction)]:
            continue

        nx, ny = x + DX[direction], y + DY[direction]
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
            new_cost = cost + 1
            if new_cost <= costs[(nx, ny, direction)]:
                costs[(nx, ny, direction)] = new_cost
                backtrack[(nx, ny, direction)].append((x, y, direction))
                heapq.heappush(pq, (new_cost, nx, ny, direction))

        current_dir_idx = DIRECTIONS.index(direction)
        for delta in [1, -1]:  # CW and CCW
            new_dir = DIRECTIONS[(current_dir_idx + delta) % 4]
            new_cost = cost + 1000
            if new_cost <= costs[(x, y, new_dir)]:
                costs[(x, y, new_dir)] = new_cost
                backtrack[(x, y, new_dir)].append((x, y, direction))
                heapq.heappush(pq, (new_cost, x, y, new_dir))
    
    return costs, backtrack

def find_tiles_on_best_paths(grid, start, end, costs, backtrack):
    rows, cols = len(grid), len(grid[0])
    end_x, end_y = end

    min_cost = min(costs[(end_x, end_y, direction)] for direction in DIRECTIONS)

    best_path_tiles = set()
    queue = [(end_x, end_y, direction) for direction in DIRECTIONS if costs[(end_x, end_y, direction)] == min_cost]
    
    while queue:
        x, y, direction = queue.pop()
        best_path_tiles.add((x, y))
        for prev_state in backtrack[(x, y, direction)]:
            if prev_state not in queue:
                queue.append(prev_state)
    
    return best_path_tiles

def mark_best_path_tiles(grid, best_path_tiles):
    marked_grid = [list(row) for row in grid]
    for x, y in best_path_tiles:
        if marked_grid[x][y] not in ('S', 'E', '#'):
            marked_grid[x][y] = 'O'
    return [''.join(row) for row in marked_grid]

def main():
    grid, start, end = parse_input('input.txt')
    costs, backtrack = find_lowest_score(grid, start, end)
    best_path_tiles = find_tiles_on_best_paths(grid, start, end, costs, backtrack)
    marked_grid = mark_best_path_tiles(grid, best_path_tiles)
    for row in marked_grid:
        print(row)
    print(f"Number of tiles on the best paths: {len(best_path_tiles)}")

if __name__ == '__main__':
    main()
