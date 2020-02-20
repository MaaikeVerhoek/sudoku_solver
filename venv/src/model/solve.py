from pulp import *
def solve_sudoku(prob):
    # The problem data is written to an .lp file
    prob.writeLP("Sudoku.lp")
    # The problem is solved using PuLP's choice of Solver
    prob.solve()
    # The status of the solution is printed to the screen
    print("Status:", LpStatus[prob.status])
    return prob
    