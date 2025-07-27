class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower_bound = float('-inf')

        for value in preorder:
            # If we find a value smaller than allowed lower bound, return False
            if value < lower_bound:
                return False

            # Pop all smaller ancestors (left subtree done), update lower_bound
            while stack and value > stack[-1]:
                lower_bound = stack.pop()

            stack.append(value)

        return True


"""
In a BST, for preorder traversal:

The first element is the root.

Then comes the left subtree elements, all less than root.

Then the right subtree elements, all greater than root.

When traversing preorder, whenever you encounter a value greater than the last popped root, 
that means you are now in the right subtree, 
so you must update the lower bound (minimum allowed value for the upcoming nodes).


Use a stack to simulate the path in BST preorder.

lower_bound tracks the smallest allowed value (to maintain BST property).

When the current value is greater than the top of the stack, 
it means we are moving from left subtree to right subtree:

Pop from stack and update lower_bound.

If any value violates the BST property by being less than lower_bound, return False.

"""