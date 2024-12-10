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

def count_distinct_trails(map_data, start):
    rows, cols = len(map_data), len(map_data[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cache = {}  
    
    def dfs(r, c):
        if (r, c) in cache:  
            return cache[(r, c)]
        
        current_height = map_data[r][c]
        if current_height == 9:  
            return 1
        
        total_trails = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols: 
                if map_data[nr][nc] == current_height + 1: 
                    total_trails += dfs(nr, nc)
        
        cache[(r, c)] = total_trails  
        return total_trails
    
    return dfs(*start)

def calculate_trailhead_ratings(map_data):
    trailheads = find_trailheads(map_data)
    total_rating = 0
    
    for trailhead in trailheads:
        rating = count_distinct_trails(map_data, trailhead)
        total_rating += rating
    
    return total_rating

def main():
    
    map_data = read_map("input.txt")
    
    # Calculate total rating
    total_rating = calculate_trailhead_ratings(map_data)
    
    print(total_rating)

if __name__ == "__main__":
    main()
