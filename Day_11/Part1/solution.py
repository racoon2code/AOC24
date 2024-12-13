def split_number(num):
    num_str = str(num)
    mid = len(num_str) // 2
    left = int(num_str[:mid]) if num_str[:mid] else 0
    right = int(num_str[mid:]) if num_str[mid:] else 0
    return left, right

def process_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        left, right = split_number(stone)
        return [left, right]
    else:
        return [stone * 2024]

def simulate_blinks(initial_stones, blinks):
    stones = initial_stones[:]
    for _ in range(blinks):
        next_stones = []
        for stone in stones:
            next_stones.extend(process_stone(stone))
        stones = next_stones
    return len(stones)

def read_input(file_path):
    with open(file_path, 'r') as file:
        return list(map(int, file.readline().strip().split()))


input_file = "input.txt"
initial_stones = read_input(input_file)


blinks = 25


result = simulate_blinks(initial_stones, blinks)

print(result)