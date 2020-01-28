
from sudoku.FStructure import *


class Ant:
	"""
	Simple reactive agent that tries to follow pheromone trail to find optimal path on G graph, that is thoroughly
	described in the documentation.
	"""

	def __init__(self, initial_state, f_structure_ref, attractiveness_base):
		"""
		A constructor.
		:param initial_state:	Initial state representing anthill, from which each ant starts its journey.
		"""
		self._state = copy.deepcopy(initial_state)
		self._initial_state = copy.deepcopy(initial_state)
		self._f_structure = f_structure_ref
		self._attractiveness_base = int(attractiveness_base)
		# self.alpha = 0.1

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
		# try to sense nearest pheromone trail
		(attractiveness, promising_state) = self._f_structure.get_the_most_attractive_promising_state(self.state)

		# based on the attractiveness parameter, there is weighted random choice whether to make random move or
		# move towards promising_state
		acceptance_level_random = random.randrange(0, self._attractiveness_base)
		is_pheromone_sensed = attractiveness > acceptance_level_random

		# make a move
		if is_pheromone_sensed:
			(position, new_digit) = promising_state.state.get_move_towards(self.state)
			self._state.change_deliberately(position, new_digit)
		else:
			self._state.change_randomly()

		# if this is worth it, mark current new state with pheromone
		if self._state.is_this_promising_state():
			pheromone_value = self._get_pheromone_value()
			if self._f_structure.add_promising_state(PromisingState(self.state, pheromone_value)):
				self._get_back_to_anthill()

	def _get_pheromone_value(self):
		"""
		Returns pheromone value for current state.
		"""
		return 1

	def _get_back_to_anthill(self):
		"""
		Ant gets back to the beginning - State S_0
		"""
		self._state = copy.deepcopy(self._initial_state)


if __name__ == "__main__":
	S = np.array([
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
	])
	S_hardcoded = np.array([
		[False, False, True, True],
		[False, False, True, True],
		[False, True, True, True],
		[False, True, False, True]
	])
	f_structure_test = FStructure(0.2, 1.0)
	ant_test = Ant(State(Sudoku(S, S_hardcoded)), f_structure_test, 100000)
	print(ant_test)
	print(ant_test.state.sudoku)
	for i in range(0, 100):
		ant_test.move()
		print(ant_test.state.sudoku)

