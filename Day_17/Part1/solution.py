def run_program(registers, program):
    A, B, C = registers

    instruction_pointer = 0
    output = []

    def get_combo_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            raise ValueError("Invalid combo operand")

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        instruction_pointer += 2  

        if opcode == 0: 
            denom = 2 ** get_combo_value(operand)
            A //= denom
        elif opcode == 1:  
            B ^= operand
        elif opcode == 2:  
            B = get_combo_value(operand) % 8
        elif opcode == 3:  
            if A != 0:
                instruction_pointer = operand
        elif opcode == 4:  
            B ^= C
        elif opcode == 5:  
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:  
            denom = 2 ** get_combo_value(operand)
            B = A // denom
        elif opcode == 7:  
            denom = 2 ** get_combo_value(operand)
            C = A // denom
        else:
            raise ValueError("Invalid opcode")

    return ",".join(map(str, output))

with open("input.txt", "r") as file:
    lines = file.readlines()

initial_registers = [
    int(lines[0].split(":")[1].strip()),
    int(lines[1].split(":")[1].strip()),
    int(lines[2].split(":")[1].strip())
]
program = list(map(int, lines[4].split(":")[1].strip().split(",")))

result = run_program(initial_registers, program)
print("Output:", result)
