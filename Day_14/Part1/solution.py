def parse_input(text):
    import re
    robots = []
    for line in text.strip().split("\n"):
        position = tuple(map(int, re.findall(r"p=([\d,]+)", line)[0].split(",")))
        velocity = tuple(map(int, re.findall(r"v=([\d,\-]+)", line)[0].split(",")))
        robots.append((position, velocity))
    return robots

def simulate_robot_step(current_state, grid_size):
    position, velocity = current_state
    i_max, j_max = grid_size
    next_position = (position[0] + velocity[0]) % i_max, (position[1] + velocity[1]) % j_max
    return next_position, velocity

def simulate_robots_and_calculate_safety_factor(robot_states, grid_size, steps):
    quadrants = {i: 0 for i in range(4)}
    i_max, j_max = grid_size

    for robot_state in robot_states:
        for _ in range(steps):
            robot_state = simulate_robot_step(robot_state, grid_size)
        robot_pos_i, robot_pos_j = robot_state[0]

        if robot_pos_i < i_max // 2:
            if robot_pos_j < j_max // 2:
                quadrants[0] += 1
            elif robot_pos_j > j_max // 2:
                quadrants[3] += 1
        elif robot_pos_i > i_max // 2:
            if robot_pos_j < j_max // 2:
                quadrants[1] += 1
            elif robot_pos_j > j_max // 2:
                quadrants[2] += 1

    from math import prod
    return prod(quadrants.values())

if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        in_text = fh.read()

    robots = parse_input(in_text)
    grid_size = (101, 103)
    steps = 100
    result = simulate_robots_and_calculate_safety_factor(robots, grid_size, steps)
    print(result)
