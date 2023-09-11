# source: https://adventofcode.com/2021/day/5
from dataclasses import dataclass
from typing import List

DEBUG = False

def log(msg):
    if DEBUG:
        print(msg)

@dataclass(frozen=True)
class Point:
    x: int
    y: int

class LineSegment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.start} -> {self.end}'

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_diagnal(self):
        res = abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y)
        return res

    def points(self):
        assert self.is_horizontal() or self.is_vertical() or self.is_diagnal()

        if self.end.x > self.start.x:
            dx = 1
        elif self.end.x < self.start.x:
            dx = -1
        else:
            dx = 0

        if self.end.y > self.start.y:
            dy = 1
        elif self.end.y < self.start.y:
            dy = -1
        else:
            dy = 0

        pt = self.start
        ret = []
        while 1:
            ret.append(pt)
            if pt == self.end:
                break
            pt = Point(x=pt.x + dx, y=pt.y + dy)

        return ret

def parse_line_to_segment(line: str) -> LineSegment:
    start, end = line.split('->')
    start_x, start_y = start.strip().split(',')
    end_x, end_y = end.strip().split(',')

    start_pnt = Point(x=int(start_x), y=int(start_y))
    end_pnt = Point(x=int(end_x), y=int(end_y))
    return LineSegment(start_pnt, end_pnt)

segments = []
with open('input', 'r') as f:
    for ln in f:
        if not ln:
            continue
        seg = parse_line_to_segment(ln)
        segments.append(seg)

class Diagram:
    def __init__(self, segments, with_diagnal=False):
        max_x, max_y = 0, 0
        for seg in segments:
            max_x = max(seg.start.x, seg.end.x, max_x)
            max_y = max(seg.start.y, seg.end.y, max_y)

        # build initial diagram
        self._diagram = self.initialize(max(max_x, max_y))

        # for every horizontal and vertical segments, draw the points
        self.draw_segments(segments, with_diagnal=with_diagnal)

    def pprint(self):
        if not DEBUG:
            return

        for idx, row in enumerate(self._diagram):
            row_lst = []
            for e in row:
                if not e:
                    row_lst.append('.')
                else:
                    row_lst.append(str(e))
            print(f"y{idx}: {''.join(row_lst)}")

    def initialize(self, max_val) -> List[List[int]]:
        ret = []
        for i in range(max_val + 1):
            row: List[int] = []
            for j in range(max_val + 1):
                row.append(0)
            ret.append(row)
        return ret

    def draw_segments(self, segments: List[LineSegment], with_diagnal=False):
        for seg in segments:
            if with_diagnal:
                if not seg.is_horizontal() and not seg.is_vertical() and not seg.is_diagnal():
                    log(f'seg {seg} invalid, continue')
                    continue
            else:
                if not seg.is_horizontal() and not seg.is_vertical():
                    continue

            log(f'draw_seg: {seg}')
            self.draw_points(seg.points())

    def draw_points(self, points: List[Point]):
        log(f'draw_points.., {points}')
        for point in points:
            self._diagram[point.y][point.x] += 1
        self.pprint()

    def count_points(self):
        """Count cells that value >= 2"""
        cnt = 0
        for row in self._diagram:
            for val in row:
                if val and val >= 2:
                    cnt += 1
        return cnt

diag = Diagram(segments, with_diagnal=False)
print(diag.count_points())      # 4826

diag = Diagram(segments, with_diagnal=True)
print(diag.count_points())      # 16793
