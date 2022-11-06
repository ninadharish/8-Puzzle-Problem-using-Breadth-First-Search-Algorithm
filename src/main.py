import numpy as np
from queue import Queue
from methods import *


## Find the solution from initial state to goal state by Breadth First Search
def bfs(initial_state, goal_state):

    if np.array_equal(initial_state, goal_state):
        print("Start state is equal to Goal state")

    else: 

        goal_reached = False

        start_node = initial_state

        queue = Queue(maxsize=0)
        visited = []
        parent = []

        parent.append(0)

        queue.put(start_node)
        parent_id = 0

        while (not queue.empty()) and (not goal_reached):

            currentState = queue.get()

            if ((visited.count(currentState.tolist())) > 0):
                continue

            visited.append(currentState.tolist())
            parent_id += 1

            if np.array_equal(currentState, goal_state):
                goal_reached = True
                print("Goal Reached")
                print("")
                break 
            else:
                childrenStates = getChildren(currentState)
                if childrenStates:
                    for x in childrenStates:
                        if (not ((visited.count(x.tolist())) > 0)):
                            queue.put(x)
                            parent.append(parent_id)

        parent = parent[:len(visited)]

        solution = generate_path(visited, parent)

        write(solution, visited, parent)
        print_solution()



if __name__ == "__main__":

    ## Test Case (Generated files and are located inside the folder /output)
    initial_state = np.array([4, 1, 7, 2, 0, 8, 5, 3, 6])
    goal_state = np.array([1, 4, 7, 2, 5, 8, 3, 6, 0])


    bfs(initial_state, goal_state)