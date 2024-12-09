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
    current_file_id = layout[0]
    block_start_idx = 0
    file_blocks = {}

    for i, block in enumerate(layout):
        if block != current_file_id or i == len(layout) - 1:
            if current_file_id in file_blocks:
                file_blocks[current_file_id].append(
                    (block_start_idx, i - 1 if block != current_file_id else i)
                )
            else:
                file_blocks[current_file_id] = [(block_start_idx, i - 1 if block != current_file_id else i)]
            block_start_idx = i
            current_file_id = block

    empty_blocks = file_blocks.pop(-1, [])
    for file_id, positions in reversed(file_blocks.items()):
        start_idx, end_idx = positions[0]
        file_size = end_idx - start_idx + 1
        for i, (s, e) in enumerate(empty_blocks):
            empty_space_size = e - s + 1
            if s <= start_idx and empty_space_size >= file_size:
                layout[s:s + file_size] = [file_id] * file_size
                layout[start_idx:end_idx + 1] = [-1] * file_size
                if empty_space_size > file_size:
                    empty_blocks[i] = (s + file_size, e)
                else:
                    empty_blocks.pop(i)
                break

    return layout

def get_checksum(layout: list[int]) -> int:
    return sum(block * i for i, block in enumerate(layout) if block != -1)

if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        in_text = fh.read()

    disk_layout = parse_input(in_text)

    
    result = get_checksum(defragment_disk(disk_layout))
   

    print(result)
