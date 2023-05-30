from abc import ABC, abstractmethod
from typing import List


def is_digit(text: str) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False
    
def is_operator(text: str) -> bool:
    return text == "+" or text == "-" or text == "/" or text == "*"



class SolvingComponent(ABC):
    
    @abstractmethod
    def to_string():
        raise NotImplementedError

class Inequation(SolvingComponent):
    def __init__(self, type: str, left: SolvingComponent, right: SolvingComponent) -> None:
        super().__init__()
        self.type = type
        self.left = left
        self.right = right

    def develop(self):
        return self
    
    def simplify(self):
        return self
    
    def isolate(self):
        return self

    def to_string(self):
        return f"{self.left.to_string()}{self.type}{self.right.to_string()}"

class Priority(SolvingComponent):
    def __init__(self, inside: SolvingComponent) -> None:
        super().__init__()
        self.inside = inside

    def to_string(self):
        return f"({self.inside.to_string()})"

class Operator(SolvingComponent):
    def __init__(self, operator: str, left: SolvingComponent, right: SolvingComponent) -> None:
        super().__init__()
        self.operator = operator
        self.left = left
        self.right = right

    def to_string(self):
        return f"{self.left.to_string()}{self.operator}{self.right.to_string()}"

class X(SolvingComponent):
    def __init__(self) -> None:
        super().__init__()
        
    def to_string():
        return "x"
    
class Digit(SolvingComponent):
    def __init__(self, digit: float) -> None:
        super().__init__()
        self.digit = digit

    def to_string(self):
        return f"{self.digit}"

def solve(text: str)->float:
    exploded = explode(text)
    solving_tree = form_tree(exploded)
    solving_tree = solving_tree.develop()
    solving_tree = solving_tree.simplify()
    solving_tree = solving_tree.isolate()
    return solving_tree.to_string()

def explode(text: str) -> List[str]:
    exploded = []
    i = 0
    while i < len(text):
        if text[i] == "(" or text[i] == ")" or text[i] == "+" or text[i] == "-" or text[i] == "/" or text[i] == "*" or text[i] == "x":
            exploded.append(text[i])
        elif is_digit(text[i]):
            nbr = f"{text[i]}"
            i += 1
            while i < len(text) and is_digit(text[i]):
                nbr = f"{nbr}{text[i]}"
                i += 1
            i -= 1
            exploded.append(nbr)
        elif text[i] == "<" or text[i] == ">":
            if text[i+1] == "=":
                exploded.append(f"{text[i]}{text[i+1]}")
                i += 1
            else:
                exploded.append(f"{text[i]}")
        i += 1
    return exploded


def form_tree(exploded) -> Inequation:
    for i in range(len(exploded)):
        if exploded[i][0] == ">" or exploded[i][0] == "<":
            return Inequation(exploded[i], form_component(exploded[:i-1]), form_component(exploded[i+1:]))
    raise SyntaxError


def form_component(exploded) -> SolvingComponent:
    # FORM PRIORITY
    # FORM OPERATOR
    return Digit(9632.432)

if __name__ == "__main__":
    print(solve("23*x+4*2<=365"))