""" Solve a nonogram of the form:
{
    "cols": [[3],[1,1],[1,1],[1,1],[3]],
    "rows": [[3],[1,1],[1,1],[1,1],[3]],
    "solution": []
}
"""

import pyeda.inter as pe

def generate_possible_line(line, variables, size):

    slack = size - sum(line)- line.count(0)

    if slack <= 0:

        return [line]

    slack_positions = [0]

    current_sum = 0
    for i in line:
        if i != 0:
            current_sum += i
            slack_positions.append(current_sum)

    answers = []


    for i in slack_positions:
        newline = line[:]
        newline.insert(i, 0)
        answers.extend(generate_possible_line(newline, variables, size))

    return answers


def process_line(line, variables, size):

    """ Converts line to bit string and assigns variables
    
        ex. [0, 3, 0] => [0, 1, 1, 1, 0] => [~x1, x2, x3, x4, ~x5]
    
     """

    lines = generate_possible_line(line, variables, size)

    # print("lines" + str(lines))

    processed_lines = []

    for line in lines:

        # Expand the line
        a = []
        for i in line:
            if i==0:
                a.append(0)
            else:
                for _ in range(i):
                    a.append(1)


        processed_lines.append(a)

    equations = []

    for line in processed_lines:
        used_variables = [pe.And(variables[n]) if i==1 else pe.Not( variables[n]) for n, i in enumerate(line)]
        equation = pe.And(*used_variables)
        equations.append(equation)

    eqs = pe.Or(*equations)
    return [eqs]



def run_sat():
    pass

def solve_nonogram(nonogram):
    # Main solver


    """
    for every row
        get all possibilities of row
        convert to sat problem


    for every column
        get all possibilities for column
        convert to sat problem


    solve sat problem"""


    sizex = len(nonogram["cols"])
    sizey = len(nonogram["rows"])


    # Create variables

    variables = []

    for i in range(sizex):
        row = []
        for j in range(sizey):
            variable = pe.exprvar("V" +str(i)+str(j))
            row.append(variable)
        variables.append(row)

    # print(variables)

    big_equation_list = []

    # Iterate through rows
    for n, i in enumerate(nonogram["rows"]):
        row_variables = variables[n]
        eqn = process_line(i, row_variables, sizex)
        big_equation_list.extend(eqn)

    # Iterate through columns
    for n, i in enumerate(nonogram["cols"]):
        column_variables = [a[n] for a in variables]
        eqn = process_line(i, column_variables, sizey)
        big_equation_list.extend(eqn)


    full_eq = pe.And(*big_equation_list)

    answer = full_eq.satisfy_one()

    result = {"cols": nonogram["cols"], "rows":nonogram["rows"], "solution": answer}
    return result

    












if __name__ == "__main__":

    nonogram = {\
    "cols": [[3],[1,1],[1,1],[1,1],[3]],\
    "rows": [[3],[1,1],[1,1],[1,1],[3]],\
    "solution": []\
    }

    print(solve_nonogram(nonogram))
