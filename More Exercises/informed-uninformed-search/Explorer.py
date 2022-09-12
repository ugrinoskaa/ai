from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def can_move(x, y, o1, o2):
    in_table = x >= 0 and x < 8 and y >= 0 and y < 6
    return in_table and ((x, y) != o1) and ((x, y) != o2)

class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successor = dict()
        man_x, man_y = state[0], state[1]
        obstacle1 = [state[2], state[3], state[4]] # [2, 5, -1]
        obstacle2 = [state[5], state[6], state[7]]

        if obstacle1[2] == -1 and obstacle1[1] == 0:
            obstacle1_new_d = 1
        elif obstacle1[2] == 1 and obstacle1[1] == 5:
            obstacle1_new_d = -1
        else:
            obstacle1_new_d = obstacle1[2]

        obstacle1_x = obstacle1[0]
        obstacle1_y = obstacle1[1] + obstacle1_new_d

        if obstacle2[2] == -1 and obstacle2[1] == 0:
            obstacle2_new_d = 1
        elif obstacle2[2] == 1 and obstacle2[1] == 5:
            obstacle2_new_d = -1
        else:
            obstacle2_new_d = obstacle2[2]

        obstacle2_x = obstacle2[0]
        obstacle2_y = obstacle2[1] + obstacle2_new_d

        obs1 = (obstacle1_x, obstacle1_y)
        obs2 = (obstacle2_x, obstacle2_y)

        # covece desno
        if can_move(man_x + 1, man_y, obs1, obs2):
            successor["Right"] = (man_x + 1, man_y, obstacle1_x, obstacle1_y, obstacle1_new_d, obstacle2_x, obstacle2_y, obstacle2_new_d)

        # covece levo
        if can_move(man_x - 1, man_y, obs1, obs2):
            successor["Left"] = (man_x - 1, man_y, obstacle1_x, obstacle1_y, obstacle1_new_d, obstacle2_x, obstacle2_y, obstacle2_new_d)

        # covece gore
        if can_move(man_x, man_y + 1, obs1, obs2):
            successor["Up"] = (man_x, man_y + 1, obstacle1_x, obstacle1_y, obstacle1_new_d, obstacle2_x, obstacle2_y, obstacle2_new_d)

        # covece dolu
        if can_move(man_x, man_y - 1, obs1, obs2):
            successor["Down"] = (man_x, man_y - 1, obstacle1_x, obstacle1_y, obstacle1_new_d, obstacle2_x, obstacle2_y, obstacle2_new_d)

        return successor

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man_x = state[0]
        man_y = state[1]
        return [man_x, man_y] == self.goal


if __name__=='__main__':
    x_explorer = int(input())
    y_explorer = int(input())

    x_home = int(input())
    y_home = int(input())

    obstacle_1 = (2, 5, -1)
    obstacle_2 = (5, 0, 1)
    home = [x_home, y_home]

    explorer = Explorer((x_explorer, y_explorer,  obstacle_1[0], obstacle_1[1], obstacle_1[2], obstacle_2[0], obstacle_2[1], obstacle_2[2]), home)

    result = breadth_first_graph_search(explorer).solution()
    print(result)
