
from sudoku.Sudoku import *
import random


class State:
	"""
	State defined as a fully filled Sudoku board.
	"""

	def __init__(self, sudoku):
		"""
		A constructor.
		:param sudoku:	Sudoku object which is connected with current state.
		"""
		self._sudoku = Sudoku(sudoku.board, sudoku.hardcoded_digits)

	@property
	def sudoku(self):
		return self._sudoku

	def change_randomly(self):
		"""
		Makes a move on the G graph.
		In another words: ant modifies its State by changing single digit in the sudoku.
		Random position may
		"""
		position = random.choice(self.sudoku.editable_positions)
		old_digit = self.sudoku.board[position[0]][position[1]]
		digit = old_digit
		while old_digit == digit:
			digit = np.random.randint(low=1, high=self.sudoku.size, size=1)
		self.sudoku.update_digit(position_to_edit=position, new_digit=digit)


if __name__ == "__main__":
	S = np.array([
		[1, 2, 3, 4],
		[3, 4, 1, 2],
		[2, 1, 4, 3],
		[4, 3, 2, 1],
	])
	S_hardcoded = np.array([
		[True, False, True, True],
		[True, True, True, True],
		[True, True, True, True],
		[True, True, False, True]
	])
	sudoku_test = Sudoku(S, S_hardcoded)
	state_test = State(sudoku_test)
	print(state_test.sudoku)
	state_test.change_randomly()
	print(state_test.sudoku)

