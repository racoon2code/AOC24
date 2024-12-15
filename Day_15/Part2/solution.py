import sys
import re
from collections import deque
import pyperclip as pc

def log_and_copy_result(result):
    print(result)
    pc.copy(result)

sys.setrecursionlimit(10**6)

# Bewegungsrichtungen: oben, rechts, unten, links
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def extract_numbers_from_string(s):
    return [int(x) for x in re.findall(r'-?\d+', s)] 

input_filename = 'input.txt'
data = open(input_filename).read().strip()

warehouse_map, robot_movements = data.split('\n\n')
warehouse = warehouse_map.split('\n')

def navigate_warehouse(warehouse):
    rows = len(warehouse)
    cols = len(warehouse[0])

    
    expanded_warehouse = []
    for row in range(rows):
        new_row = []
        for col in range(cols):
            if warehouse[row][col] == '#':
                new_row.append('#')
                new_row.append('#')
            elif warehouse[row][col] == 'O':
                new_row.append('[')
                new_row.append(']')
            elif warehouse[row][col] == '.':
                new_row.append('.')
                new_row.append('.')
            elif warehouse[row][col] == '@':
                new_row.append('@')
                new_row.append('.')
        expanded_warehouse.append(new_row)
    warehouse = expanded_warehouse
    cols *= 2 

    robot_row, robot_col = -1, -1
    for row in range(rows):
        for col in range(cols):
            if warehouse[row][col] == '@':
                robot_row, robot_col = row, col
                warehouse[row][col] = '.' 

    current_row, current_col = robot_row, robot_col  

    for movement in robot_movements:
        if movement == '\n':
            continue

        delta_row, delta_col = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[movement]
        new_row, new_col = current_row + delta_row, current_col + delta_col

        if warehouse[new_row][new_col] == '#':
            continue

        elif warehouse[new_row][new_col] == '.':
            current_row, current_col = new_row, new_col

        elif warehouse[new_row][new_col] in ['[', ']', 'O']:
            queue = deque([(current_row, current_col)])
            visited = set()
            is_move_valid = True

            while queue:
                current_r, current_c = queue.popleft()
                if (current_r, current_c) in visited:
                    continue
                visited.add((current_r, current_c))

                next_r, next_c = current_r + delta_row, current_c + delta_col
                if warehouse[next_r][next_c] == '#':
                    is_move_valid = False
                    break
                if warehouse[next_r][next_c] == 'O':
                    queue.append((next_r, next_c))
                if warehouse[next_r][next_c] == '[':
                    queue.append((next_r, next_c))
                    assert warehouse[next_r][next_c + 1] == ']'
                    queue.append((next_r, next_c + 1))
                if warehouse[next_r][next_c] == ']':
                    queue.append((next_r, next_c))
                    assert warehouse[next_r][next_c - 1] == '['
                    queue.append((next_r, next_c - 1))

            if not is_move_valid:
                continue

            while visited:
                for r, c in sorted(visited):
                    next_r, next_c = r + delta_row, c + delta_col
                    if (next_r, next_c) not in visited:
                        assert warehouse[next_r][next_c] == '.'
                        warehouse[next_r][next_c] = warehouse[r][c]
                        warehouse[r][c] = '.'
                        visited.remove((r, c))
            current_row, current_col = current_row + delta_row, current_col + delta_col

    result = 0
    for r in range(rows):
        for c in range(cols):
            if warehouse[r][c] in ['[', 'O']:
                result += 100 * r + c

    return result

# Ausgabe der Lösung für Part 2
log_and_copy_result(navigate_warehouse(warehouse))  # Nur Part 2 ausführen
