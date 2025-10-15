from random import seed, randint, choice
from solverz3 import parse_puzzle_to_z3, generic_solver

def generate_generic_puzzle(n: int):
    """Returns a satisfiable generic Knights and Knaives puzzle with n people.""" #unicode \u0085 for Next Line

    puzzle_text = 'Em uma ilha vivem apenas cavaleiros e patifes.' + '\n' + 'Cavaleiros sempre dizem a verdade, e patifes sempre mentem.' + '\n'
    seed()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(1, n+1):
        current_person = alphabet[i-1]
        random_p1 = alphabet[randint(0, n-1)]
        random_p2 = alphabet[randint(0, n-1)]

        while random_p1 == current_person:
            random_p1 = alphabet[randint(0, n-1)]
        while random_p2 == current_person or random_p2 == random_p1:
            random_p2 = alphabet[randint(0, n-1)]

        line = f'{current_person} diz:' + choice([f"'{random_p1} é um cavaleiro.'\n",
                                     f"'{random_p1} é um patife.'\n",
                                     f"'{random_p1} e eu somos diferentes.'\n",
                                     f"'{random_p1} e eu somos iguais.'\n",
                                     f"'{random_p1} e {random_p2} são iguais.'\n",
                                     f"'{random_p1} e {random_p2} são diferentes.'\n"])
        puzzle_text += line
 
    variables, restrictions = parse_puzzle_to_z3(puzzle_text)
    if generic_solver(variables, restrictions) in ["Inconsistente (sem solução)", "Indefinido (solver não conseguiu decidir)"]:
        return generate_generic_puzzle(n)
    return puzzle_text + 'Quem é cavaleiro e quem é patife?\n'


def save_to_txt_file():
    pass

def main():
    puzzle = generate_generic_puzzle(3)
    print(puzzle)
    variables, restrictions = parse_puzzle_to_z3(puzzle)
    resultado_z3 = generic_solver(variables, restrictions)
    print("Resposta correta (Z3 real)\n")
    if isinstance(resultado_z3, dict):
        for p, v in resultado_z3.items():
            print(f"{p}: {'Cavaleiro' if v else 'Patife'}")
    else:
        print(resultado_z3)


if __name__ == '__main__':
    main()
    