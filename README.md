Requires Python 2.7.11 to run.

Solves a 8-Puzzle, printing the solution path to the goal state.

Details:
The user may first choose either a default 8-puzzle or to enter their own custom 8 puzzle. (MUST BE SOLVABLE)

Then they may choose their algorithm of choice:
Uniform Cost Search (weights of tree edges are all 1 so effectively bfs)
A* with Misplaced Tiles Heuristic
A* with Manhattan Distance Heuristic

The program then returns the solution found, its depth, and the path to it from the initial state.