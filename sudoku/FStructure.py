
from sudoku.PromisingState import *


class FStructure:
	"""
	Custom data structure containing shared with every ant Promising States.
	"""

	def __init__(self):
		"""
		A constructor.
		"""
		self._promisingStates = {}		# TODO nice to have: more efficient data structure should be used here

	def decrease_pheromones(self):
		"""
		Every iteration each PromisingState's pheromone value should be decreased. When one's value is below zero - that
		PromisingState should be removed from the structure.
		"""
		# TODO

	def add_promising_state(self, new_promising_state):
		"""
		When called, at first FStructure should check if new_promising_state already exist. If not - it should add it to
		self._promisingStates.
		"""
		# TODO

	def get_promising_states(self):
		"""
		Returns all contained PromisingStates sorted by pheromone value.
		"""
		# TODO


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
	state_test = State(Sudoku(S, S_hardcoded))
	print(state_test.sudoku)
	promising_state_test = PromisingState(state_test, 1.0)
	print(promising_state_test)
	f = FStructure()
	f.add_promising_state(promising_state_test)
	print(f)
