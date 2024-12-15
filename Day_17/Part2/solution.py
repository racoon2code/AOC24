import re

def parse_input(text: str) -> tuple[list[int], list[int]]:
    registers = []
    for register in ("A", "B", "C"):
        registers.append(int(re.findall(rf"Register {register}: (\d+)", text)[0]))
    instructions = list(map(int, re.findall(r"Program: ((?:\d,)+\d)$", text)[0].split(",")))
    return registers, instructions

class Program:
    def __init__(self, registers: list[int], instructions: list[int]):
        self.registers = registers.copy()
        self.instructions = instructions
        self.pointer = 0
        self.opcodes = [
            lambda x: self.adv(x),
            lambda x: self.bxl(x),
            lambda x: self.bst(x),
            lambda x: self.jnz(x),
            lambda x: self.bxc(x),
            lambda x: self.out(x),
            lambda x: self.bdv(x),
            lambda x: self.cvd(x),
        ]
        self.output = []

    def combo(self, x: int) -> int:
        if x <= 3:
            return x
        else:
            return self.registers[x - 4]

    def adv(self, x: int):
        self.registers[0] = self.registers[0] >> self.combo(x)
        return 2

    def bxl(self, x: int):
        self.registers[1] = self.registers[1] ^ x
        return 2

    def bst(self, x: int):
        self.registers[1] = self.combo(x) % 8
        return 2

    def jnz(self, x: int):
        if self.registers[0] != 0:
            self.pointer = x
            return 0
        else:
            return 2

    def bxc(self, _: int):
        self.registers[1] = self.registers[1] ^ self.registers[2]
        return 2

    def out(self, x: int):
        self.output.append(self.combo(x) % 8)
        return 2

    def bdv(self, x: int):
        self.registers[1] = self.registers[0] >> self.combo(x)
        return 2

    def cvd(self, x: int):
        self.registers[2] = self.registers[0] >> self.combo(x)
        return 2

    def run(self):
        while self.pointer < len(self.instructions):
            opcode = self.instructions[self.pointer]
            arg = self.instructions[self.pointer + 1]
            pointer_increase = self.opcodes[opcode](arg)
            self.pointer += pointer_increase
        return self.output

def find_correct_register_a_value(registers: list[int], instructions: list[int]) -> int:
    possible_a_values = {-1: [0]}
    l = len(instructions)
    for i in range(l):
        for a_value in possible_a_values[i - 1]:
            for a in range(8):
                next_a_value = a_value * 8 + a
                registers[0] = next_a_value
                output = Program(registers, instructions).run()
                if output == instructions[-1 - i:]:
                    if i in possible_a_values.keys():
                        possible_a_values[i].append(next_a_value)
                    else:
                        possible_a_values[i] = [next_a_value]
    return min(possible_a_values[l - 1])

if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        in_text = fh.read()

    program = parse_input(in_text)

    result = find_correct_register_a_value(*program)
    print(result)
