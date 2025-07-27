class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (
                rec1[2] <= rec2[0] or  # rect1 left of rect2
                rec1[0] >= rec2[2] or  # rect 1 right of rect2
                rec1[3] <= rec2[1] or  # rect1 is below rect1
                rec1[1] >= rec2[3]  # rect1 is above rect2

        )
