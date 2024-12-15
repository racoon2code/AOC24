import heapq

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
    return abs(x - end_x) + abs(y - end_y)

def find_lowest_score(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = start
    end_x, end_y = end

    pq = [(0, start_x, start_y, 'E')]  
    visited = set()
    
    while pq:
        cost, x, y, direction = heapq.heappop(pq)

        if (x, y) == (end_x, end_y):
            return cost

        state = (x, y, direction)
        if state in visited:
            continue
        visited.add(state)

        nx, ny = x + DX[direction], y + DY[direction]
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
            heapq.heappush(pq, (cost + 1, nx, ny, direction))
        
        current_dir_idx = DIRECTIONS.index(direction)
        for rotation, delta in [('CW', 1), ('CCW', -1)]:
            new_dir = DIRECTIONS[(current_dir_idx + delta) % 4]
            heapq.heappush(pq, (cost + 1000, x, y, new_dir))
    
    return -1 

def main():
    grid, start, end = parse_input('input.txt')
    lowest_score = find_lowest_score(grid, start, end)
    print(f"Lowest score: {lowest_score}")

if __name__ == '__main__':
    main()
