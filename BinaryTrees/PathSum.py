# Time: O(N) 
#   Each algorithm, recurisve or iterative uses this amount of time
#   to traverse each subtree from node to leaf to determine whether or not a solution exists.
# Space: O(N)
#   Each algorithm uses a stack explicit or implicit to process the nodes in the tree.
from typing import Optional
from TreeNode import TreeNode
class Solution:
# Algorithm:
#   For this recursive solution we include the current sum as a parameter to check whether or not we have a valid path to targetSum
#   When we hit a leaf node we compare the current sum to target sum.
#   We recursively call this helper function on the left and right subtrees of each node.
#   We also include a null check at the beginning.
    def hasPathSumRecursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def isValidPath(node,curSum):
            if not node:
                return False
            
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            left = isValidPath(node.left,curSum)
            right = isValidPath(node.right,curSum)
            
            return left or right
        
        return isValidPath(root,0)
    
# Algorithm:
#   The iterative solution follows the same pattern as the recursive except we use an explicit call stack 
#   starting with the root node.
#   To simulate the current sum parameter we create a set of the current node and its current sum.
#   The order in which we add the left and right subtrees to the stack does not matter.
    def hasPathSumIterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        nxt = [(root,root.val)]
        
        while nxt and nxt[-1]:
            cur,cur_sum = nxt.pop()
            if not cur.left and not cur.right and cur_sum == targetSum:
                return True

            if cur.right:
                nxt.append((cur.right,cur_sum+cur.right.val))
            if cur.left:
                nxt.append((cur.left,cur_sum+cur.left.val))
        
        return False