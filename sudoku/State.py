
from sudoku.Sudoku import *


class State:
	"""
	State defined as a fully filled Sudoku board.
	"""
	def __init__(self, sudoku):
		"""
		A constructor.
		:param sudoku:	Sudoku object which is connected with current state.
		"""
		self._sudoku = Sudoku(sudoku.board)