from pulp import *
def init_model(Vals, Rows, Cols):
    # The prob variable is created to contain the problem data
    prob = LpProblem("SudokuProblem", LpMinimize)

    # The problem variables are created
    choices = LpVariable.dicts("Choice", (Vals, Rows, Cols), 0, 1, LpInteger)
    return prob, choices