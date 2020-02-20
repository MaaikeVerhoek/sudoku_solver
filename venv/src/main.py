import src.dataprep.setup_sudoku as ss
import src.model.initialize_model as mod
import src.model.add_goal as go
import src.model.add_constraints as cons
import src.model.solve as so
import src.datapost.print_solution as ps


Vals, Rows, Cols, Boxes = ss.init_sudoku()

prob_init, choices = mod.init_model(Vals=Vals, Rows=Rows, Cols=Cols)

prob_w_obj = go.objective_function(prob=prob_init)

prob_cons = cons.add_general_constraints(Rows=Rows, Cols=Cols, Vals=Vals, Boxes=Boxes, choices=choices, prob=prob_w_obj)

prob_start = cons.add_starting_constraints(prob=prob_cons, choices=choices)

prob_solved = so.solve_sudoku(prob=prob_start)

# The solution is written to the sudokuout.txt file
ps.print_sol(Rows=Rows, Cols=Cols, Vals=Vals, choices=choices)

# The location of the solution is give to the user
print("Solution Written to sudokuout.txt")
