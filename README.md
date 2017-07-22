Requires Python 2.7.11 to run.

Solves an 8-Puzzle, printing the solution path to the goal state.

Details:
The user may first choose either a default 8-puzzle or to enter their own custom 8 puzzle. (MUST BE SOLVABLE)

Then they may choose their algorithm of choice:
Uniform Cost Search (weights of tree edges are all 1 so effectively bfs)
A* with Misplaced Tiles Heuristic
A* with Manhattan Distance Heuristic

The program then returns the solution found, its depth, and the path to it from the initial state.

How to use:
The program will prompt you to either enter a custom puzzle or use the default
then it will prompt you to choose the algorithm
then it runs
prints the depth, queue size, total nodes, and the path to the solution
it then loops back and prompts again
Enter -1 at any time to exit
