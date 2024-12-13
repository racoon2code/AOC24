from itertools import product
import math

def read_input(file):
    """Liest die Eingabe aus der Datei"""
    machines = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4):
            a_line = lines[i].strip().split(', ')
            b_line = lines[i+1].strip().split(', ')
            prize_line = lines[i+2].strip().split(', ')

            a_x, a_y = map(int, (a_line[0].split('+')[1], a_line[1].split('+')[1]))
            b_x, b_y = map(int, (b_line[0].split('+')[1], b_line[1].split('+')[1]))
            prize_x, prize_y = map(int, (prize_line[0].split('=')[1], prize_line[1].split('=')[1]))

            machines.append(((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))
    return machines

def gcd(a, b):
    """Greatest common divisor"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least common multiple"""
    return abs(a * b) // gcd(a, b)

def solve_machine(a, b, prize, max_presses=100):
    """Berechnet die minimale Anzahl an Token für eine Maschine"""
    a_x, a_y = a
    b_x, b_y = b
    prize_x, prize_y = prize

    # Bounds based on maximum presses
    min_cost = math.inf
    solution = None

    for a_count, b_count in product(range(max_presses + 1), repeat=2):
        x_movement = a_count * a_x + b_count * b_x
        y_movement = a_count * a_y + b_count * b_y

        if x_movement == prize_x and y_movement == prize_y:
            cost = a_count * 3 + b_count * 1
            if cost < min_cost:
                min_cost = cost
                solution = (a_count, b_count)

    return min_cost if solution else None

def main():
    machines = read_input('input.txt')
    total_cost = 0
    prizes_won = 0

    for machine in machines:
        a, b, prize = machine
        cost = solve_machine(a, b, prize)
        if cost is not None:
            prizes_won += 1
            total_cost += cost

    print(f"Prizes won: {prizes_won}")
    print(f"Total cost: {total_cost}")

if __name__ == "__main__":
    main()
