from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Star(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    @staticmethod
    def can_move(x, y, w, z):
        in_table = x >= 0 and x < 8 and y >= 0 and y < 8
        return in_table and (x, y) not in (w, z)

    def successor(self, state):
        successors = dict()
        konj_x, konj_y, lovec_x, lovec_y, stars = state
        stars = list(stars)

        # K1 - gore gore levo
        if self.can_move(konj_x + 1, konj_y + 2, lovec_x, lovec_y) and (konj_x, konj_y) != (konj_x + 1, konj_y + 2):
            new_stars = [star for star in stars if star != (konj_x + 1, konj_y + 2)]
            successors["K1"] = (konj_x + 1, konj_y + 2, lovec_x, lovec_y, tuple(new_stars))

        # K2 - gore gore desno
        if self.can_move(konj_x - 1, konj_y + 2, lovec_x, lovec_y) and (konj_x, konj_y) != (konj_x - 1, konj_y + 2):
            new_stars = [star for star in stars if star != (konj_x - 1, konj_y + 2)]
            successors["K2"] = (konj_x - 1, konj_y + 2, lovec_x, lovec_y, tuple(new_stars))

        # K3 - desno desno gore
        if self.can_move(konj_x + 2, konj_y + 1, lovec_x, lovec_y) and (konj_x, konj_y) != (konj_x + 2, konj_y + 1):
            new_stars = [star for star in stars if star != (konj_x + 2, konj_y + 1)]
            successors["K3"] = (konj_x + 2, konj_y + 1, lovec_x, lovec_y, tuple(new_stars))

        # K4 - desno desno dolu
        if self.can_move(konj_x + 2, konj_y - 1, lovec_x, lovec_y) and (konj_x, konj_y) != (konj_x + 2, konj_y - 1):
            new_stars = [star for star in stars if star != (konj_x + 2, konj_y - 1)]
            successors["K4"] = (konj_x + 2, konj_y - 1, lovec_x, lovec_y, tuple(new_stars))

        # K5 - dolu dolu desno
        if self.can_move(konj_x + 1, konj_y - 2, lovec_x, lovec_y) and (konj_x, konj_y) != (konj_x + 1, konj_y - 2):
            new_stars = [star for star in stars if star != (konj_x + 1, konj_y - 2)]
            successors["K5"] = (konj_x + 1, konj_y - 2, lovec_x, lovec_y, tuple(new_stars))

        # K6 - dolu dolu levo
        if self.can_move(konj_x - 1, konj_y - 2, lovec_x, lovec_y) and (konj_x, konj_y) != (konj_x - 1, konj_y - 2):
            new_stars = [star for star in stars if star != (konj_x - 1, konj_y - 2)]
            successors["K6"] = (konj_x - 1, konj_y - 2, lovec_x, lovec_y, tuple(new_stars))

        # K7 - levo levo dolu
        if self.can_move(konj_x - 2, konj_y - 1, lovec_x, lovec_y) and (konj_x, konj_y) != (konj_x - 2, konj_y - 1):
            new_stars = [star for star in stars if star != (konj_x - 2, konj_y - 1)]
            successors["K7"] = (konj_x - 2, konj_y - 1, lovec_x, lovec_y, tuple(new_stars))

        # K8 - levo levo gore
        if self.can_move(konj_x - 2, konj_y + 1, lovec_x, lovec_y) and (konj_x, konj_y) != (konj_x - 2, konj_y + 1):
            new_stars = [star for star in stars if star != (konj_x - 2, konj_y + 1)]
            successors["K8"] = (konj_x - 2, konj_y + 1, lovec_x, lovec_y, tuple(new_stars))

        # B1 - gore levo
        if self.can_move(lovec_x - 1, lovec_y + 1, konj_x, konj_y) and (lovec_x, lovec_y) != (lovec_x - 1, lovec_y + 1):
            new_stars = [star for star in stars if star != (lovec_x - 1, lovec_y + 1)]
            successors["B1"] = (konj_x, konj_y, lovec_x - 1, lovec_y + 1, tuple(new_stars))

        # B2 - gore desno
        if self.can_move(lovec_x + 1, lovec_y + 1, konj_x, konj_y) and (lovec_x, lovec_y) != (lovec_x + 1, lovec_y + 1):
            new_stars = [star for star in stars if star != (lovec_x + 1, lovec_y + 1)]
            successors["B2"] = (konj_x, konj_y, lovec_x + 1, lovec_y + 1, tuple(new_stars))

        # B3 - dolu levo
        if self.can_move(lovec_x - 1, lovec_y - 1, konj_x, konj_y) and (lovec_x, lovec_y) != (lovec_x - 1, lovec_y - 1):
            new_stars = [star for star in stars if star != (lovec_x - 1, lovec_y - 1)]
            successors["B3"] = (konj_x, konj_y, lovec_x - 1, lovec_y - 1, tuple(new_stars))

        # B4 - dolu desno
        if self.can_move(lovec_x + 1, lovec_y - 1, konj_x, konj_y) and (lovec_x, lovec_y) != (lovec_x + 1, lovec_y - 1):
            new_stars = [star for star in stars if star != (lovec_x + 1, lovec_y - 1)]
            successors["B4"] = (konj_x, konj_y, lovec_x + 1, lovec_y - 1, tuple(new_stars))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        stars = state[4]
        return len(stars) == 0


if __name__ == '__main__':
    konj_x = int(input())
    konj_y = int(input())

    lovec_x = int(input())
    lovec_y = int(input())

    star1_x = int(input())
    star1_y = int(input())

    star2_x = int(input())
    star2_y = int(input())

    star3_x = int(input())
    star3_y = int(input())

    stars = ((star1_x, star1_y), (star2_x, star2_y), (star3_x, star3_y))

    star = Star((konj_x, konj_y, lovec_x, lovec_y, stars))

    result = breadth_first_graph_search(star).solution()
    print(result)