class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)

        return stack


"""
 Intuition:
We use a stack to simulate the collision process.
Traverse the asteroids list
For each asteroid:
If it’s moving right (> 0) → push to stack
If it’s moving left (< 0) → check for possible collision with asteroids moving right on top of the stack
Collision logic:
If top of stack is positive (right-moving) and current is negative (left-moving) → collision
Compare sizes:
Smaller asteroid explodes
Equal size → both explode
If left-moving survives, check again with the new top of the stack

"""