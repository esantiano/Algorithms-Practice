# Time: O(N)
#   At worst we will have to check all nodes to determine the LCA of p and q.
# Space: O(N)
#   At worst we will have to use space on a stack or stack and dictionary to determine the LCA of p and q.
from TreeNode import TreeNode
class Solution:
# Algorithm:
#   This algorithm uses a recursive DFS post order traversal to check nodes. PostOrder traversal -> Left, Right, Root
#   Starting at the root node we will travel down to each leaf node in the tree and will either return one of the found nodes or null.
#   The recursive function starts with a null check.
#   Then we recurse on the left and right children of the current node and capture the returned values.
#   After the recursive calls we can check the following conditions:
#   If both the left and right variables return nodes we can conclude that the current root node is the LCA of both p and q.
#   If the current root node matches either p or q we can return it.
#   If neither of the above conditions have been met we can expect either the left or right children to return one of the nodes. (Either None or nodes p or q will bubble up from the recursive call.)
    def lowestCommonAncestorRecursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def checkRoot(root):
            if not root:
                return None
            
            left = checkRoot(root.left)
            right = checkRoot(root.right)
            if (left and right) or root == p or root == q:
                return root
            return left or right
        
        return checkRoot(root)

# Algorithm:
#   For this solution we use a stack, dictionary of nodes and parent nodes, and a set to help us determine the LCA of p and q.
#   Starting at the root node we iteratively build a dicionary of nodes and their parent nodes until the dictionary contains the ndoes p and q. (key:value = childNode:parentNode)
#   Once the dictionary contains p and q we can start building our ancestors set. 
#   Using the dicionary we add all ancestors of the node p to the set including p itself. We will also update the pointer p using the dictionary. (We continue doing this until p points to None. Eventually p will be updated to the original root node whose parent is None)
#   After adding all ancestors of the node p to the set we can use the dictionary to search for node q's ancestor. We will also update the pointer q using the dictionary. (At this point the LCA will be inside the set. We continue doing this until q points to one of the nodes in the set which will be the LCA.)
#   After updating the pointer q it will be pointing to the LCA. 
    def lowestCommonAncestorIterativeDictionary(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        
        return q