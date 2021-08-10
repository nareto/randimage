import random
import numpy as np


class BasePath(object):
    def __init__(self, mask) -> None:
        self.mask = mask
        self.mask_shape = mask.shape
        self.max_x, self.max_y = self.mask_shape[0] - 1, self.mask_shape[1] - 1

    def _get_square_neighboorhood(self, point, used_points):
        x, y = point
        cx, cy = self.mask_shape[0] - x, self.mask_shape[1] - y
        max_radius = max(x, cx, y, cy)
        out = set()
        radius = 1
        while not out:
            if radius >= max_radius:
                break
            left_line = [(max(0, x-radius),
                          max(0, min(y-radius + i, self.max_y))
                          ) for i in range(2*radius + 1)]
            right_line = [(min(self.max_x, x+radius),
                          max(0, min(y-radius + i, self.max_y))
                           ) for i in range(2*radius + 1)]
            top_line = [(max(0, min(x-radius + i, self.max_x)),
                         max(y-radius, 0)
                         ) for i in range(2*radius + 1)]
            bottom_line = [(max(0, min(x-radius + i, self.max_x)),
                            min(y+radius, self.max_y)
                            ) for i in range(2*radius + 1)]
            square_neighbors = set(
                left_line + right_line + top_line + bottom_line)
            out = square_neighbors.difference(used_points)
            radius += 1
        return out


class EPWTPath(BasePath):
    def get_path(self):
        x, y = random.randint(0, self.max_x), random.randint(0, self.max_y)
        cur_point = (x, y)
        out = [cur_point]
        used_points = {cur_point}
        while True:
            neighbors = self._get_square_neighboorhood(cur_point, used_points)
            if not neighbors:
                break
            mindiff = np.inf
            for neigh in neighbors:
                diff = np.abs(self.mask[cur_point] - self.mask[neigh])
                if diff < mindiff:
                    mindiff = diff
                    next_point = neigh
            out.append(next_point)
            used_points.add(next_point)
            cur_point = next_point
        return out

class ProbabilisticPath(BasePath):
    def get_path(self, rule=None):
        if rule is None: rule = bin(random.randint(0,2**12))[2:]
        x, y = random.randint(0, self.max_x), random.randint(0, self.max_y)
        cur_point = (x, y)
        out = [cur_point]
        used_points = {cur_point}
        while True:
            neighbors = self._get_square_neighboorhood(cur_point, used_points)
            if not neighbors:
                break
            neighbors = tuple(neighbors)
            weights = np.zeros(len(neighbors))
            for idx,n in enumerate(neighbors):
                weights[idx] = self.mask[n]
            next_point = random.choices(neighbors, weights=weights, k=1).pop()
            out.append(next_point)
            used_points.add(next_point)
            cur_point = next_point
        return out


PATHS = (EPWTPath,ProbabilisticPath)
