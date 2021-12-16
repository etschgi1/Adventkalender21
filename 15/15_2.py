import numpy as np
from heapq import heappush, heappop, heapify
from dataclasses import dataclass


@dataclass(order=True)
class raw_Node:
    key: int
    val: any


class Node:
    def __init__(self, coords, weight, flag=None):
        self.coords = coords
        self.weight = weight
        self.flag = flag
        self.distance = 0 if flag == "start" else np.inf
        self.neighbours = []
        self.prevNode = []

    def __repr__(self):
        return f"{self.coords} - {self.weight} dist {self.distance}"

    def __lt__(self, other):
        return self.distance < other.distance

    def setpredecessor(self, prev_node):
        if self.prevNode != []:
            print("predecessor set more than once!")
        self.prevNode = prev_node

    def getpredecessor(self):
        return self.prevNode

    def setdistance(self, distance):
        self.distance = distance

    def getweight(self):
        return self.weight

    def getdistance(self):
        return self.distance

    def setprevNode(self, prevNode):
        self.prevNode = prevNode

    def getprevNode(self):
        return self.prevNode

    def get_coords(self):
        return self.coords

    def setNeighbours(self, neighbours):
        self.neighbours = neighbours

    def getNeighboursraw(self):
        return [(x.getweight(), x) for x in self.neighbours]


class dfs:
    def __init__(self, nodes, startnode, endnode, dimx, dimy):
        self.nodes = nodes
        self.rawnodes = []
        self.startnode = (startnode.getdistance(), startnode)
        self.endnode = (endnode.getdistance(), endnode)
        self.dimx, self.dimy = dimx, dimy
        self.link_nodes()
        self.populaterawnodes()
        self.heap = []
        heappush(self.heap, self.startnode)
        self.dijkstra()
        # self.minpath_search(startpos, endpos)

    def populaterawnodes(self):
        for node in self.nodes.values():
            self.rawnodes.append((node.getweight(), node))

    def link_nodes(self):
        for coords, data in self.nodes.items():
            top, left, bottom, right = None, None, None, None
            x, y = coords
            if x > 0:  # got left neighbour
                left = (x-1, y)
            if x < self.dimx:  # got right neighbour
                right = (x+1, y)
            if y > 0:  # got top neighbour
                top = (x, y-1)
            if y < self.dimy:  # get bottom neighbour
                bottom = (x, y+1)
            self.nodes[coords].setNeighbours(
                [self.nodes[x] for x in [top, left, bottom, right] if x != None])

    def dijkstra(self):
        # init
        last_node = None
        while self.heap:
            toprint = [x[1] for x in self.heap]
            # for p in toprint:
            #     print(p, end="")
            #     print(p.getpredecessor())
            next_node_raw = heappop(self.heap)
            next_node = next_node_raw[1]
            if next_node.coords == (3, 2):
                print("as")
            if next_node.flag == "end":
                last_node = next_node
                break
            neighbours_raw = next_node.getNeighboursraw()
            neighbours = [x[1] for x in neighbours_raw]
            for neighbour in neighbours:
                if neighbour.getdistance() > (next_node.getdistance() + neighbour.getweight()):
                    neighbour.setdistance(
                        next_node.getdistance() + neighbour.getweight())
                    neighbour.setpredecessor(
                        next_node.getpredecessor()+[next_node])
                    print(f"add - {neighbour.coords} - {neighbour.weight}")
                    heappush(self.heap, (neighbour.getdistance(), neighbour))
                    heapify(self.heap)
        print("Done, distance to last: ", end="")
        print(last_node.getdistance())
        print("Path:")
        sum_ = 0
        for prev in last_node.getpredecessor():
            sum_ += prev.weight
            print(f"{prev.weight} - {prev.coords}")
        print("Done, distance to last: ", end="")
        print(last_node.getdistance())


def create_large_map(map_):
    dimx, dimy = len(map_[0])-1, len(map_)-1
    dimx, dimy = ((dimx+1)*5)-1, ((dimy+1)*5)-1
    print(map_, dimx, dimy)
    # gen firstrow
    for pos, row in enumerate(map_):
        for i in range(5-1):  # gen 4 new to right
            to_right = [x+1 if x < 9 else 1 for x in row]
            map_[pos] += to_right
    origrows = len(map_)
    # gen rows down:
    for i in range(5-1):  # gen 4 left down
        for rownum in range(i*origrows, i*origrows+origrows):
            to_insert = [x+1 if x < 9 else 1 for x in map_[rownum]]
            map_.append(to_insert)
    # ugly map:
    ugly_map = []
    for y, line in enumerate(map_):
        ugly_map.append([((c, y), int(x), 1000000000)
                        for c, x in enumerate(line)])
    # print(ugly_map)
    return (np.array(ugly_map), dimx, dimy)


def main(map_):
    map_, dimx, dimy = create_large_map(map_)
    # dimx, dimy = map_[-1][-1][0] #! add later
    Nodes = {}
    for row in map_:
        for element in row:
            if element[0] == (0, 0):
                node = Node(element[0], element[1], "start")
                startnode = node
            elif element[0] == (dimx, dimy):
                node = Node(element[0], element[1], "end")
                endnode = node
            else:
                node = (Node(element[0], element[1]))
            Nodes[element[0]] = node
    search = dfs(Nodes, startnode, endnode, dimx, dimy)
    # print(search.start, search.end)


FILENAME2 = "./test.txt"
FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    input_ = f.readlines()
    f.close()
    input_ = [x.strip("\n") for x in input_]
    map_ = []
    for y, line in enumerate(input_):
        map_.append([int(x) for x in line])
        #map_.append([((c, y), int(x), 1000000000) for c, x in enumerate(line)])
    main(map_)
