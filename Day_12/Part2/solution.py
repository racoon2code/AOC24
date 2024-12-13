import numpy as np

DIRECTIONS = {
    (-1,  0): 0,
    ( 0,  1): 1,
    ( 1,  0): 2,
    ( 0, -1): 3,
}

def parse_input(filename: str) -> np.array:
    with open(filename, 'r') as f:
        mat = [list(line.strip()) for line in f.readlines()]
    return np.array(mat, dtype="U1")

def explore_region_and_calculate_fencing_cost(
        starting_point: tuple[int, int],
        grid: np.array,
        visited: np.array
) -> int:
    i_max, j_max = grid.shape
    is_perimeter = np.zeros((i_max + 4, j_max + 4, 4), dtype=bool)
    queue = [starting_point]
    region_type = grid[starting_point]
    region_area = 0
    region_sides = 0

    while queue:
        i, j = queue.pop(0)
        if visited[i, j]:
            continue
        visited[i, j] = True
        region_area += 1

        # Check neighbors
        neighbors = ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))
        for next_i, next_j in neighbors:
            if 0 <= next_i < i_max and 0 <= next_j < j_max and grid[next_i, next_j] == region_type:
                queue.append((next_i, next_j))
            else:
                direction = DIRECTIONS.get((next_i - i, next_j - j))
                if direction is not None:
                    if not (
                        is_perimeter[next_i + 3, next_j + 2, direction] or
                        is_perimeter[next_i + 2, next_j + 3, direction] or
                        is_perimeter[next_i + 1, next_j + 2, direction] or
                        is_perimeter[next_i + 2, next_j + 1, direction]
                    ):
                        region_sides += 1
                    is_perimeter[next_i + 2, next_j + 2, direction] = True

    return region_area * region_sides

def calculate_overall_fencing_cost(grid: np.array) -> int:
    i_max, j_max = grid.shape
    visited = np.zeros((i_max, j_max), dtype=bool)
    total_cost = 0

    for i in range(i_max):
        for j in range(j_max):
            if not visited[i, j]:
                total_cost += explore_region_and_calculate_fencing_cost((i, j), grid, visited)

    return total_cost

def main():
    garden_grid = parse_input("input.txt")

    total_price = calculate_overall_fencing_cost(garden_grid)

    print(total_price)

if __name__ == "__main__":
    main()
