# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

def optimum_policy2D(grid, init, goal, cost):
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]]

    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(4):
                    if goal[0] == x and goal[1] == y:
                        if value[orientation][x][y] > 0:
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                            change = True
                    elif grid[x][y] == 0:
                        for i in range(3):
                            o2 = (orientation + action[i])%4
                            x2 = x + forward[o2][0]
                            y2 = y + forward[o2][1]
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[o2][x2][y2] + cost[i]
                                if v2 < value[orientation][x][y]:
                                    change = True
                                    value[orientation][x][y] = v2
                                    policy[orientation][x][y] = action_name[i]

    x = init[0]
    y = init[1]
    orientation = init[2]
    policy2D[x][y] = policy[orientation][x][y]
    while policy[orientation][x][y] != '*':
        if policy[orientation][x][y] == '#':
            o2 = orientation
        elif policy[orientation][x][y] == 'R':
            o2 = (orientation -1 )%4
        elif policy[orientation][x][y] == 'L':
            o2 = (orientation+1)%4
        x = x + forward[o2][0]
        y = y + forward[o2][1]
        orientation = o2
        policy2D[x][y] = policy[orientation][x][y]

    return policy2D
# ----------------------------------------
# modify code below
# ----------------------------------------
'''
def optimum_policy2D(grid, init, goal, cost):
    close_grid = grid
    policy2D = [[' ' for col in range(len(grid[row]))] for row in range(len(grid))]
    g = 0 # record the cost
    a = action[1]
    open_list = [[g, init[0], init[1], init[2], a]]
    while len(open_list) != 0:
        open_list.sort()
        open_list.reverse()
        next = open_list.pop()
        g = next[0]
        x = next[1]
        y = next[2]
        d = next[3]
        a = next[4]
        close_grid[x][y] = 1
        policy2D[x][y] = action_name[a+1]

        if x == goal[0] and y == goal[1]:
            policy2D[x][y] = '*'
            return policy2D

        for f in range(len(forward)):
            x2 = x + forward[f][0]
            y2 = y + forward[f][1]
            if x2 >= 0 and x2 <= len(grid)-1 and y2 >= 0 and y2 <= len(grid[0])-1:
                if grid[x2][y2] == 0:
                    if f == 0 or f == 2:
                        g2 = g + cost[1]
                        a = action[1]
                    elif f == 1: #left
                        g2 = g + cost[2]
                        a = action[2]
                    else: # Right
                        g2 = g + cost[0]
                        a = action[0]
                    if close_grid[x2][y2] == 0:
                        open_list.append([g2, x2, y2, f, a])
                else: # grid[][] ==1
                    close_grid[x2][y2] = 1

    return policy2D

def optimum_policy2D(grid, init, goal, cost):
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True
                        policy2D[x][y] = '*'

                elif grid[x][y] == 0:
                    for a in range(len(forward)):
                        x2 = x + forward[a][0]
                        y2 = y + forward[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + 1

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                if a == 0 or a == 2:
                                    policy2D[x][y] = action_name[1]
                                elif a == 1:
                                    policy2D[x][y] = action_name[2]
                                elif a == 3:
                                    policy2D[x][y] = action_name[0]

    return policy2D
'''

policy = optimum_policy2D(grid, init,  goal, cost)
for i in range(len(policy)):
    print(policy[i])
