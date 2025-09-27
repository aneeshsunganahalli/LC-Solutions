from typing import List
from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        # Shoelace Formula
        max_area = 0
        for p1, p2, p3 in combinations(points, 3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
            max_area = max(max_area, area)

        return max_area
        
        # Intuitive with Heron's
        def distance(p1, p2):
            x1 = p1[0]
            x2 = p2[0]
            y1, y2 = p1[1], p2[1]

            d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            return d

        def areaFinder(d1,d2,d3):
            s = (d1 + d2 + d3) / 2

            area_squared = s*(s - d1)*(s - d2)*(s - d3)
            if area_squared <= 0:
                return 0
            return math.sqrt(area_squared)

        n = len(points)
        maxArea = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j+ 1, n):

                    d1 = distance(points[i], points[j])
                    d2 = distance(points[j], points[k])
                    d3 = distance(points[k], points[i])

                    area = areaFinder(d1,d2,d3)
                    maxArea = max(maxArea, area)
        return maxArea