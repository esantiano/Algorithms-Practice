# Time: O(N)
#   We use this time to build the dictionary (, the deque,) and the nodes for the tree.
# Space: O(N)
#   We need this space for the inorder index dictionary(, preorder deque,) and call stack to build the nodes.
# Notes: Preorder traversal: Root -> Left -> Right
# Algorithm: 
#   This algorithm is similar to the postorder approach however instead of taking values from the end we take from the beginning of the preorder list.
#   We also recursively build the left and then the right subtrees according to the preorder traversal order.
#   There are two approaches we can take when getting the value from the preorder list:
#   We can create a deque of the preorder list and popleft().
#   We can create a global variable for the starting index of the preorder list and increment it every time we create a new node.
from collections import deque
from typing import List, Optional
from TreeNode import TreeNode
class Solution:
    def buildTreeDeque(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i,val in enumerate(inorder):
            indices[val]=i
        
        pre = deque()
        for val in preorder:
            pre.append(val)
            
        def buildNode(start,end):
            if start > end:
                return None
            
            newNode = TreeNode(pre.popleft())
            rootIdx = indices[newNode.val]
            
            newNode.left = buildNode(start,rootIdx-1)
            newNode.right = buildNode(rootIdx+1,end)
            
            return newNode
        
        return buildNode(0,len(inorder)-1)
    
    def buildTreeIndex(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i,val in enumerate(inorder):
            indices[val]=i
        self.preIdx = 0
        def buildNode(start,end):
            if start > end:
                return None
            
            newNode = TreeNode(preorder[self.preIdx])
            self.preIdx+=1
            rootIdx = indices[newNode.val]
            
            newNode.left = buildNode(start,rootIdx-1)
            newNode.right = buildNode(rootIdx+1,end)
            
            return newNode
        
        return buildNode(0,len(inorder)-1)