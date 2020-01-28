
from sudoku.PromisingState import *
from collections import *

ALPHA = 0.1


class FStructure:
	"""
	Custom data structure containing shared with every ant Promising States.
	"""

	def __init__(self, alpha, decreasing_param):
		"""
		A constructor.
		"""
		self._promising_states = set()		# TODO nice to have: more efficient data structure should be used here
		self._alpha = alpha
		self._decreasing_param = decreasing_param

	def decrease_pheromones(self):
		"""
		Every iteration each PromisingState's pheromone value should be decreased. When one's value is below zero - that
		PromisingState should be removed from the structure.
		"""
		for s in self._promising_states:
			s.pheromone_value *= self._decreasing_param

	def add_promising_state(self, new_promising_state):
		"""
		When called, at first FStructure should check if new_promising_state already exist. If not - it should add it to
		self._promisingStates and return True - else: False. After each insert self._promising_states should be
		re-sorted (when not done by self._promisingStates itself.
		"""
		is_really_new = True
		for prom_state in self._promising_states:
			if np.array_equal(prom_state.state.sudoku.board, new_promising_state.state.sudoku.board):
				prom_state.update_pheromone_value_by(1 + self._alpha)
				is_really_new = False
				break

		if is_really_new:
			self._promising_states.add(new_promising_state)
			return True
		else:
			return False

	def get_the_most_attractive_promising_state(self, other_state):
		"""
		Returns the most attractive promising state along with it's attractiveness for the ant in other_state.
		"""
		attractiveness_best = 0
		state_best = None
		for state in self._promising_states:
			if other_state == state:
				continue
			attractiveness_temp = state.get_attractiveness(other_state)
			if attractiveness_best < attractiveness_temp:
				attractiveness_best = attractiveness_temp
				state_best = state

		return attractiveness_best, state_best


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
	f = FStructure(0.2, 1.0)
	f.add_promising_state(promising_state_test)
	print(f)
