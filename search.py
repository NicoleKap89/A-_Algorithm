from search_node import search_node
from heapq import heapify, heappush, heappop, heappushpop

def create_open_set():
    heap = []
    dict = {}
    return (heap, dict)


def create_closed_set():
    dict = {}
    return dict


def add_to_open(vn, open_set):
    heappush(open_set[0], vn)
    open_set[1][vn.state.get_state_str()] = vn


def open_not_empty(open_set):
    return len(open_set[0]) != 0


def get_best(open_set):
    return heappop(open_set[0])


def add_to_closed(vn, closed_set):
    closed_set[vn.state.get_state_str()] = vn


#returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
#remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    return vn.state.get_state_str() in open_set[1] and vn.g >= open_set[1][vn.state.get_state_str()].g


#returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
#remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    return vn.state.get_state_str() in closed_set and vn.g >= closed_set[vn.state.get_state_str()].g

def print_path(path):
    for i in range(len(path)-1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic, goal_state):

    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if current.state.get_state_str() == goal_state:
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None




