from sympy.abc import x, y
from sympy import reduce_inequalities

def process_text(text: str) -> str:
    
    return text

def process_solution(solution) -> str:
    solution = solution.split("&")
    if "oo" in solution[0]:
        solution = solution[1]
    else:
        solution = solution[0]
    return solution.replace(" ", "")[1:-1]

def solve(text: str) -> str:
    text = process_text(text)
    if "y" in text:
        solution = reduce_inequalities(text, [x])
    solution = reduce_inequalities(text, [])
    return process_solution(str(solution))

if __name__ == "__main__":
    print(solve("2*x<3"))