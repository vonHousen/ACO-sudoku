from collections import *
from sudoku.Sudoku import *
import random


class State:
	"""
	State defined as a fully filled Sudoku board.
	Thoroughly described in the documentation.
	"""

	def __init__(self, sudoku):
		"""
		A constructor.
		:param sudoku:	Sudoku object which is connected with current state.
		"""
		self._sudoku = Sudoku(sudoku.board, sudoku.hardcoded_digits)
		self._best_conflict_count = self.sudoku.size ** 2
		self._conflict_count = self.sudoku.size ** 2
		self._update_conflict_count()

	@property
	def sudoku(self):
		return self._sudoku

	def change_randomly(self):
		"""
		Makes a move on the G graph.
		In another words: ant modifies its State by changing single digit in the sudoku.
		Change is made randomly, when no pheromone trail was found by the Ant.
		"""
		position = random.choice(self.sudoku.editable_positions)
		old_digit = self.sudoku.board[position[0]][position[1]]
		digit = old_digit
		while old_digit == digit:
			digit = np.random.randint(low=1, high=self.sudoku.size, size=1)
		self.sudoku.update_digit(position_to_edit=position, new_digit=digit)

	def change_deliberately(self, position_to_edit, new_digit):
		"""
		Makes a move on the G graph.
		In another words: ant modifies its State by changing single digit in the sudoku.
		Change is made deliberately, when pheromone attracted the Ant.
		"""
		self.sudoku.update_digit(position_to_edit, new_digit)

	def _update_conflict_count(self):
		"""
		Counts conflict's count - f(state) function in documentation.
		Updates both _conflict_count & _best_conflict_count
		"""
		conflict_count = 0

		# initialise custom dictionary
		dict_count_for_digit = {}
		for digit in range(1, self.sudoku.size + 1):
			dict_count_for_digit[digit] = 0

		# iterate through rows
		for row_id in range(0, self.sudoku.size):

			# count digits in given row
			for col_id in range(0, self.sudoku.size):
				digit = self.sudoku.board[row_id][col_id]
				dict_count_for_digit[digit] += 1

			# count conflicts
			for digit_count in dict_count_for_digit.values():
				if digit_count > 1:
					conflict_count += 1

			# clear the digit counts
			for digit in range(1, self.sudoku.size):
				dict_count_for_digit[digit] = 0

		# iterate through columns
		for col_id in range(0, self.sudoku.size):

			# count digits in given row
			for row_id in range(0, self.sudoku.size):
				digit = self.sudoku.board[row_id][col_id]
				dict_count_for_digit[digit] += 1

			# count conflicts
			for digit_count in dict_count_for_digit.values():
				if digit_count > 1:
					conflict_count += 1

			# clear the digit counts
			for digit in range(1, self.sudoku.size):
				dict_count_for_digit[digit] = 0

		# iterate through blocks
		for block_first_row_id in range(0, self.sudoku.size, self.sudoku.rank):
			for block_first_col_id in range(0, self.sudoku.size, self.sudoku.rank):

				# count digits in given block
				for internal_row_id in range(0, self.sudoku.rank):
					for internal_col_id in range(0, self.sudoku.rank):
						digit = self.sudoku \
							.board[block_first_row_id + internal_row_id][block_first_col_id + internal_col_id]
						dict_count_for_digit[digit] += 1

				# count conflicts
				for digit_count in dict_count_for_digit.values():
					if digit_count > 1:
						conflict_count += 1

				# clear the digit counts
				for digit in range(1, self.sudoku.size):
					dict_count_for_digit[digit] = 0

		# update current conflict count
		self._conflict_count = conflict_count

		if self._conflict_count < self._best_conflict_count:
			self._best_conflict_count = self._conflict_count

	def is_this_promising_state(self):
		"""
		Returns True if just updated _conflict_count is better (lower) than calculated _best_conflict_count so far.
		:return: boolean if it is a promising state.
		"""
		self._update_conflict_count()
		if self._best_conflict_count == self._conflict_count:
			return True
		else:
			return False

	def get_distance_from(self, other_state):
		"""
		Calculates the distance from this state to given other_state.
		:return: calculated distance
		"""
		distance = 0
		for row_id in range(0, self.sudoku.size):
			for col_id in range(0, self.sudoku.size):
				if self.sudoku.board[row_id][col_id] != other_state.sudoku.board[row_id][col_id]:
					distance += 1

		return distance

	def get_move_towards(self, other_state):
		"""
		Having all differences between self and other_state, it returns random move - (position, new_digit)
		that certainly would decrease distance between self and other_state.
		:return:	Tuple of: position of digit to be changed, new digit to be inserted on the position.
		"""
		available_moves = []
		for row_id in range(0, self.sudoku.size):
			for col_id in range(0, self.sudoku.size):
				if self.sudoku.board[row_id][col_id] != other_state.sudoku.board[row_id][col_id]:
					available_moves.append(((row_id, col_id), other_state.sudoku.board[row_id][col_id]))

		return random.choice(available_moves)


if __name__ == "__main__":
	S = np.array([
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
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
	for i in range(0, 10):
		state_test.change_randomly()
		print(state_test.sudoku)

