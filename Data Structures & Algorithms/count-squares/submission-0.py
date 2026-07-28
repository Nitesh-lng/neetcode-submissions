from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), count in list(self.pts_count.items()):
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            
            res += count * self.pts_count.get((px, y), 0) * self.pts_count.get((x, py), 0)

        return res