import copy
import time
import heapq

#for creating the tree itself
#TreeNode class has data, children array, parent, and the heuristic value used to compare in the A* algs
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = 0
        self.hVal = 0
        self.depth = 0
        self.tQueue = 0
        self.mQueue = 0
        self.won = 0
    def append(self, newNode):
        self.children.append(newNode)
    def __lt__(self, other):
        return self.hVal < other.hVal

#Pair class, used as a helper for later functions
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        print self.x, self.y

#used to store the board state itself, also has a compare func, display func
#intitializes with a initial board state.
#clone copies another board
#getLoc finds the location of said item in the board
#isequal checks if the board is equal to another board, mostly used to see if were at the goal state w/ wrapper class
#display prints the contents of the 2d array
#getzeroloc gets the location of where the zero is at. considering adding a member that just save the loc, and updates
#every move.
#getMisplacedTiles returns the amt of misplaced tiles
#getManhattanDistance returns the manhattan distance of the board
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
        self.state = copy.deepcopy(boardB.state)
        self.zeroloc = copy.deepcopy(boardB.state)
    def getLoc(self, val):
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state)):
                if self.state[i][j] == val:
                    return Pair(j, i)
    def isEqual(self, boardB):
        for i in range(0, len(boardB.state)):
            for j in range(0, len(boardB.state)):
                if self.state[i][j] != boardB.state[i][j]:
                    return False
        return True
    def quickIsEqual(self, boardB):
        if self.zeroloc.x == boardB.zeroloc.x and self.zeroloc.y == boardB.zeroloc.y:
            return True
        else:
            return False
    def getMisplacedTiles(self, boardB):
        sumMisplacedTiles = 0
        for i in range(0, len(boardB.state)):
            for j in range(0, len(boardB.state)):
                if self.state[i][j] != 0 and self.state[i][j] != boardB.state[i][j]:
                    sumMisplacedTiles += 1
        return sumMisplacedTiles
    def getManhattanDistance(self, boardB):
        manhattanDist = 0
        for i in range(0, len(boardB.state)):
            for j in range(0, len(boardB.state)):
                if self.state[i][j] != 0 and self.state[i][j] != boardB.state[i][j]:
                    goalLoc = boardB.getLoc(self.state[i][j])
                    curLoc = Pair(j, i)
                    manhattanDist += abs(goalLoc.x - curLoc.x) + abs(goalLoc.y - curLoc.y)
        return manhattanDist
    def getZeroLocation(self):
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
    def isSolvable(self):
        temp = []
        inversions = 0
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state)):
                temp.append(self.state[i][j])
        for x in temp:
            print x,
        print
        for i in range(0, len(temp)):
            for j in range(i+1, len(temp)):
                if(temp[i] > temp[j] and  temp[i] != 0 and temp [j] != 0):
                    inversions += 1
        #print inversions
        if inversions & 1:
            return False
        else:
            return True

#holds the Board object internally, used as a helper to the Board, performs ops on it
#weapper class that calls board's internal functions, with some extra
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
    def getMisplacedTiles(self, goalBoard):
        return self.board.getMisplacedTiles(goalBoard)
    def getManhattanDistance(self, goalBoard):
        return self.board.getManhattanDistance(goalBoard)

#returns the depth of the node in its tree
def getDepth(node):
    count = 0
    temp = node.parent
    while temp != 0:
        temp = temp.parent
        count += 1
    return count

#returns the path to the node in its tree
def getPath(node):
    path = []
    moves = []
    temp = node
    while temp != 0:
        path.append(temp)
        temp = temp.parent
    path.reverse()

    for i in range(0, len(path) - 1):
        if path[i].data.board.zeroloc.x < path[i + 1].data.board.zeroloc.x:
            moves.append("Right,")
        elif path[i].data.board.zeroloc.x > path[i + 1].data.board.zeroloc.x:
            moves.append("Left,")
        elif path[i].data.board.zeroloc.y < path[i + 1].data.board.zeroloc.y:
            moves.append("Down,")
        else:
            moves.append("Up,")

    print "Solution Path: "
    for item in path:
        item.data.display()
    print "[ ",
    for item in moves:
        print item,
    print " ]"
    return path

def findSolution(puzzle, goal, type):
    #1 = UCS, 2 = MTH, 3 = MDH
    if type != 1 and type != 2 and type != 3:
        return -1

    # create the root
    root = TreeNode(puzzle)
    heap = []
    heapq.heappush(heap, root)

    tQueue = 0
    mQueue = 0

    while heap:
        #node that is being expanded
        # print "Expanding Node: "
        # queue[0].data.display()

        #found the goal state
        if(heap[0].data.isGoal(goal)):
            print "Goal Has Been Found!"
            heap[0].mQueue = mQueue
            heap[0].tQueue = tQueue
            return heap[0]

        #get all legal moves
        legalMoves = heap[0].data.getLegalMoves()

        #add all legal moves of the node to be it's children
        for item in legalMoves:

            #create the node itself, takes the board state, performs the move, assigns it parent, depth, hVal
            tempNode = TreeNode(Puzzle(Board(copy.deepcopy(heap[0].data.board.state))))
            tempNode.data.move(item)
            tempNode.parent = heap[0]
            tempNode.depth = heap[0].depth + 1
            if type == 1:
                tempNode.hVal = tempNode.depth
            elif type == 2:
                tempNode.hVal = tempNode.data.getMisplacedTiles(goal) + tempNode.depth
            elif type == 3:
                tempNode.hVal = tempNode.data.getManhattanDistance(goal) + tempNode.depth

            # Designate the new node as a child of its parent
            heap[0].append(tempNode)

            #check to see if the node is a return to the parent / grandparent state
            if tQueue >= 1:
                # must check to see that it is not returning to the grandpa move
                if not tempNode.data.board.isEqual(((tempNode.parent).parent).data.board):
                    #add node to the queue
                    heapq.heappush(heap, tempNode)
            else:
                heapq.heappush(heap, tempNode)

        #note that another node has been expanded
        tQueue += 1

        #note the last popped node
        heapq.heappop(heap)

        #check if new max queue size
        if len(heap) > mQueue:
            mQueue = len(heap)

    #should not be Reached
    print "error, queue ended without finding answer"
    return root

while True:
    #take in input
    userInput = raw_input("Welcome to Raymond Farias's puzzle solver:\nEnter 1 for the default puzzle, or 2 to enter your own. (-1 to exit)\n")
    startBoard = []
    endBoard = []
    endBoard.append([1, 2, 3])
    endBoard.append([4, 5, 6])
    endBoard.append([7, 8, 0])

    if(int(userInput) == 0):
        startBoard.append([4, 0, 1])
        startBoard.append([7, 2, 3])
        startBoard.append([5, 8, 6])
    elif(int(userInput) == 1):
        #make default board
        # startBoard.append([1, 2, 3])
        # startBoard.append([4, 0, 6])
        # startBoard.append([7, 5, 8])
        # startBoard = []
        startBoard.append([4, 1, 3])
        startBoard.append([0, 2, 6])
        startBoard.append([7, 5, 8])
    elif(int(userInput) == 2):
        #take in user board
        print("Enter your puzzle, enter a zero to represent the blank.")
        userInput = raw_input("Enter your first row, use space between numbers\n")
        tempList = map(int, userInput.split())
        print tempList
        startBoard.append(tempList)
        userInput = raw_input("Enter your second row, use space between numbers\n")
        tempList = map(int, userInput.split())
        print tempList
        startBoard.append(tempList)
        userInput = raw_input("Enter your third row, use space between numbers\n")
        tempList = map(int, userInput.split())
        print tempList
        startBoard.append(tempList)

        tempBoard = Board(startBoard)
        tempBoard.display()
    elif(int(userInput) == -2):
        startBoard.append([8, 1, 3])
        startBoard.append([4, 0, 2])
        startBoard.append([7, 6, 5])
    elif (int(userInput) == -3):
        startBoard.append([0, 1, 2])
        startBoard.append([3, 4, 5])
        startBoard.append([6, 7, 8])
    elif(int(userInput) == -1):
        raise SystemExit
    else:
        print ("Error, please enter a correct number.")
        raise "InputError"

    userInput = raw_input("1: Uniform Cost Search \n2: A* with Misplaced Tile H. \n3: A* with Manhattan Distance H. (-1 to exit)\n")

    userBoard = Board(startBoard)
    goalBoard = Board(endBoard)

    userPuzzle = Puzzle(userBoard)

    if userBoard.isSolvable() == False:
        raise "Error: Puzzle not solvable!"

    mQueue = 0
    tQueue = 0

    if(int(userInput) == 1):
        start1 = time.time()
        x = findSolution(userPuzzle, goalBoard, 1)
        end1 = time.time()
        time1 = end1 - start1

        print "1, Uniform Cost Search: " + repr(time1)
        count = getDepth(x)
        print "Solution Depth = " + repr(count)
        print "Max Queue Size = " + repr(x.mQueue)
        print "Total Nodes = " + repr(x.tQueue)
        path = getPath(x)
    elif(int(userInput) == 2):
        print "Initial Misplaced Tiles is: " + repr(userPuzzle.getMisplacedTiles(goalBoard))

        start2 = time.time()
        x = findSolution(userPuzzle, goalBoard, 2)
        end2 = time.time()
        time2 = end2 - start2

        print "2, Misplaced Tiles Heuristic A*: " + repr(time2)
        count = getDepth(x)
        print "Solution Depth = " + repr(count)
        print "Max Queue Size = " + repr(x.mQueue)
        print "Total Nodes = " + repr(x.tQueue)
        path = getPath(x)
    elif(int(userInput) == 3):
        print "Initial Manhattan Distance is: " + repr(userPuzzle.getManhattanDistance(goalBoard))

        start3 = time.time()
        x = findSolution(userPuzzle, goalBoard, 3)
        end3 = time.time()
        time3 = end3 - start3

        print "3, Manhattan Distance Heuristic A*: " + repr(time3)
        count = getDepth(x)
        print "Solution Depth = " + repr(count)
        print "Max Queue Size = " + repr(x.mQueue)
        print "Total Nodes = " + repr(x.tQueue)
        path = getPath(x)
    elif(int(userInput) == -1):
        raise SystemExit
    else:
        #try solution
        print "Initial Manhattan Distance is: " + repr(userPuzzle.getManhattanDistance(goalBoard))
        print "Initial Misplaced Tiles is: " + repr(userPuzzle.getMisplacedTiles(goalBoard))

        start1 = time.time()
        x = findSolution(userPuzzle, goalBoard, 1)
        end1 = time.time()
        time1 = end1 - start1

        start2 = time.time()
        y = findSolution(userPuzzle, goalBoard, 2)
        end2 = time.time()
        time2 = end2 - start2

        start3 = time.time()
        z = findSolution(userPuzzle, goalBoard, 3)
        end3 = time.time()
        time3 = end3 - start3

        print "1, Uniform Cost Search: " + repr(time1)
        print "Solution Depth = " + repr(getDepth(x))
        print "Max Queue Size = " + repr(x.mQueue)
        print "Total Nodes = " + repr(x.tQueue)
        path = getPath(x)

        print "2, Misplaced Tiles Heuristic A*: " + repr(time2)
        print "Solution Depth = " + repr(getDepth(y))
        print "Max Queue Size = " + repr(y.mQueue)
        print "Total Nodes = " + repr(y.tQueue)
        path = getPath(y)

        print "3, Manhattan Distance Heuristic A*: " + repr(time3)
        print "Solution Depth = " + repr(getDepth(z))
        print "Max Queue Size = " + repr(z.mQueue)
        print "Total Nodes = " + repr(z.tQueue)
        path = getPath(z)
