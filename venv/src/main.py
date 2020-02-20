# Import PuLP modeler functions
from pulp import *
import src.datapost.print_solution as ps
import src.model.add_constraints as cons

# A list of strings from "1" to "9" is created
Sequence = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# The Vals, Rows and Cols sequences all follow this form
Vals = Sequence
Rows = Sequence
Cols = Sequence

# The boxes list is created, with the row and column index of each square in each box
Boxes =[]
for i in range(3):
    for j in range(3):
        Boxes += [[(Rows[3*i+k],Cols[3*j+l]) for k in range(3) for l in range(3)]]



# The prob variable is created to contain the problem data
prob = LpProblem("SudokuProblem",LpMinimize)

# The problem variables are created
choices = LpVariable.dicts("Choice",(Vals,Rows,Cols),0,1,LpInteger)

# The arbitrary objective function is added
prob += 0, "Arbitrary Objective Function"

prob = cons.add_general_constraints(Rows=Rows, Cols=Cols, Vals=Vals, Boxes=Boxes, choices=choices, prob=prob)


prob = cons.add_starting_constraints(prob=prob, choices=choices)


# The problem data is written to an .lp file
prob.writeLP("Sudoku.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# The solution is written to the sudokuout.txt file
ps.print_sol(Rows=Rows, Cols=Cols, Vals=Vals, choices=choices)

# The location of the solution is give to the user
print("Solution Written to sudokuout.txt")
