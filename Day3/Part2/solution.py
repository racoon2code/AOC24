import re

result = 0 

with open("input.txt", "r") as file:
    input_data = file.read()

mul_pattern = r"mul\((\d+),(\d+)\)"  
do_pattern = r"do\(\)"               
dont_pattern = r"don't\(\)"          


is_enabled = True


for match in re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_data):
    instruction = match.group(0)  

    if instruction == "do()":
        is_enabled = True 
    elif instruction == "don't()":
        is_enabled = False  
    else: 
        if is_enabled:  
            x, y = map(int, re.findall(r"\d+", instruction))
            result += x * y

print(result)
