from sympy import reduce_inequalities
from sympy.abc import x


def is_digit(text: str) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False

def process_text(text: str) -> str:
    if len(text) > 0:
        i: int = 1
        while i < len(text):
            if (text[i] == "(" or text[i] == "x") and (is_digit(text[i-1]) or text[i-1] == ")"):
                text = f"{text[:i]}*{text[i:]}"
            i += 1
    return text


def process_solution(solution: str) -> str:
    solution: str = solution.split("&")
    if "oo" in solution[0]:
        solution : str = solution[1]
    else:
        solution : str = solution[0]
    return solution.replace(" ", "")[1:-1]


def solve(text: str) -> str:
    text: str = process_text(text)
    if "y" in text:
        solution : str = reduce_inequalities(text, [x])
    solution : str = reduce_inequalities(text, [])
    return process_solution(str(solution))
