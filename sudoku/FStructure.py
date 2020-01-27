
from sudoku.PromisingState import *
from collections import *


class FStructure:
	"""
	Custom data structure containing shared with every ant Promising States.
	"""

	def __init__(self):
		"""
		A constructor.
		"""
		self._promising_states = OrderedDict()		# TODO nice to have: more efficient data structure should be used here

	def decrease_pheromones(self):
		"""
		Every iteration each PromisingState's pheromone value should be decreased. When one's value is below zero - that
		PromisingState should be removed from the structure.
		"""
		for s in self._promising_states:
			s.pheromone_value = s.pheromone_value/s.get_distance_from()
		# TODO

	def add_promising_state(self, new_promising_state, alpha):
		"""
		When called, at first FStructure should check if new_promising_state already exist. If not - it should add it to
		self._promisingStates and return True - else: False. After each insert self._promising_states should be
		re-sorted (when not done by self._promisingStates itself.
		"""
		if not self._promising_states.__contains__(new_promising_state):
			new_promising_state.pheromone_value = (1-alpha)*new_promising_state.pheromone_value
			self._promising_states.popitem(new_promising_state)

		return True		# TODO

	def get_the_most_attractive_promising_state(self, other_state):
		"""
		Returns the most attractive promising state along with it's attractiveness for the ant in other_state.
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
