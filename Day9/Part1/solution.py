def parse_input(text: str) -> list[int]:
    layout = []
    file_id = 0
    for i, block_size_str in enumerate(text.strip()):
        block_size = int(block_size_str)
        if i % 2 == 0:
            layout.extend([file_id] * block_size)
            file_id += 1
        else:
            layout.extend([-1] * block_size)
    return layout

def defragment_disk(layout: list[int]) -> list[int]:
    layout = layout.copy()
    occupied_disk_size = len(layout) - layout.count(-1)
    free_space_idcs = [i for i, block in enumerate(layout) if block == -1 and i < occupied_disk_size]

    for i, block in enumerate(layout[::-1]):
        idx = len(layout) - i - 1
        if free_space_idcs and block != -1:
            layout[free_space_idcs.pop(0)] = block
            layout[idx] = -1

    return layout

def get_checksum(layout: list[int]) -> int:
    return sum(block * i for i, block in enumerate(layout) if block != -1)

if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        in_text = fh.read()

    disk_layout = parse_input(in_text)

    result = get_checksum(defragment_disk(disk_layout))
    
    print(result)
