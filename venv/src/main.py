# Import PuLP modeler functions
from pulp import *
import src.datapost.print_solution as ps
import src.model.initialize_model as mod
import src.model.add_goal as go
import src.model.add_constraints as cons
import src.dataprep.setup_sudoku as ss


Vals, Rows, Cols, Boxes = ss.init_sudoku()

prob_init, choices = mod.init_model(Vals=Vals, Rows=Rows, Cols=Cols)

prob_w_obj = go.objective_function(prob=prob_init)

prob_cons = cons.add_general_constraints(Rows=Rows, Cols=Cols, Vals=Vals, Boxes=Boxes, choices=choices, prob=prob_w_obj)

prob_start = cons.add_starting_constraints(prob=prob_cons, choices=choices)


# The problem data is written to an .lp file
prob_start.writeLP("Sudoku.lp")

# The problem is solved using PuLP's choice of Solver
prob_start.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob_start.status])

# The solution is written to the sudokuout.txt file
ps.print_sol(Rows=Rows, Cols=Cols, Vals=Vals, choices=choices)

# The location of the solution is give to the user
print("Solution Written to sudokuout.txt")
