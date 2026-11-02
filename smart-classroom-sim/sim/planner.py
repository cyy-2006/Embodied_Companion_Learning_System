"""二维栅格 A* 路径规划（从原 Three.js PathPlanner 迁移，改为 Python/NumPy）。"""
import heapq
import math
from collections import deque

import numpy as np


def wrap_angle(angle):
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle < -math.pi:
        angle += 2 * math.pi
    return angle


class GridMap:
    def __init__(self, blocked, min_x, min_y, cell_size):
        self.blocked = np.asarray(blocked, dtype=bool)
        self.min_x = float(min_x)
        self.min_y = float(min_y)
        self.cell_size = float(cell_size)
        self.nx, self.ny = self.blocked.shape

    def world_to_cell(self, x, y):
        return int(math.floor((x - self.min_x) / self.cell_size)), int(
            math.floor((y - self.min_y) / self.cell_size)
        )

    def cell_to_world(self, ix, iy):
        return (
            self.min_x + (ix + 0.5) * self.cell_size,
            self.min_y + (iy + 0.5) * self.cell_size,
        )

    def inside(self, ix, iy):
        return 0 <= ix < self.nx and 0 <= iy < self.ny

    def is_blocked_cell(self, ix, iy):
        if not self.inside(ix, iy):
            return True
        return bool(self.blocked[ix, iy])

    def is_blocked_world(self, x, y):
        return self.is_blocked_cell(*self.world_to_cell(x, y))

    def nearest_free(self, ix, iy, max_cells=80):
        if not self.is_blocked_cell(ix, iy):
            return ix, iy
        queue = deque([(ix, iy)])
        seen = {(ix, iy)}
        while queue:
            cx, cy = queue.popleft()
            if not self.is_blocked_cell(cx, cy):
                return cx, cy
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                nx, ny = cx + dx, cy + dy
                if not self.inside(nx, ny) or (nx, ny) in seen:
                    continue
                if abs(nx - ix) > max_cells or abs(ny - iy) > max_cells:
                    continue
                seen.add((nx, ny))
                queue.append((nx, ny))
        return None

    def line_of_sight(self, a, b):
        x1, y1 = a
        x2, y2 = b
        distance = math.hypot(x2 - x1, y2 - y1)
        steps = max(2, int(math.ceil(distance / (self.cell_size * 0.5))))
        for i in range(steps + 1):
            t = i / steps
            if self.is_blocked_world(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t):
                return False
        return True

    def smooth(self, path):
        if len(path) <= 2:
            return path
        out = [path[0]]
        i = 0
        while i < len(path) - 1:
            j = len(path) - 1
            while j > i + 1 and not self.line_of_sight(path[i], path[j]):
                j -= 1
            out.append(path[j])
            i = j
        return out

    def plan(self, start, goal):
        """start/goal 为世界坐标 (x, y)，返回世界坐标路径或 None。"""
        s = self.world_to_cell(*start)
        g = self.world_to_cell(*goal)
        if self.is_blocked_cell(*g):
            return None
        if self.is_blocked_cell(*s):
            near = self.nearest_free(*s, max_cells=12)
            if near is None:
                return None
            s = near

        def heuristic(cell):
            return max(abs(cell[0] - g[0]), abs(cell[1] - g[1]))

        open_heap = [(heuristic(s), 0.0, s)]
        g_score = {s: 0.0}
        came_from = {}
        closed = set()
        directions = (
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1),
        )

        while open_heap:
            _, current_g, current = heapq.heappop(open_heap)
            if current in closed:
                continue
            if current == g:
                return self.smooth(self._reconstruct(came_from, current))
            closed.add(current)

            for dx, dy in directions:
                nxt = (current[0] + dx, current[1] + dy)
                if self.is_blocked_cell(*nxt) or nxt in closed:
                    continue
                if dx != 0 and dy != 0:
                    if self.is_blocked_cell(current[0] + dx, current[1]) or self.is_blocked_cell(
                        current[0], current[1] + dy
                    ):
                        continue
                step = 1.41421356 if dx != 0 and dy != 0 else 1.0
                tentative = current_g + step
                if tentative >= g_score.get(nxt, float("inf")):
                    continue
                came_from[nxt] = current
                g_score[nxt] = tentative
                heapq.heappush(open_heap, (tentative + heuristic(nxt), tentative, nxt))

        return None

    def _reconstruct(self, came_from, current):
        cells = [current]
        while current in came_from:
            current = came_from[current]
            cells.append(current)
        cells.reverse()
        return [self.cell_to_world(ix, iy) for ix, iy in cells]
