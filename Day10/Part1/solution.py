def read_map(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(map_data):
    trailheads = []
    for r, row in enumerate(map_data):
        for c, val in enumerate(row):
            if val == 0:
                trailheads.append((r, c))
    return trailheads

def find_reachable_nines(map_data, start):
    rows, cols = len(map_data), len(map_data[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    stack = [start]
    reachable_nines = set()
    
    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        current_height = map_data[r][c]
        
        
        if current_height == 9:
            reachable_nines.add((r, c))
        
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:  
                next_height = map_data[nr][nc]
                if next_height == current_height + 1:  
                    stack.append((nr, nc))
    
    return reachable_nines

def calculate_trailhead_scores(map_data):
    trailheads = find_trailheads(map_data)
    total_score = 0
    
    for trailhead in trailheads:
        reachable_nines = find_reachable_nines(map_data, trailhead)
        total_score += len(reachable_nines)
    
    return total_score

def main():
    
    map_data = read_map("input.txt")
    
    
    total_score = calculate_trailhead_scores(map_data)
    
    print(total_score)

if __name__ == "__main__":
    main()
