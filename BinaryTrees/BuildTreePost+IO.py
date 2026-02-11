# Time: O(N) 
#   In order to build each node we must process all the elements within the postorder list.
# Space: O(N)
#   Here we use space for the dictionary of indices for the inorder list and on the call stack to build each node in the tree.
# Notes: Postorder travel -> Left, Right, Root. Inorder travel -> Left, Root, Right
# Algorithm:
#   We use a dictionary to map values and their indices within the inorder list.
#   These indices will be used to determine which subtree we are building.
#   Using a recursive function we build each node of the tree using the values from the postorder list.
#   We build a node using the last value of the postorder list. (root values are the last values within the list as defined by the travel order)
#   We'll use the indice from the inorder list to determine the inorder list boundaries of the left and right subtrees of the node. (the inorder list gives us the closest structural approximation of the resulting tree, it will tell us when we have reached a leaf ndoe)
#   The boundaries help us determine when we have reached a leaf node. (base case)
#   Starting from the beginning to the last indexes of the inorder list we'll recursively build the right and left nodes. (reverse of postorder travel)

from typing import List, Optional
from TreeNode import TreeNode
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i,val in enumerate(inorder):
            indices[val] = i
        
        def buildNode(start,end):
            if start > end:
                return None
            
            newNode = TreeNode(postorder.pop())
            root_ind = indices[newNode.val]
            
            newNode.right = buildNode(root_ind+1,end)
            newNode.left = buildNode(start,root_ind-1)
            
            return newNode
        
        return buildNode(0,len(inorder)-1)