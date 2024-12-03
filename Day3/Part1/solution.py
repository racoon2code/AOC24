import re

result = 0

with open("input.txt", "r") as file:
    input = file.read()


find_mul = r"mul\(\d+,\d+\)"
find_int = r"\d+"



input = re.findall(find_mul, input)

for pair in input:
    i = re.findall(find_int, pair)
    
    result += int(i[0]) * int(i[1])

print(result)
