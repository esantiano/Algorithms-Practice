# Time: O(N)
#   At the worst case we need to visit every node to confirm validity
# Space: O(N)
#   Whether explicitly or implicitly we use a stack to validate all the nodes
from typing import Optional
from TreeNode import TreeNode
class Solution:
    # Algorithm: 
    # For this algorithm we we use the inorder traversal and a variable to store the previously processed nodes value to validate the tree.
    # We initiate the prev variable to negative infinity.
    # We use the results of each recursive call to determine the validity of the overall tree.
    def isValidBSTPrevValRecursive(self, root: Optional[TreeNode]) -> bool:
        self.prev = float("-inf") # used to store all previously processed node values
        def isValidNode(root):
            if not root: # we can ignore null nodes
                return True
            if not isValidNode(root.left): # we can immediately return false if the left subtree is not valid
                return False
            if root.val <= self.prev: # check the node itself
                return False
            self.prev = root.val
            return isValidNode(root.right) # return the result of the recursive call on the right subtree
        
        return isValidNode(root)
    
    # The above is repeated here using the iterative approach. 
    def isValidBSTPrevValIterative(self, root: Optional[TreeNode]) -> bool:
        stack, prev = [], float("-inf")
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root <= prev:
                return False
            prev = root.val
            root = root.right
        return True
    
    # Algorithm
    # This approach uses min and max values to determine the validity of a BST. 
    # Each node value is compared to the min and max values for each node. 
    # If a nodes value falls outside of this range then it is considered an invalid node and therefore not a BST.
    def isValidBSTMinMaxRecursive(self, root: Optional[TreeNode]) -> bool:
        def isValidNode(root,low,high):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return isValidNode(root.left,low,root.val) and isValidNode(root.right,root.val,high)
        
        return isValidNode(root,float("-inf"),float("inf"))
    
    def isValidBSTMinMaxIterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root,float("-inf"),float("inf"))]
        while stack:
            cur, low, high = stack.pop()
            if not cur:
                continue
            if cur.val <= low or cur.val >= high:
                return False
            stack.append((cur.left,low,cur.val))
            stack.append((cur.right,cur.val,high))
        return True