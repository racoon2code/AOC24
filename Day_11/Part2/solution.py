from collections import Counter

def process_stones_optimized(stones):
    new_stones = Counter()
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(str(stone)) % 2 == 0: 
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            new_stones[left] += count
            new_stones[right] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones

def count_stones_after_blinks_optimized(input_file, blinks):
    with open(input_file, 'r') as f:
        initial_stones = list(map(int, f.read().strip().split()))


    stones = Counter(initial_stones)

    for _ in range(blinks):
        stones = process_stones_optimized(stones)

    return sum(stones.values())

if __name__ == "__main__":
    input_file = "input.txt"
    blinks = 75
    result = count_stones_after_blinks_optimized(input_file, blinks)
    print(result)
