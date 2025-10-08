import re
from z3 import * 

def generic_solver(variables, restrictions):
    """
    variables: dict with name -> Z3 type (e.g., {'A': Bool('A'), 'B': Bool('B')})
    restrictions: list of Z3 expressions (BoolRef)
    """
    solver = Solver()
    for r in restrictions:
        solver.add(r)

    if solver.check() == sat:
        model = solver.model()
        return {name: model[var] for name, var in variables.items()}
    elif solver.check() == unsat:
        return "Inconsistente (sem solução)"
    else:
        return "Indefinido (solver não conseguiu decidir)"
    

def parse_puzzle_to_z3(puzzle_text):
    """
    Interprets simple Knights and Knaves puzzles (A, B, C, ...) and generates variables and restrictions.
    It is generic for up to 3 characters. Returns (variables, restrictions).
    """
    # Extract possible characters (A, B, C, D, ...)
    names = re.findall(r"\b([A-Z])\s+diz:", puzzle_text)
    names = sorted(set(names))
    if not names:
        raise ValueError("Nenhum personagem encontrado no texto do puzzle.")

    # Creates boolean variables: True = knight, False = scoundrel
    variables = {n: Bool(n) for n in names}
    restrictions = []

    # Simple pattern-based parser
    for n in names:
        if f"{n} diz" not in puzzle_text:
            continue

        fala = puzzle_text.split(f"{n} diz:")[-1].split("'")[1]  # take what is in quotes

        # Example 1: "B é um patife."
        if "é um patife" in fala:
            ref = fala.strip()[0]  # fist letter (ex: B)
            if ref in variables:
                restr = variables[n] == Not(variables[ref])  # If A is knight, then B is Knaves 
                restrictions.append(restr)

        # Exemple 2: "A e eu somos diferentes."
        elif "somos diferentes" in fala:
            ref = fala.strip()[0]
            if ref in variables:
                restr = variables[n] == (variables[n] != variables[ref])
                restrictions.append(restr)

        # Exemple 3: "A e eu somos iguais."
        elif "somos iguais" in fala:
            ref = fala.strip()[0]
            if ref in variables:
                restr = variables[n] == (variables[n] == variables[ref])
                restrictions.append(restr)

    if not restrictions:
        raise ValueError("Nenhuma restrição reconhecida no puzzle. Verifique o formato.")

    return variables, restrictions