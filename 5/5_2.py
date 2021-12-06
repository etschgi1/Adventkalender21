class Point:
    def __init__(self, x, y):
        self.x_ = int(x)
        self.y_ = int(y)

    def y(self):
        return self.y_

    def x(self):
        return self.x_


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.created = False
        self.points = []
        self.init_points()

    def get_xymax(self):
        xmax = max([i.x() for i in self.points])
        ymax = max([i.y() for i in self.points])
        return (xmax, ymax)

    def getpoints(self):
        return self.points

    def init_vertical(self):
        distance = abs(self.start.y()-self.end.y())
        if self.start.x() > self.end.x():
            start, end = self.end, self.start
        else:
            start, end = self.start, self.end
        # start bottom-leftmost
        if end.y() < start.y():
            for i in range(distance):
                self.points.append(Point(start.x()+i, start.y()-i))
        else:
            for i in range(distance):
                self.points.append(Point(start.x()+i, start.y()+i))
        if self.start.x() != self.end.x() and self.start.y() != self.end.y():
            self.points.append(end)
        self.created = True

    def init_points(self):
        xFlag = False
        if self.start.x() == self.end.x():
            xFlag = True
        elif self.start.y() == self.end.y():
            xFlag = False
        else:
            self.init_vertical()
            return
        distance = 0
        if xFlag:  # same x
            distance -= self.start.y()-self.end.y()
        else:  # same y
            distance -= self.start.x()-self.end.x()
        for i in range(abs(distance)):
            i = i if distance >= 0 else -i
            if xFlag:
                self.points.append(Point(self.start.x(), self.start.y()+i))
            else:
                self.points.append(Point(self.start.x()+i, self.start.y()))
            # add end
        if self.start.x() != self.end.x() or self.start.y() != self.end.y():
            self.points.append(self.end)
        self.created = True


class Board:
    def __init__(self, filename):
        self.f = filename
        self.rawdata = []
        self.lines = []
        self.gameboard = []
        self.hashmap = {}
        self.load_data()
        self.create_lines()
        self.init_gameboard()

    def load_data(self):
        f = open(self.f, "r")
        self.rawdata = f.readlines()
        f.close()

    def create_lines(self):
        for l in self.rawdata:
            start, end = l.split(" -> ")
            startx, starty = start.split(",")
            endx, endy = end.split(",")
            startpoint = Point(startx, starty)
            endpoint = Point(endx, endy)
            line = Line(startpoint, endpoint)
            if line.created:
                self.lines.append(line)

    def init_gameboard(self):
        xmax, ymax = 0, 0
        for l in self.lines:
            x, y = l.get_xymax()
            xmax = x if x > xmax else xmax
            ymax = y if y > ymax else ymax
        self.gameboard = [[0]*(xmax+1)]*(ymax+1)
        # populate
        for l in self.lines:
            points = l.getpoints()
            for point in points:
                val = f"{point.x()}-{point.y()}"
                if PRINT:
                    print(val)
                try:
                    self.hashmap[val] += 1
                except KeyError:
                    self.hashmap[val] = 1
            # x_, y_ = [i.x() for i in l.points], [i.y() for i in l.points]
            # for x, y in zip(x_, y_):
            #     print(x, y)
            #     self.gameboard[y] = [i if c != x else i +
            #                          1 for c, i in enumerate(self.gameboard[y])]

    def get_higher2(self):
        vals = self.hashmap.values()
        c = 0
        for val in vals:
            c = c+1 if val >= 2 else c
        return c

    def print_gameboard(self):
        for x in range(len(self.gameboard[0])):
            for y in range(len(self.gameboard)):
                pos = f"{y}-{x}"
                try:
                    val = self.hashmap[pos]
                except KeyError:
                    val = "."
                print(val, end="")
            print("")

PRINT=False
FILENAME = "./input.txt"
FILENAME2 = "./test.txt"
B = Board(FILENAME)
B.print_gameboard()
print(f"Higher than 2: {B.get_higher2()}")
