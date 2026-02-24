from TreeNode import TreeNode
from typing import Optional
class Solution:
    # Time: O(N)
    #   Worst case we must check all nodes, best case we only need to check half the nodes in the tree
    # Space: O(1)
    # Algorithm:
    #   In this solution we utilize the structure of the binary search tree to determine which subtrees to check for the successor node.
    #   Given a node p we can compare its value against the root node value and eliminate half the nodes based on the comparison. 
    #   If we encounter a node that has a greater value than p's we can consider it a possible successor and traverse its left subtrees for other possibilities.
    def inorderSuccessorBST(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if p.val <= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
    # Time: O(N)
    #   Worst case we must check all the nodes. (Skewed BST)
    # Space: O(N)
    #   We may need to use space on the call stack for all the nodes.
    # Algorithm:
    #   This solution can be used for both BSTs and BTs. It involves looking at two cases
    #   In the first case we consider that the node p has a right subtree. 
    #   For this case we travel down to the leftmost node in the right subtree which should be p's successor node.
    #   For the second case we consider that p does not have a right subtree and therefore the successor node is an ancestor of p.
    #   In this case we perform an inorder search until we have encountered p and begin processing the next node which will be the successor node.
    def inorderSuccessorGeneral(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.successor = None
        self.prev = None

        def inorderSearch(root,p):
            if not root:
                return None
            inorderSearch(root.left,p)
            if self.prev == p and not self.successor:
                self.successor = root
                return
            self.prev = root
            inorderSearch(root.right,p)

        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left
            self.succcessor = leftmost
        else:
            inorderSearch(root,p)
        return self.successor