def init_sudoku():
    # A list of strings from "1" to "9" is created
    Sequence = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # The Vals, Rows and Cols sequences all follow this form
    Vals = Sequence
    Rows = Sequence
    Cols = Sequence

    # The boxes list is created, with the row and column index of each square in each box
    Boxes = []
    for i in range(3):
        for j in range(3):
            Boxes += [[(Rows[3 * i + k], Cols[3 * j + l]) for k in range(3) for l in range(3)]]

    return Vals, Rows, Cols, Boxes

