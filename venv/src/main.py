# Import PuLP modeler functions
from pulp import *
import src.datapost.print_solution as ps
import src.model.initialize_model as mod
import src.model.add_goal as go
import src.model.add_constraints as cons
import src.dataprep.setup_sudoku as ss


Vals, Rows, Cols, Boxes = ss.init_sudoku()

prob, choices = mod.init_model(Vals=Vals, Rows=Rows, Cols=Cols)

prob = go.objective_function(prob=prob)

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
