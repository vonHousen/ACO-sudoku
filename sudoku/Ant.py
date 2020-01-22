
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
		self._initial_state = copy.deepcopy(initial_state)

	@property
	def state(self):
		"""
		The only state ant is the owner, which consistently modifies as traveling throughout the G graph.
		"""
		return self._state

	def move(self):
		"""
		Ant makes a move (in graph sense) = changes its state into another.
		Depends on environment (attractiveness of the nearest Promising State = intensiveness of pheromones).
		If pheromones are perceived easily, ant moves towards them = calls self.state.change_deliberately().
		Else - makes random change = calls self.state.change_randomly().
		After the move ant checks if self.state.is_this_promising_state() - if so, it makes PromisingState out of it,
		adds it to F-structure and come back to the anthill. If it was already existing PromisingState, ant is not
		coming back but go further looking for the better, not known one.
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
	ant_test = Ant(State(Sudoku(S, S_hardcoded)))
	print(ant_test.state.sudoku)
	print(ant_test)
