import math

# Write a program that solves the following problem using python/scala/golang: Three missionaries and three cannibals come to a river and find a boat that holds two people. Everyone must get across the river to continue on the journey. However, if the cannibals ever outnumber the missionaries on either bank, the missionaries will be eaten. Find a series of crossings that will get everyone safely to the other side of the river.

# ---- Solution ----

# Initially, both the missionaries and cannibals are on the left side of the river, with 0 missionaries and 0 cannibals on the left bank and 3 missionaries and 3 cannibals on the right bank.

# The following steps are taken to transport them safely:

# Two cannibals are sent to the left bank: 0 missionaries, 2 cannibals on the left bank, and 3 missionaries, 1 cannibal on the right bank.

# One cannibal is sent from left to right: 0 missionaries, 1 cannibal on the left bank, and 3 missionaries, 2 cannibals on the right bank.

# The remaining two cannibals are sent to the left bank: 0 missionaries, 3 cannibals on the left bank, and 3 missionaries, 0 cannibals on the right bank.

# One cannibal is sent to the right bank: 0 missionaries, 2 cannibals on the left bank, and 3 missionaries, 1 cannibal on the right bank.

# Two missionaries are sent to the left bank: 2 missionaries, 2 cannibals on the left bank, and 1 missionary, 1 cannibal on the right bank.

# One missionary and one cannibal are sent to the right bank: 1 missionary, 1 cannibal on the left bank, and 2 missionaries, 2 cannibals on the right bank.

# Two missionaries are sent to the left bank: 3 missionaries, 1 cannibal on the left bank, and 0 missionaries, 2 cannibals on the right bank.

# One cannibal is sent to the right bank: 3 missionaries, 0 cannibals on the left bank, and 0 missionaries, 3 cannibals on the right bank.

# Two cannibals are sent to the left bank: 3 missionaries, 2 cannibals on the left bank, and 0 missionaries, 1 cannibal on the right bank.

# One cannibal is sent to the right bank: 3 missionaries, 1 cannibal on the left bank, and 0 missionaries, 2 cannibals on the right bank.

# Two cannibals are sent to the left bank: 3 missionaries, 3 cannibals on the left bank, and 0 missionaries, 0 cannibals on the right bank.

# This sequence ensures that all missionaries and cannibals have crossed the river safely.







class State():
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None

	def is_goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	def is_valid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False

	def __eq__(self, other):
		return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
                   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
                   and self.missionaryRight == other.missionaryRight

	def __hash__(self):
		return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))

def successors(cur_state):
	children = []
	if cur_state.boat == 'left':
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 2)
		## Two missionaries cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 2, cur_state.missionaryRight)
		## Two cannibals cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)
		## One missionary and one cannibal cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 1)
		## One missionary crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight)
		## One cannibal crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	else:
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 2)
		## Two missionaries cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 2, cur_state.missionaryRight)
		## Two cannibals cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)
		## One missionary and one cannibal cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 1)
		## One missionary crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight)
		## One cannibal crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	return children

def breadth_first_search():
	initial_state = State(3,3,'left',0,0)
	if initial_state.is_goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.is_goal():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print ("(" + str(state.cannibalLeft) + "," + str(state.missionaryLeft) \
                              + "," + state.boat + "," + str(state.cannibalRight) + "," + \
                              str(state.missionaryRight) + ")")

def main():
	solution = breadth_first_search()
	print("Steps: ")
	print_solution(solution)

main()