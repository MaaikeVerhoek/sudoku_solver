from pulp import *
def add_general_constraints(Rows, Cols, Vals, Boxes, choices, prob):
    # A constraint ensuring that only one value can be in each square is created
    for r in Rows:
        for c in Cols:
            prob += lpSum([choices[v][r][c] for v in Vals]) == 1, ""

    # The row, column and box constraints are added for each value
    for v in Vals:
        for r in Rows:
            prob += lpSum([choices[v][r][c] for c in Cols]) == 1, ""

        for c in Cols:
            prob += lpSum([choices[v][r][c] for r in Rows]) == 1, ""

        for b in Boxes:
            prob += lpSum([choices[v][r][c] for (r, c) in b]) == 1, ""
    return prob

def add_starting_constraints(prob, choices):
    # The starting numbers are entered as constraints
    prob += choices["5"]["1"]["1"] == 1, ""
    prob += choices["6"]["2"]["1"] == 1, ""
    prob += choices["8"]["4"]["1"] == 1, ""
    prob += choices["4"]["5"]["1"] == 1, ""
    prob += choices["7"]["6"]["1"] == 1, ""
    prob += choices["3"]["1"]["2"] == 1, ""
    prob += choices["9"]["3"]["2"] == 1, ""
    prob += choices["6"]["7"]["2"] == 1, ""
    prob += choices["8"]["3"]["3"] == 1, ""
    prob += choices["1"]["2"]["4"] == 1, ""
    prob += choices["8"]["5"]["4"] == 1, ""
    prob += choices["4"]["8"]["4"] == 1, ""
    prob += choices["7"]["1"]["5"] == 1, ""
    prob += choices["9"]["2"]["5"] == 1, ""
    prob += choices["6"]["4"]["5"] == 1, ""
    prob += choices["2"]["6"]["5"] == 1, ""
    prob += choices["1"]["8"]["5"] == 1, ""
    prob += choices["8"]["9"]["5"] == 1, ""
    prob += choices["5"]["2"]["6"] == 1, ""
    prob += choices["3"]["5"]["6"] == 1, ""
    prob += choices["9"]["8"]["6"] == 1, ""
    prob += choices["2"]["7"]["7"] == 1, ""
    prob += choices["6"]["3"]["8"] == 1, ""
    prob += choices["8"]["7"]["8"] == 1, ""
    prob += choices["7"]["9"]["8"] == 1, ""
    prob += choices["3"]["4"]["9"] == 1, ""
    prob += choices["1"]["5"]["9"] == 1, ""
    prob += choices["6"]["6"]["9"] == 1, ""
    prob += choices["5"]["8"]["9"] == 1, ""
    return prob