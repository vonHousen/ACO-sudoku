
import numpy as np
import math
import copy


class Sudoku:
	"""
	Class representing classic Sudoku riddle.
	"""

	def __init__(self, board):
		"""
		Constructor of the Sudoku.
		:param board: board of digits Sudoku is made of, in the Numpy array format.
		"""
		self._board = copy.deepcopy(board)
		self._size = len(self.board)
		self._rank = int(math.sqrt(self.size))
		assert(self.rank ** 2 == self.size)

	@property
	def rank(self):
		"""
		Square root of the maximum number in the sudoku.
		"""
		return self._rank

	@property
	def size(self):
		"""
		Maximum number in the sudoku.
		"""
		return self._size

	@property
	def board(self):
		"""
		Board of digits sudoku is made of, in numpy format.
		access field simply by operators: board[y][x] <-> board[row_number][column_number]
		"""
		return self._board

	def __str__(self):
		vertical_line_sign = '|'
		horizontal_line_sign = '- '
		border_line = (self.size + 2 * self.rank) \
			* horizontal_line_sign + '\n'

		def generate_row(row_number):
			row = vertical_line_sign
			for l in range(self.rank):
				for m in range(self.rank):
					row += ' ' + str(self.board[row_number][self.rank * l + m]) + ' '
				row += vertical_line_sign

			row += '\n'
			return row

		to_print = border_line
		for i in range(self.rank):
			for j in range(self.rank):
				to_print += generate_row(self.rank * i + j)
			to_print += border_line

		return to_print


# TODO S would be an internal representation of a sudoku class
S3 = np.array([
	[1, 2, 3, 1, 2, 3, 1, 2, 3],
	[4, 5, 6, 4, 5, 6, 4, 5, 6],
	[7, 8, 9, 7, 8, 9, 7, 8, 9],
	[1, 2, 3, 1, 2, 3, 1, 2, 3],
	[4, 5, 6, 4, 5, 6, 4, 5, 6],
	[7, 8, 9, 7, 8, 9, 7, 8, 9],
	[1, 2, 3, 1, 2, 3, 1, 2, 3],
	[4, 5, 6, 4, 5, 6, 4, 5, 6],
	[7, 8, 9, 7, 8, 9, 7, 8, 9]
])

S2 = np.array([
	[1, 2, 3, 4],
	[3, 4, 1, 2],
	[2, 1, 4, 3],
	[4, 3, 2, 1],
])


if __name__ == "__main__":
	sudoku_test = Sudoku(S2)
	print()
	print('Sudoku from dummy matrix:')
	print(sudoku_test)
