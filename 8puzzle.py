#for creating the tree itself
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def append(self, newNode):
        self.children.append(newNode)

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#used to store the board state itself, also has a compare func, display func
class Board:
    def __init__(self):
        self.state = []
    def __init__(self, initial_state):
        self.state = initial_state
    def isEqual(self, boardB):
        for i in range(0, len(boardB.state)):
            for j in range(0, len(boardB.state)):
                if(self.state[i][j] != boardB.state[i][j]):
                    return False
        return True
    def getZeroLocation(self):
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state)):
                if self.state[i][j] == 0:
                    return Pair(j, i)
    def display(self):
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state)):
                print repr(self.state[i][j]),
            print " "
    def moveUp(self):
        loc = self.getZeroLocation()
        self.state[loc.y][loc.x] = self.state[loc.y - 1][loc.x]
        self.state[loc.y - 1][loc.x] = 0

    def moveRight(self):
        loc = self.getZeroLocation()
        self.state[loc.y][loc.x] = self.state[loc.y][loc.x + 1]
        self.state[loc.y][loc.x + 1] = 0

    def moveDown(self):
        loc = self.getZeroLocation()
        self.state[loc.y][loc.x] = self.state[loc.y + 1][loc.x]
        self.state[loc.y + 1][loc.x] = 0

    def moveLeft(self):
        loc = self.getZeroLocation()
        self.state[loc.y][loc.x] = self.state[loc.y][loc.x - 1]
        self.state[loc.y ][loc.x - 1] = 0



#holds the Board object internally, used as a helper to the Board, performs ops on it
class Puzzle:
    def __init__(self, board):
        self.board = board
    def display(self):
        self.board.display()
    def isGoal(self, goalBoard):
        return self.board.isEqual(goalBoard)
    def getLegalMoves(self):
        tempPair = self.board.getZeroLocation()
        legalMoves = []
        if(tempPair.x > 0):
            legalMoves.append("l")
        if(tempPair.y > 0):
            legalMoves.append("u")
        if(tempPair.x < len(self.board.state) - 1):
            legalMoves.append("r")
        if(tempPair.y < len(self.board.state) - 1):
            legalMoves.append("d")
        return legalMoves
    def move(self, direction):
        if(direction == "u"):
            self.board.moveUp()
        elif(direction == "r"):
            self.board.moveRight()
        elif (direction == "d"):
            self.board.moveDown()
        elif (direction == "l"):
            self.board.moveLeft()

def findSolution(puzzle, goal):
    # create the root
    root = TreeNode(puzzle)
    queue = []
    queue.append(root)

    while queue:
        legalMoves = queue[0].data.getLegalMoves()
        for item in legalMoves:
            tempPuzzle = queue[0]
            tempPuzzle.move(item)
            queue[0].append(TreeNode(tempPuzzle))

#take in input
userInput = raw_input("Welcome to Raymond Farias's puzzle solver: Enter 1 for the default puzzle, or 2 to enter your own.")
startBoard = []
endBoard = []
if(int(userInput) == 1):
    #make default board
    startBoard = []
    startBoard.append([1, 5, 2])
    startBoard.append([4, 0, 3])
    startBoard.append([7, 8, 6])

    endBoard.append([1, 2, 3])
    endBoard.append([4, 5, 6])
    endBoard.append([7, 8, 0])
elif(int(userInput) == 2):
    #take in user board
    print("Enter your puzzle, enter a zero to represent the blank.")
else:
    print ("Error, please enter a correct number.")
    raise "InputError"


#board test
userBoard = Board(startBoard)
userBoard.display()
#userBoard.moveLeft()

goalBoard = Board(endBoard)

#puzzle test
userPuzzle = Puzzle(userBoard)
userPuzzle.display()
print userPuzzle.getLegalMoves()
print userPuzzle.isGoal(goalBoard)