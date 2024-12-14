import re
import numpy as np
import skimage

def parse_input(text: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    out = []
    for line in text.strip().split("\n"):
        position = tuple(map(int, re.findall(r"p=([\d,]+)", line)[0].split(",")))
        velocity = tuple(map(int, re.findall(r"v=([\d,\-]+)", line)[0].split(",")))
        out.append((position, velocity))

    return out

def simulate_robot_step(
        current_state: tuple[tuple[int, int], tuple[int, int]],
        grid_size: tuple[int, int]
) -> tuple[tuple[int, int], tuple[int, int]]:
    position, velocity = current_state
    i_max, j_max = grid_size
    next_position = (position[0] + velocity[0]) % i_max, (position[1] + velocity[1]) % j_max

    return next_position, velocity

def simulate_robots_and_find_num_steps_to_form_christmas_tree(
        robot_states: list[tuple[tuple[int, int], tuple[int, int]]],
        grid_size: tuple[int, int],
        steps: int
) -> int:
    min_entropy = np.inf
    best_image = None
    tree_found_after_steps = 0
    for n in range(steps):
        image = np.zeros(grid_size, dtype=int)
        for robot_state in robot_states:
            position, _ = robot_state
            image[position] += 1
        entropy = skimage.measure.shannon_entropy(image)
        if entropy < min_entropy:
            min_entropy = entropy
            best_image = image
            tree_found_after_steps = n
        robot_states = [simulate_robot_step(robot_state, grid_size) for robot_state in robot_states]

    return tree_found_after_steps


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        in_text = fh.read()

    robots = parse_input(in_text)

    result = simulate_robots_and_find_num_steps_to_form_christmas_tree(robots, (101, 103), 10000)
    print(result)
