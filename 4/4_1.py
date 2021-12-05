class Bingo_board():
    def __init__(self):
        self.board = []
        self.marked = []

    def add_row(self, row):
        if len(row) != 5:
            raise Exception("INVALID NUM per row!!!")
        self.board.append(row)

    def try_mark(self, num):
        for i in range(len(self.board)):
            if num in self.board[i]:  # try to mark num
                self.marked.append(num)
                return

    def get_winning_status(self):
        # check rows
        rc = 0
        cc = 0
        for row in self.board:
            rc = 0
            for cell in row:
                rc += 1 if cell in self.marked else 0
            if rc == 5:
                return True
        for cnum in range(5):
            cc = 0
            for c in [self.board[i][cnum] for i in range(5)]:
                cc += 1 if c in self.marked else 0
            if cc == 5:
                return True
        return False

    def board_sum(self):
        return sum([sum(self.board[i]) for i in range(len(self.board))])-sum(self.marked)


class Bingo():
    def __init__(self, filename):
        self.filename = filename
        self.rawinput = []
        self.random_nums = []
        self.boards = []

    def loadfile(self):
        f = open(self.filename, "r")
        raw = f.readlines()
        f.close()
        self.rawinput = raw

    def playbingo(self):
        for c, num in enumerate(self.random_nums):
            for board in self.boards:
                board.try_mark(num)  # try to mark num
                if board.get_winning_status() == True:
                    return board.board_sum()*num

    def processraw(self):
        # random nums
        self.random_nums = self.rawinput[0].split(",")
        self.random_nums = [int(x) for x in self.random_nums]
        # bingo boards
        i = 1
        new_board = False
        cur_board = None
        while(True):
            try:
                row = self.rawinput[i]
            except IndexError:
                self.boards.append(cur_board)
                break
            if row == '\n':  # new bingo board
                if(cur_board):
                    self.boards.append(cur_board)
                cur_board = Bingo_board()
            else:
                row = row.split(" ")
                int_row = []
                for x in row:
                    if x:
                        int_row.append(int(x))
                cur_board.add_row(int_row)
            i += 1
        if DEBUG:
            print(self.random_nums)


DEBUG = True
FILENAME = "./input.txt"
FILENAME2 = "./test.txt"

if __name__ == "__main__":
    B = Bingo(FILENAME)
    B.loadfile()
    B.processraw()
    print(B.playbingo())
