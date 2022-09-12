from searching_framework.utils import Problem
from searching_framework.informed_search import *
import math


class Football(Problem):

    def __init__(self, opponents, obstacles_ball, initial, goal=None):
        super().__init__(initial, goal)
        self.opponents = opponents
        self.obstacles_ball = obstacles_ball

    @staticmethod
    def check_valid(x, y):
        in_table = x >= 0 and x < 8 and y >= 0 and y < 6
        return in_table and (x, y) not in opponents and (x, y) not in obstacles_ball

    def successor(self, state):
        succ = dict()

        x_man, y_man, x_ball, y_ball = state

        # GORE
        if self.check_valid(x_man, y_man + 1):
            if (x_man, y_man + 1) == (x_ball, y_ball) and self.check_valid(x_ball, y_ball + 1): # ja sutnal topkata
                succ['t-gore'] = (x_man, y_man + 1, x_ball, y_ball + 1)
            else:
                succ['c-gore'] = (x_man, y_man + 1, x_ball, y_ball) # nemalo topka

        # DOLU
        if self.check_valid(x_man, y_man - 1):
            if (x_man, y_man - 1) == (x_ball, y_ball) and self.check_valid(x_ball, y_ball - 1):
                succ['t-dolu'] = (x_man, y_man - 1, x_ball, y_ball - 1)
            else:
                succ['c-dolu'] = (x_man, y_man - 1, x_ball, y_ball)

        # DESNO
        if self.check_valid(x_man + 1, y_man):
            if (x_man + 1, y_man) == (x_ball, y_ball) and self.check_valid(x_ball + 1, y_ball):
                succ['t-desno'] = (x_man + 1, y_man, x_ball + 1, y_ball)
            else:
                succ['c-desno'] = (x_man + 1, y_man, x_ball, y_ball)

        # GORE-DESNO
        if self.check_valid(x_man + 1, y_man + 1):
            if (x_man + 1, y_man + 1) == (x_ball, y_ball) and self.check_valid(x_ball + 1, y_ball + 1):
                succ['t-gore-desno'] = (x_man + 1, y_man + 1, x_ball + 1, y_ball + 1)
            else:
                succ['c-gore-desno'] = (x_man + 1, y_man + 1, x_ball, y_ball)

        # DOLU-DESNO
        if self.check_valid(x_man + 1, y_man - 1):
            if (x_man + 1, y_man - 1) == (x_ball, y_ball) and self.check_valid(x_ball + 1, y_ball - 1):
                succ['t-dolu-desno'] = (x_man + 1, y_man - 1, x_ball + 1, y_ball - 1)
            else:
                succ['c-dolu-desno'] = (x_man + 1, y_man - 1, x_ball, y_ball)

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        ball_x, ball_y = state[2], state[3]
        if (ball_x, ball_y) in self.goal:
            return True

    @staticmethod
    def mhd(x, y, w, z):
        return abs(x - w) + abs(y - z)

    def h(self, node):
        x_ball, y_ball = node.state[2], node.state[3]
        goal1_x, goal1_y = self.goal[0][0], self.goal[0][1]
        goal2_x, goal2_y = self.goal[1][0], self.goal[1][1]
        first_mhd = self.mhd(x_ball, y_ball, goal1_x, goal1_y)
        second_mhd = self.mhd(x_ball, y_ball, goal2_x, goal2_y)
        return min(first_mhd, second_mhd)


if __name__ == '__main__':
    x_man = int(input())
    y_man = int(input())

    x_ball = int(input())
    y_ball = int(input())

    goal = ((7, 2), (7, 3))

    obstacles_ball = ((2, 2), (3, 2), (4, 2), (2, 3), (4, 3), (5, 3), (6, 3), (2, 4), (3, 4), (4, 4),
                      (6, 4), (4, 5), (5, 5), (6, 5))

    opponents = ((3, 3), (5, 4))

    football = Football(opponents, obstacles_ball, (x_man, y_man, x_ball, y_ball), goal)

    result = astar_search(football).solution()
    print(result)
