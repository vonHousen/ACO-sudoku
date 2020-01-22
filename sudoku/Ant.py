
from sudoku.Sudoku import *
from sudoku.State import *


class Ant:
	"""
	Simple reactive agent that tries to follow pheromone trail to find optimal path on G graph, that is thoroughly
	described in the documentation.
	"""

	def __init__(self, initial_state):
		"""
		A constructor.
		:param initial_state:	Initial state representing anthill, from which each ant starts its journey.
		"""
		self._state = copy.deepcopy(initial_state)

	@property
	def state(self):
		"""
		The only state ant is the owner, which consistently modifies as traveling throughout the G graph.
		"""
		return self._state


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
	ant_test = Ant(State(Sudoku(S, S_hardcoded)))
	print(ant_test.state.sudoku)
	print(ant_test)
