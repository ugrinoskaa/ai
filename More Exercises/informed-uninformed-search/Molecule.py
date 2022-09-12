from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def can_move(x, y, obstacles_molecule, obstacles):
    in_table = x >= 0 and x < 9 and y >= 0 and y < 7
    return in_table and (x, y) not in obstacles_molecule and (x, y) not in obstacles

def right(x, y, obstacles_molecule, obstacles):
    x_new = x + 1
    if can_move(x_new, y, obstacles_molecule, obstacles):
        return right(x_new, y, obstacles_molecule, obstacles)
    else:
        return (x, y)

def left(x, y, obstacles_molecule, obstacles):
    x_new = x - 1
    if can_move(x_new, y, obstacles_molecule, obstacles):
        return left(x_new, y, obstacles_molecule, obstacles)
    else:
        return (x, y)

def up(x, y, obstacles_molecule, obstacles):
    y_new = y + 1
    if can_move(x, y_new, obstacles_molecule, obstacles):
        return up(x, y_new, obstacles_molecule, obstacles)
    else:
        return (x, y)

def down(x, y, obstacles_molecule, obstacles):
    y_new = y - 1
    if can_move(x, y_new, obstacles_molecule, obstacles):
        return right(x, y_new, obstacles_molecule, obstacles)
    else:
        return (x, y)

class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        h1_x, h1_y, h2_x, h2_y, o_x, o_y = state

        # molecule right H1
        h1_right = right(h1_x, h1_y, ((h2_x, h2_y), (o_x, o_y)), self.obstacles)
        if h1_right != (h1_x, h1_y):
            successors["RightH1"] = (h1_right[0], h1_right[1], h2_x, h2_y, o_x, o_y)

        # molecule right H2
        h2_right = right(h2_x, h2_y, ((h1_x, h1_y), (o_x, o_y)), self.obstacles)
        if h2_right != (h2_x, h2_y):
            successors["RightH2"] = (h1_x, h1_y, h2_right[0], h2_right[1], o_x, o_y)

        # molecule right O
        o_right = right(o_x, o_y, ((h1_x, h1_y), (h2_x, h2_y)), self.obstacles)
        if o_right != (o_x, o_y):
            successors["RightO"] = (h1_x, h1_y, h2_x, h2_y, o_right[0], o_right[1])

        # molecule left H1
        h1_left = left(h1_x, h1_y, ((h2_x, h2_y), (o_x, o_y)), self.obstacles)
        if h1_left != (h1_x, h1_y):
            successors["LeftH1"] = (h1_left[0], h1_left[1], h2_x, h2_y, o_x, o_y)

        # molecule left H2
        h2_left = left(h2_x, h2_y, ((h1_x, h1_y), (o_x, o_y)), self.obstacles)
        if h2_left != (h2_x, h2_y):
            successors["LeftH2"] = (h1_x, h1_y, h2_left[0], h2_left[1], o_x, o_y)

        # molecule left O
        o_left = left(o_x, o_y, ((h1_x, h1_y), (h2_x, h2_y)), self.obstacles)
        if o_left != (o_x, o_y):
            successors["LeftO"] = (h1_x, h1_y, h2_x, h2_y, o_left[0], o_left[1])

        # molecule up H1
        h1_up = up(h1_x, h1_y, ((h2_x, h2_y), (o_x, o_y)), self.obstacles)
        if h1_up != (h1_x, h1_y):
            successors["UpH1"] = (h1_up[0], h1_up[1], h2_x, h2_y, o_x, o_y)

        # molecule up H2
        h2_up = up(h2_x, h2_y, ((h1_x, h1_y), (o_x, o_y)), self.obstacles)
        if h2_up != (h2_x, h2_y):
            successors["UpH2"] = (h1_x, h1_y, h2_up[0], h2_up[1], o_x, o_y)

        # molecule up O
        o_up = up(o_x, o_y, ((h1_x, h1_y), (h2_x, h2_y)), self.obstacles)
        if o_up != (o_x, o_y):
            successors["UpO"] = (h1_x, h1_y, h2_x, h2_y, o_up[0], o_up[1])

        # molecule down H1
        h1_down = down(h1_x, h1_y, ((h2_x, h2_y), (o_x, o_y)), self.obstacles)
        if h1_down != (h1_x, h1_y):
            successors["DownH1"] = (h1_down[0], h1_down[1], h2_x, h2_y, o_x, o_y)

        # molecule down H2
        h2_down = down(h2_x, h2_y, ((h1_x, h1_y), (o_x, o_y)), self.obstacles)
        if h2_down != (h2_x, h2_y):
            successors["DownH2"] = (h1_x, h1_y, h2_down[0], h2_down[1], o_x, o_y)

        # molecule down O
        o_down = down(o_x, o_y, ((h1_x, h1_y), (h2_x, h2_y)), self.obstacles)
        if o_down != (o_x, o_y):
            successors["DownO"] = (h1_x, h1_y, h2_x, h2_y, o_down[0], o_down[1])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        h1_y, h2_y, o_y = state[1], state[3], state[5]
        h1_x, h2_x, o_x = state[0], state[2], state[4]
        y_ok = h1_y == h2_y == o_y
        x_ok = (o_x == h1_x + 1 and h2_x == o_x + 1)
        return x_ok and y_ok

if __name__ == '__main__':
    obstacles_list = [(0, 1), (1, 1), (1, 3), (2, 5), (3, 1), (3, 6), (4, 2),
                      (5, 6), (6, 1), (6, 2), (6, 3), (7, 3), (7, 6), (8, 5)]
    h1_x = int(input())
    h1_y = int(input())

    h2_x = int(input())
    h2_y = int(input())

    o_x = int(input())
    o_y = int(input())

    # h1_position = [h1_x, h1_y]
    # h2_position = [h2_x, h2_y]
    # o_position = [o_x, o_y]

    molecule = Molecule(obstacles_list, (h1_x, h1_y, h2_x, h2_y, o_x, o_y))

    result = breadth_first_graph_search(molecule).solution()
    print(result)