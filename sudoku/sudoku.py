

class Sudoku:   # TODO
    pass


# TODO S would be an internal representation of a sudoku class
S = [[1, 2, 3, 1, 2, 3, 1, 2, 3],
     [4, 5, 6, 4, 5, 6, 4, 5, 6],
     [7, 8, 9, 7, 8, 9, 7, 8, 9],
     [1, 2, 3, 1, 2, 3, 1, 2, 3],
     [4, 5, 6, 4, 5, 6, 4, 5, 6],
     [7, 8, 9, 7, 8, 9, 7, 8, 9],
     [1, 2, 3, 1, 2, 3, 1, 2, 3],
     [4, 5, 6, 4, 5, 6, 4, 5, 6],
     [7, 8, 9, 7, 8, 9, 7, 8, 9]]


def print_from_matrix(matrix):      # TODO made it method in Sudoku class
    """
    Prints sudoku from given matrix of dimensions: 9x9.
    Matrix represented by: list of lists.
    """
    assert len(matrix) == 9             # assert that given matrix is of right dimensions
    for i in range(9):
        assert len(matrix[i]) == 9

    vertical_line_sign = '|'
    horizontal_line_sign = '-'
    border_line = 31 * horizontal_line_sign

    def print_row(matrix_inner, row_number):
        row = vertical_line_sign
        for l in range(3):
            for m in range(3):
                row += ' ' + str(matrix_inner[row_number][3*l+m]) + ' '
            row += vertical_line_sign
        print(row)

    print(border_line)
    for i in range(3):
        for j in range(3):
            print_row(matrix, 3*i+j)
        print(border_line)


if __name__ == "__main__":
    print()
    print('Sudoku from dummy matrix:')
    print_from_matrix(S)
