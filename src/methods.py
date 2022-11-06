import numpy as np


## Function to move the empty space left
def ActionMoveLeft(currentState):
    currentState_temp = np.copy(currentState)
    if ((np.where(currentState == 0)[0][0]) == 0) or ((np.where(currentState == 0)[0][0]) == 1) or ((np.where(currentState == 0)[0][0]) == 2):
        return np.array([])
    else:
        currentState_temp[(np.where(currentState == 0)[0][0])], currentState_temp[(np.where(currentState == 0)[0][0])-3] = currentState[(np.where(currentState == 0)[0][0])-3], currentState[(np.where(currentState == 0)[0][0])]

    return currentState_temp


## Function to move the empty space right
def ActionMoveRight(currentState):
    currentState_temp = np.copy(currentState)
    if ((np.where(currentState == 0)[0][0]) == 6) or ((np.where(currentState == 0)[0][0]) == 7) or ((np.where(currentState == 0)[0][0]) == 8):
        return np.array([])
    else:
        currentState_temp[(np.where(currentState == 0)[0][0])], currentState_temp[(np.where(currentState == 0)[0][0])+3] = currentState[(np.where(currentState == 0)[0][0])+3], currentState[(np.where(currentState == 0)[0][0])]

    return currentState_temp


## Function to move the empty space up
def ActionMoveUp(currentState):
    currentState_temp = np.copy(currentState)
    if ((np.where(currentState == 0)[0][0]) == 0) or ((np.where(currentState == 0)[0][0]) == 3) or ((np.where(currentState == 0)[0][0]) == 6):
        return np.array([])
    else:
        currentState_temp[(np.where(currentState == 0)[0][0])], currentState_temp[(np.where(currentState == 0)[0][0])-1] = currentState[(np.where(currentState == 0)[0][0])-1], currentState[(np.where(currentState == 0)[0][0])]

    return currentState_temp


## Function to move the empty space down
def ActionMoveDown(currentState):
    currentState_temp = np.copy(currentState)
    if ((np.where(currentState == 0)[0][0]) == 2) or ((np.where(currentState == 0)[0][0]) == 5) or ((np.where(currentState == 0)[0][0]) == 8):
        return np.array([])
    else:
        currentState_temp[(np.where(currentState == 0)[0][0])], currentState_temp[(np.where(currentState == 0)[0][0])+1] = currentState[(np.where(currentState == 0)[0][0])+1], currentState[(np.where(currentState == 0)[0][0])]

    return currentState_temp


## Get child states of the current state
def getChildren(currentState):
    children = []

    if ActionMoveUp(currentState).size != 0:
        children.append(ActionMoveUp(currentState))

    if ActionMoveRight(currentState).size != 0:
        children.append(ActionMoveRight(currentState))

    if ActionMoveDown(currentState).size != 0:
        children.append(ActionMoveDown(currentState))

    if ActionMoveLeft(currentState).size != 0:
        children.append(ActionMoveLeft(currentState))

    return children


## Function for backtracking
def generate_path(visited, parent):
    solution = []

    i = len(visited) - 1

    while (i >= 0):
        solution.append(visited[i])
        i = (parent[i] - 1)

    return solution[::-1]


## Generate output text files
def write(solution, visited, parent):
    with open('../output/nodePath.txt', 'w') as file:
        for item in solution:
            file.write((" ".join([str(int) for int in item])) + '\n')

    with open('../output/Nodes.txt', 'w') as file:
        for item in visited:
            file.write((" ".join([str(int) for int in item])) + '\n')

    with open('../output/NodesInfo.txt', 'w') as file:
        file.write('Node_index' + '   ' + 'Parent_Node_index' + '   ' + "\n")
        i = 0
        for item in parent:
            file.write(str(i+1) + ' ' + str(item) + ' ' + '\n')
            i += 1
            


def print_matrix(state):
    counter = 0
    for row in range(0, len(state), 3):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(state), 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")


def print_solution():
    fname = '../output/nodePath.txt'
    data = np.loadtxt(fname)
    if len(data[1]) is not 9:
        print("Format of the text file is incorrect, retry ")
    else:
        for i in range(0, len(data)):
            if i == 0:
                print("Start Node")
            elif i == len(data)-1:
                print("Achieved Goal Node")
            else:
                print("Step ",i)
            print_matrix(data[i])
            print()
            print()





    
    