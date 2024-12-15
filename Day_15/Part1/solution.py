def parse_input(map_lines, move_sequence):
    warehouse = [list(line) for line in map_lines.strip().splitlines()]
    moves = move_sequence.replace("\n", "") 
    return warehouse, moves

def find_robot_and_boxes(warehouse):
    robot_position = None
    box_positions = []
    for y, row in enumerate(warehouse):
        for x, cell in enumerate(row):
            if cell == '@':
                robot_position = (y, x)
            elif cell == 'O':
                box_positions.append((y, x))
    return robot_position, box_positions

def move_robot(warehouse, robot_pos, box_positions, direction):
    dy, dx = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}[direction]
    new_robot_y, new_robot_x = robot_pos[0] + dy, robot_pos[1] + dx

    if warehouse[new_robot_y][new_robot_x] == '#':
        return robot_pos, box_positions 

    if (new_robot_y, new_robot_x) in box_positions:
        moving_boxes = []
        current_y, current_x = new_robot_y, new_robot_x

        while (current_y, current_x) in box_positions:
            moving_boxes.append((current_y, current_x))
            current_y += dy
            current_x += dx

        if warehouse[current_y][current_x] == '#' or (current_y, current_x) in box_positions:
            return robot_pos, box_positions

        for y, x in reversed(moving_boxes):
            box_positions.remove((y, x))
            box_positions.append((y + dy, x + dx))

    return (new_robot_y, new_robot_x), box_positions

def calculate_gps_sum(box_positions, warehouse_height, warehouse_width):
    gps_sum = 0
    for y, x in box_positions:
        gps_sum += 100 * y + x
    return gps_sum

def simulate_warehouse_from_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    split_index = lines.index('\n') if '\n' in lines else lines.index('')
    map_lines = ''.join(lines[:split_index]).strip()
    move_sequence = ''.join(lines[split_index + 1:]).strip()

    warehouse, moves = parse_input(map_lines, move_sequence)
    robot_pos, box_positions = find_robot_and_boxes(warehouse)

    for move in moves:
        robot_pos, box_positions = move_robot(warehouse, robot_pos, box_positions, move)

    return calculate_gps_sum(box_positions, len(warehouse), len(warehouse[0]))

if __name__ == "__main__":
    input_file = "input.txt"
    result = simulate_warehouse_from_file(input_file)
    print(result)
