class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x = min(ax2, bx2) - max(ax1, bx1) if max(ax1, bx1) < min(ax2, bx2) else 0
        y = min(ay2, by2) - max(ay1, by1) if max(ay1, by1) < min(ay2, by2) else 0
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - x * y
