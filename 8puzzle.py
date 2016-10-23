import copy

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
#intitializes with a initial board state.
#clone copies another board
#isequal checks if the board is equal to another board, mostly used to see if were at the goal state w/ wrapper class
#display prints the contents of the 2d array
#getzeroloc gets the location of where the zero is at. considering adding a member that just save the loc, and updates
#every move.
#The move functions move the blank left right up or down (our operators), does not error check because the wrapper does

class Board:
    def __init__(self):
        self.state = []
        self.zeroloc = 0
    def __init__(self, initial_state):
        self.state = initial_state
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state)):
                if self.state[i][j] == 0:
                    initialZero = Pair(j, i)
        self.zeroloc = initialZero
    def clone(self, boardB):
        self.state = boardB.state
        self.zeroloc = boardB.state
    def isEqual(self, boardB):
        for i in range(0, len(boardB.state)):
            for j in range(0, len(boardB.state)):
                if(self.state[i][j] != boardB.state[i][j]):
                    return False
        return True
    def getZeroLocation(self):
        # for i in range(0, len(self.state)):
        #     for j in range(0, len(self.state)):
        #         if self.state[i][j] == 0:
        #             return Pair(j, i)
        return self.zeroloc
    def display(self):
        for i in range(0, len(self.state)):
            print "-",
        print " "
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state)):
                print repr(self.state[i][j]),
            print " "
        for i in range(0, len(self.state)):
            print "-",
        print " "
    def moveUp(self):
        loc = self.getZeroLocation()
        self.state[loc.y][loc.x] = self.state[loc.y - 1][loc.x]
        self.state[loc.y - 1][loc.x] = 0
        self.zeroloc = Pair(self.zeroloc.x, self.zeroloc.y - 1)

    def moveRight(self):
        loc = self.getZeroLocation()
        self.state[loc.y][loc.x] = self.state[loc.y][loc.x + 1]
        self.state[loc.y][loc.x + 1] = 0
        self.zeroloc = Pair(self.zeroloc.x + 1, self.zeroloc.y)

    def moveDown(self):
        loc = self.getZeroLocation()
        self.state[loc.y][loc.x] = self.state[loc.y + 1][loc.x]
        self.state[loc.y + 1][loc.x] = 0
        self.zeroloc = Pair(self.zeroloc.x, self.zeroloc.y + 1)

    def moveLeft(self):
        loc = self.getZeroLocation()
        self.state[loc.y][loc.x] = self.state[loc.y][loc.x - 1]
        self.state[loc.y ][loc.x - 1] = 0
        self.zeroloc = Pair(self.zeroloc.x - 1, self.zeroloc.y)



#holds the Board object internally, used as a helper to the Board, performs ops on it
class Puzzle:
    def __init__(self, board):
        self.board = board
    def clone(self, puzzleB):
        self.board = puzzleB.board
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
        print "expanding another node"
        queue[0].data.display()
        if(queue[0].data.isGoal(goal)):
            print "found it"
            return
        legalMoves = queue[0].data.getLegalMoves()
        for item in legalMoves:
            print item
            queue[0].append(TreeNode(Puzzle(Board(copy.deepcopy(queue[0].data.board.state)))))
            queue[0].children[-1].data.move(item)
        for node in queue[0].children:
            queue.append(node)
            node.data.display()
        queue.pop(0)

    # #print "expanding another node"
    # queue[0].data.display()
    # if (queue[0].data.isGoal(goal)):
    #     print "found it"
    #     return
    # legalMoves = queue[0].data.getLegalMoves()
    # for item in legalMoves:
    #     print item
    #     queue[0].append(TreeNode(Puzzle(Board(list(queue[0].data.board.state)))))
    #     queue[0].children[-1].data.move(item)
    #     queue[-1].data.display()
    #     #print len(queue[0].children)
    # for node in queue[0].children:
    #     #print id(node)
    #     queue.append(node)
    #     node.data.display()


    queue.pop(0)
    return

#take in input
userInput = raw_input("Welcome to Raymond Farias's puzzle solver: Enter 1 for the default puzzle, or 2 to enter your own.")
startBoard = []
endBoard = []
if(int(userInput) == 1):
    #make default board
    startBoard = []
    startBoard.append([1, 2, 3])
    startBoard.append([4, 0, 6])
    startBoard.append([7, 5, 8])

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
# userBoard.display()
#userBoard.moveLeft()
# userBoard.display()
goalBoard = Board(endBoard)

#puzzle test
userPuzzle = Puzzle(userBoard)
# userPuzzle.display()
# print userPuzzle.getLegalMoves()
# print userPuzzle.isGoal(goalBoard)

#try solution
findSolution(userPuzzle, goalBoard)