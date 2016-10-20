#for creating the tree itself
class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []
	def append(self, newNode):
		self.children.append(newNode)

#used to store the board state itself, also has a compare func, display func
class Board:
    def __init__(self, initial_state):
        state = initial_state
    def isEqual(self, boardB):
        for i in range(0, len(boardB)):
            for j in range(0, len(boardB)):
                if(self.state[i][j] != boardB.state[i][j]):
                    return False
        return True
    def display(self):
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                print repr(self.state[i][j]) + " "

#holds the Board object internally, used as a helper to the Board, performs ops on it
class Puzzle:
	def __init__(self, board):
		self.board = board
	def display(self):
		board.display()
# 	def isGoal(self):
# 		if(board[len(board) - 1][len(board - 1)] != 0):
# 			return False
# 		for i in range(0, len(board):
# 			for j in range

#take in input
userInput = raw_input("Welcome to Raymond Farias's puzzle solver: Enter 1 for the default puzzle, or 2 to enter your own.")
if(userInput == 1):
    #make default board
    defBoard = []
    defBoard.append([1, 2, 0])
    defBoard.append([4, 5, 3])
    defBoard.append([7, 8, 6])
elif(userInput == 2):
    #take in user board
    print("Enter your puzzle, enter a zero to represent the blank.")
else:
    print ("Error, please enter a correct number.")
    
userBoard = Board(defBoard)
userBoard.display()
