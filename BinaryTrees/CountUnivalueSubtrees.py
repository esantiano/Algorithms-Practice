# Time: O(N) 
#   We need to process all nodes in the subtree to determine the count of unival nodes
# Space: O(N)
#   All solutions are recursive, and require space equal to the amount of nodes in a tree.
# Notes:
#   A univalue subtree means all nodes have the same value: this includes leaves and technically null nodes.
#   All algorithms are DFS, we travel to each leaf and from those leaves the counts of unival nodes bubbles up.
#   Each algorithm uses the same structure but different ways of calculating the count.
# General algorithm pattern:
#   We use a recursive function that starts with a null check, then recurses on the left and right subtrees.
#   The function will returns a boolean value.
#   Updating the count depends on the results of the left and right recursive calls as well as the node values
#   
from TreeNode import TreeNode
from typing import Optional
class Solution:
#   In this solution we calculate the count within the recursive function and return the result as a tuple.
    def countUnivalSubtreesTuple(self, root: Optional[TreeNode]) -> int:
        
        def getCount(root):
            if not root:
                return True,0
            isLeftUni, lcount = getCount(root.left)
            isRightUni, rcount = getCount(root.right)
            count = lcount + rcount
            if isLeftUni and isRightUni:
                if root.left and root.left.val != root.val:
                    return False,count
                if root.right and root.right.val != root.val:
                    return False,count
                return True,count+1 # implies that either we have hit a leaf node or all nodes in the subtree share the same value    
            return False,count
        
        return getCount(root)[1]
    
#   In this solution the count is updated as a global value
    def countUnivalSubtreesGlobal(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def getCount(root):
            if not root:
                return True
            isLeftUni = getCount(root.left)
            isRightUni = getCount(root.right)
            if isLeftUni and isRightUni:
                if root.left and root.left.val != root.val:
                    return False
                if root.right and root.right.val != root.val:
                    return False
                self.count+=1
                return True            
            return False
        
        getCount(root)
        return self.count
# Here count is passed as a reference to the recursive function but it needs to be passed inside a list.
# For python if we pass a reference to an integer a copy of the integer is created and modified rather than the original instance.
# Remember that integers are immutable.
    def countUnivalSubtreesReference(self, root: Optional[TreeNode]) -> int:

        def getCount(root,count):
            if not root:
                return True
            isLeftUni = getCount(root.left,count)
            isRightUni = getCount(root.right,count)
            if isLeftUni and isRightUni:
                if root.left and root.left.val != root.val:
                    return False
                if root.right and root.right.val != root.val:
                    return False
                count[0]+=1
                return True            
            return False
        count = [0]
        getCount(root,count)
        return count[0]