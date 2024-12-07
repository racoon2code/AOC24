from itertools import product

def parse_equations(file_path):
    equations = []
    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()  
            if not line or ":" not in line:  
                continue
            try:
                test_value, numbers = line.split(":")
                test_value = int(test_value.strip())
                numbers = list(map(int, numbers.strip().split()))
                equations.append((test_value, numbers))
            except ValueError as e:
                print(f"Fehler beim Parsen von Zeile {line_number}: {e}")
    return equations

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        elif op == "||":
            result = int(str(result) + str(numbers[i + 1]))
    return result

def find_valid_equations(equations):
    total = 0
    for test_value, numbers in equations:
        n = len(numbers) - 1  
        valid = False
        for ops in product(["+", "*", "||"], repeat=n):
            result = evaluate_expression(numbers, ops)
            if result == test_value:
                total += test_value
                valid = True
                break
    return total

file_path = "C:\dev\AOC24\Day7\Part2\input.txt"


equations = parse_equations(file_path)
calibration_result = find_valid_equations(equations)
print(f"Ergebnis: {calibration_result}")

