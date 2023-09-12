# source: https://adventofcode.com/2021/day/4
from typing import List, Dict

class Board:
    def __init__(self, name, rows: List[List[int]]):
        self.name = name
        self._board = []
        for row in rows:
            self._board.append([[num, False] for num in row])

    def __str__(self):
        return self.name

    @property
    def rows(self):
        return self._board

    @property
    def cols(self):
        ret = []
        for j in range(5):
            col = []
            for i in range(5):
                col.append(self._board[i][j])
            ret.append(col)
        return ret

    def draw_at(self, row, col):
        # print(f'draw at {row}, {col}')
        ele = self._board[row][col]
        ele[1] = True

    def all_drawn(self, row_or_col):
        return all([e[1] for e in row_or_col])

    def is_win(self):
        for row in self.rows:
            if self.all_drawn(row):
                return True

        for col in self.cols:
            if self.all_drawn(col):
                return True

        return False

    def score(self, num):
        marked, unmarked = [], []
        for row in self.rows:
            for a_num in row:
                if a_num[1] is True:
                    marked.append(a_num[0])
                else:
                    unmarked.append(a_num[0])
        # print(sum(marked), sum(unmarked))
        return num * sum(unmarked)

def parse_nums_from_input(lines) -> List[int]:
    return [int(e) for e in lines[0].split(',')]

def parse_boards_from_input(lines) -> List[Board]:
    start, next = 0, 5

    data = lines[1:]
    end = len(data)
    boards = []
    i = 1
    while start < end:
        rows = []
        for e in data[start: next]:
            e = e.strip()
            row = []
            for num in e.split(' '):
                if not num:
                    continue
                row.append(int(num))
            rows.append(row)
        b = Board(f'b{i}', rows)
        i += 1
        boards.append(b)
        start += 5
        next += 5
    return boards

def build_num_board_info(boards: List[Board]):
    """"""
    # 22 -> [(b0, 0, 0), (b1, 0, 4)]
    # 13 -> [(b0, 0, 1), (b3, 3, 2)]
    dic: Dict[int, List] = {}
    for a_board in boards:
        for i, row in enumerate(a_board.rows):
            for j, a_num in enumerate(row):
                num = a_num[0]
                if num not in dic:
                    dic[num] = []
                dic[num].append((a_board, i, j))
    return dic

# --------------------
lines = []
with open('./input') as f:
    for ln in f.readlines():
        ln = ln.strip()
        if not ln:
            continue
        lines.append(ln)
assert len(lines[1:]) % 5 == 0

nums = parse_nums_from_input(lines)
boards = parse_boards_from_input(lines)
num_board_info = build_num_board_info(boards)

def first_win():
    for num in nums:
        for e in num_board_info.get(num, []):
            board, r, c = e
            board.draw_at(r, c)
            if board.is_win():
                print(f'first win. place {num} at board {board}')   # 14
                print(board.score(num))  # 12796
                return

first_win()

# --------------------
def last_win():
    win_boards = set()
    len_boards = len(boards)
    for num in nums:
        for e in num_board_info.get(num, []):
            board, r, c = e
            board.draw_at(r, c)
            if board.is_win():
                win_boards.add(board)
                if len(win_boards) == len_boards:
                    print(f'last win. place {num} at board {board}')  # 81
                    print(board.score(num))  # 18063
                    return

last_win()
