from dataclasses import dataclass
from enum import Enum


class POSITION(Enum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3


@dataclass
class Point:
    x: int
    y: int


class Area:
    def __init__(self, bottomleft, topright):
        self.topright = topright
        self.bottomleft = bottomleft
        self.topleft = Point(bottomleft.x, topright.y)
        self.bottomright = Point(topright.x, bottomleft.y)

    def point_in_area(self, Point):
        if Point.x >= self.topleft.x and Point.x <= self.topright.x:
            if Point.y >= self.bottomleft.y and Point.y <= self.topleft.y:
                return True
        return False

    def getheight_pos(self, Point):
        if Point.y > self.topleft.y:
            return POSITION.TOP
        elif Point.y < self.bottomleft.y:
            return POSITION.BOTTOM
        return None

    def getlateral_pos(self, Point):
        if Point.x < self.topleft.x:
            return POSITION.LEFT
        elif Point.x > self.topright.x:
            return POSITION.RIGHT
        return None

    def point_in_Xarea(self, Point):
        if Point.x >= self.topleft.x and Point.x <= self.topright.x:
            return True
        return False

    def x_y_dist(self):
        return (self.topright.x, self.bottomleft.y)

# test1 = Point(10, -250)
# test2 = Point(51, -250)
# test3 = Point(10, -225)
# print(goal.point_in_area(test1))
# print(goal.point_in_area(test3))
# print(goal.point_in_area(test2))


def make_step(cur_pos, vx, vy):
    x, y = cur_pos.x, cur_pos.y
    x += vx
    y += vy
    vxnew = vx - vx/abs(vx) if vx != 0 else 0
    vynew = vy-1
    return (Point(x, y), vxnew, vynew)


def minx(xdist, goal):
    vmax = xdist
    pot_vx = []
    c = 0
    while True:
        Pos = Point(0, 0)
        vx = vmax-c
        while True:
            Pos, vx, _ = make_step(Pos, vx, 0)
            if goal.point_in_Xarea(Pos):
                pot_vx.append(vmax-c)
                break
            if vx == 0:
                break
        c += 1
        if vmax-c == 0:
            break
    return min(pot_vx)


def maxy(goal, vxmin):
    # get maxfall height through calc.
    # y = 0 10
    # y = 1 9
    # y = 2 7
    # y = 3 4
    # y = 4 0

    while True:
        vy = 0 if goal.topleft.y < 0 else goal.topleft.y
        vx = vxmin
        Pos = Point(0, 0)
        init_pos_height, init_pos_lat = goal.getheight_pos(
            Pos), goal.getlateral_pos(Pos)
        while True:  # throw ball
            Pos, vx, vy = make_step(Pos, vx, vy)
            new_height_pos, new_lat_pos = goal.getheight_pos(
                Pos), goal.getlateral_pos(Pos)  # get new relative positions


def find_highesty(goal):
    start = Point(0, 0)
    # get min x to reach goal
    xdist, ydist = goal.x_y_dist()
    vxmin = minx(xdist, goal)
    ymax = maxy(goal, vxmin)


# Area:
goal = Area(Point(10, -267), Point(50, -225))
goal = Area(Point(20, -10), Point(30, -5))
find_highesty(goal)
