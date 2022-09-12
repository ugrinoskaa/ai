import time

from searching_framework.informed_search import *
from searching_framework.utils import Problem

class Pacman(Problem):
    def __init__(self, grid_size_x, grid_size_y, obstacles, pacdad, initial, goal=None):
         super().__init__(initial, goal)
         self.grid_size_x = grid_size_x
         self.grid_size_y = grid_size_y
         self.obstacles = obstacles
         self.pacdad = pacdad

    def goal_test(self, state):
        # state = ( (p1,p2,..pk), (0,0,1,1..MxN), (gh) )
        remaining_food = sum(state[1])
        if remaining_food > 0:
            return False

        for pacchild in state[0]:
            if pacchild != self.pacdad:
                return False

        return True

    # presmetka na Manhattan distance
    @staticmethod
    def MHD(pacchild, pacdad):
        return abs(pacchild[0] - pacdad[0]) + abs(pacchild[1] - pacdad[1])

    # evristika za decata pakmani koga se dvizat za 1 cekor!
    def h(self, node):
        remaining_food = sum(node.state[1])
        pacchildren = node.state[0]
        h_food = remaining_food / len(pacchildren)
        h_max_mhd = 0

        for pacchild in pacchildren:
            value = Pacman.MHD(pacchild, self.pacdad)
            if value > h_max_mhd:
                h_max_mhd = value

        return max(h_food, h_max_mhd)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def successor(self, state):
        # state = ( (p1,p2..pk), (0,0,0,1,0,0...MxN), (ghost) )
        successors = dict()
        pacchildren = state[0]
        food = state[1]
        ghost = self.next_ghost_location_bfs()
        pacchildren_actions = []
        for pacchild in pacchildren:
            pacchildren_actions.append(self.get_valid_actions(pacchild, food, ghost))
            combined_actions = self.combine_actions(pacchildren_actions, 0)
        for action in combined_actions:
            action_name = ""
            new_pacchildren_state = []
            for pacchild_index in range(len(pacchildren)):
                action_name += f'P{pacchild_index + 1}_ {action[pacchild_index]}'
                new_pacchildren_state.append(self.decode(action[pacchild_index], pacchildren[pacchild_index]))

            collisions = self.check_collisions(new_pacchildren_state)
            if len(collisions) == 0 or (len(collisions) == 1 and collisions[0] == self.pacdad):
                new_food_state = self.new_food_state(new_pacchildren_state, food)
                successors[action_name] = (tuple(new_pacchildren_state), tuple(new_food_state), ghost)

        return successors

    # za sekoe dete pakman vo ovaa funkcija se presmetuvaat negovite sledni validni akcii
    def get_valid_actions(self, pacchild, food, ghost):
        actions = []
        remaining_food = sum(food)
        # vo slucaj da bide izedena hranata i da bide stignat deteto kaj tatkoto toa prestanuva da se dvizi,
        # odnosno se naogja vo goal state
        if remaining_food == 0 and pacchild == self.pacdad:
            return ['Goal']

        pac_x = pacchild[0]
        pac_y = pacchild[1]
        obstacles = list(self.obstacles)
        if remaining_food > 0:
            obstacles.append(self.pacdad)

        # gore
        up = (pac_x, pac_y + 1)
        if pac_y + 1 < self.grid_size_y and up not in obstacles and up != ghost:
            actions.append('Up')

        # dolu
        down = (pac_x, pac_y - 1)
        if pac_y - 1 >= 0 and down not in obstacles and down != ghost:
            actions.append('Down')

        # levo
        left = (pac_x - 1, pac_y)
        if pac_x - 1 >= 0 and left not in obstacles and left != ghost:
            actions.append('Left')

        # desno
        right = (pac_x + 1, pac_y)
        if pac_x + 1 < self.grid_size_x and right not in obstacles and right != ghost:
            actions.append('Right')

        return actions

    # ovaa funkcija gi kombinira validnite akcii od site k deca
    # "P1_Gore P2_Down P3_Down" - edna od nizata akcii
    def combine_actions(self, pacchildren, index):
        accumulator = []
        if index == len(pacchildren) - 1:
            for action in pacchildren[index]:
                accumulator.append([action])
            return accumulator

        for action in pacchildren[index]:
            for acc in self.combine_actions(pacchildren, index + 1):
                acc.insert(0, action)
                accumulator.append(acc)

        return accumulator

    # ako dete pakman e na isto pole so hrana togas nizata dobiva nula za konkretnoto pole vo sledniot state
    def new_food_state(self, pacchildren, food):
        new_food = list(food).copy()
        for pacchild in pacchildren:
            pidx = pacchild[1] * self.grid_size_x + pacchild[0]
            new_food[pidx] = 0

        return new_food

    # se izvrsuva na kraj, se proveruva dali ima dve ili povekje deca na isto pole, ako ima se ignorira akcijata
    def check_collisions(self, pacchildren):
        seen = set()
        dupes = []
        for pacchild in pacchildren:
            if pacchild in seen:
                dupes.append(pacchild)
            else:
                seen.add(pacchild)

        return dupes

    # pomosna funkcija za transformacija na akcija vo koordinata
    @staticmethod
    def decode(action, pacchild):
        pac_x = pacchild[0]
        pac_y = pacchild[1]
        if action == 'Up':
            return pac_x, pac_y + 1
        if action == 'Down':
            return pac_x, pac_y - 1
        if action == 'Left':
            return pac_x - 1, pac_y
        if action == 'Right':
            return pac_x + 1, pac_y

        return pacchild

if __name__ == '__main__':
    start_time = time.time()
    grid_size_x = 9
    grid_size_y = 6
    pacdad = (5, 4)
    ghost = (8, 1)
    pacbabies = ((0, 2), (3, 0))
    obstacles = ((0, 3), (0, 5), (2, 0), (3, 3), (4, 3), (4, 4), (5, 3), (6, 0), (6, 3), (6, 4), (8, 5))
    food = (
        1, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 0, 0,
        0, 0, 1, 0, 0, 0, 1, 1, 0,
        0, 1, 1, 0, 0, 0, 0, 1, 0,
        0, 1, 1, 1, 0, 0, 0, 1, 0,
        0, 0, 0, 1, 1, 1, 1, 1, 0
    )

    pacman = Pacman(grid_size_x, grid_size_y, obstacles, pacdad, (pacbabies, food, ghost))
    result = astar_search(pacman).solution()
    print(result)
    print(time.time() - start_time)

