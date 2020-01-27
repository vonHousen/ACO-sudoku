
from sudoku.State import *


class PromisingState:
	"""
	Decorator design pattern.
	It is the state that is distinguished because it has less conflicts than ant's previous one.
	Ant creates this object based on its current state and passes it to the F structure to be known to all other ants.
	"""
	def __init__(self, state, pheromone_value):
		"""
		A constructor.
		:param state:			ant's current state which is promising for it.
		:param pheromone_value:	pheromone value state is marked by the ant.
		"""
		self._state = copy.deepcopy(state)
		self._pheromone_value = pheromone_value

	@property
	def state(self):
		"""
		State that is distinguished.
		"""
		return self._state

	@property
	def pheromone_value(self):
		"""
		Pheromone value state is marked by the ant.
		"""
		return self._pheromone_value

	def get_attractiveness(self, other_state):
		"""
		When called, it returns attractiveness value of self, based on calculated distance from given other_state
		and self.pheromone_value.
		:param other_state: 	state from which distance is calculated.
		:return: 				attractiveness value
		"""
		return 1		# TODO - should call self.state.get_distance_from(other_state) for sure


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
