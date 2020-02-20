def print_sol(Rows, Cols, Vals, choices):
    sudokuout = open("out/sudokuout.txt", "wt")
    for r in Rows:
        if r == "1" or r == "4" or r == "7":
            sudokuout.write("+-------+-------+-------+\n")
        for c in Cols:
            for v in Vals:
                if choices[v][r][c].value() == 1:

                    if c == "1" or c == "4" or c == "7":
                        sudokuout.write("| ")

                    sudokuout.write(v + " ")

                    if c == "9":
                        sudokuout.write("|\n")
    sudokuout.write("+-------+-------+-------+")
    sudokuout.close()
    return None