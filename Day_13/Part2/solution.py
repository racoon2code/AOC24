import math
import re
from sympy import And
from sympy.abc import x, y
from sympy.solvers.diophantine.diophantine import diop_linear
from sympy.solvers.inequalities import reduce_rational_inequalities

def parse_input(text: str) -> list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    out = []
    for block in text.strip().split("\n\n"):
        a_shift = tuple(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", block)[0]))
        b_shift = tuple(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", block)[0]))
        target = tuple(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", block)[0]))
        out.append((a_shift, b_shift, target))


    return out

def solve_diophantine_equation(a: int, b: int, c: int) -> int:
    sol = diop_linear(a * x + b * y - c)
    k = sol.free_symbols.pop()
    k_range_x = reduce_rational_inequalities([[sol[0] >= 0]], k)
    k_range_y = reduce_rational_inequalities([[sol[1] >= 0]], k)
    valid_k_values = And(k_range_y, k_range_x).as_set()
    if valid_k_values.is_empty:
        return 0
    candidates = [sol.subs({k: i}) for i in range(valid_k_values.left, valid_k_values.right + 1)]
    n_a, n_b = min(candidates, key=lambda z: 3 * z[0] + z[1])

    return 3 * n_a + n_b

def solve_claw_and_get_game_cost(
        a_shift: tuple[int, int],
        b_shift: tuple[int, int],
        target: tuple[int, int]
) -> int:
    a_x, a_y = a_shift
    b_x, b_y = b_shift
    t_x, t_y = target

    try:
        n_a = (t_x * b_y - b_x * t_y) / (a_x * b_y - b_x * a_y)
    except ZeroDivisionError:
        if a_x * t_y - a_y * t_x == 0:
            a_shift_len = math.sqrt(a_x ** 2 + a_y ** 2)
            b_shift_len = math.sqrt(b_x ** 2 + b_y ** 2)
            target_len = math.sqrt(t_x ** 2 + t_y ** 2)
            if a_shift_len.is_integer() and b_shift_len.is_integer() and target_len.is_integer():
                return solve_diophantine_equation(int(a_shift_len), int(b_shift_len), int(target_len))
        return 0

    if n_a < 0 or not n_a.is_integer():
        return 0
    n_a = int(n_a)

    try:
        n_b = (t_x - a_x * n_a) / b_x
    except ZeroDivisionError:
        n_b = (t_y - a_y * n_a) / b_y

    if n_b < 0 or not n_b.is_integer():
        return 0
    n_b = int(n_b)

    return 3 * n_a + n_b

def get_total_game_costs(
        claws: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]
) -> int:
    return sum(
        solve_claw_and_get_game_cost(a_shift, b_shift, target)
        for a_shift, b_shift, target in claws
    )

def correct_unit_conversion(
        claws: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]
) -> list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    return [
        (a_shift, b_shift, (target[0] + 10000000000000, target[1] + 10000000000000))
        for a_shift, b_shift, target in claws
    ]

if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        in_text = fh.read()

    claw_machines = parse_input(in_text)

    # PART 2
    result = get_total_game_costs(correct_unit_conversion(claw_machines))
    print(result)
