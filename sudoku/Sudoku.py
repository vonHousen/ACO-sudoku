
import numpy as np
import math
import copy

ITERATIONS = 1000
N_ANTS = 10

class Sudoku:
	"""
	Class representing classic Sudoku riddle.
	"""

	def __init__(self, board, hardcoded_digits):
		"""
		Constructor of the Sudoku.
		:param board: board of digits Sudoku is made of, in the Numpy array format.
		:param hardcoded_digits: Numpy array of booleans, where Trues indicates which number is "hardcoded".
		"""
		self._board = copy.deepcopy(board)
		self._hardcoded_digits = copy.deepcopy(hardcoded_digits)
		self._size = len(self.board)
		self._rank = int(math.sqrt(self.size))
		assert(self.rank ** 2 == self.size)
		assert(len(self.board) == len(self.hardcoded_digits))
		self.Q = 1.0  # const from standard equation

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

	@property
	def hardcoded_digits(self):
		return self._hardcoded_digits

	@property
	def editable_positions(self):
		"""
		Returns a list of editable positions in sudoku.
		"""
		editables = []
		for row_number in range(self.size):
			for col_number in range(self.size):
				if not self.hardcoded_digits[row_number][col_number]:
					editables.append((row_number, col_number))

		return editables

	def update_digit(self, position_to_edit, new_digit):
		"""
		Updates digit on given position.
		"""
		if new_digit < 1 or new_digit > self.size:
			raise ValueError("Given new digit is incorrect.")
		elif position_to_edit in self.editable_positions:
			self._board[position_to_edit[0], position_to_edit[1]] = new_digit
		else:
			raise ValueError("Given position is incorrect.")

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


if __name__ == "__main__":
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
	S2_hardcoded = np.array([
		[True, False, True, True],
		[True, True, True, True],
		[True, True, True, True],
		[True, True, False, True]
	])
	sudoku_test = Sudoku(S2, S2_hardcoded)
	print()
	print('Sudoku from dummy matrix:')
	print(sudoku_test)
	print(sudoku_test.editable_positions)
	print()
	sudoku_test.update_digit((0, 1), 3)
	print(sudoku_test)
