# Time: O(N) 
#   where N is the number of nodes in the tree we will visit each node once to serialize and once to deserialize.
# Space: O(N)
#   We use a list to serialize the tree and use a list to deserialize the tree. 
from TreeNode import TreeNode
class Codec:
    # to serialize we will traverse the tree in preorder traversal 
    # we'll add strings of the values into a list 
    # for None values we'll use X 
    # after the list contains all nodes we will join the list in a comma separated string
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def buildList(root):
            if not root:
                result.append('X')
                return
            result.append(str(root.val))
            buildList(root.left)
            buildList(root.right)
        buildList(root)
        return ','.join(result)
            
    # to deserialize first we convert the string into a list
    # we'll use a local index variable to iterate through the list
    # then we will recursively build the nodes of the tree using a function
    # starting with the null check we check the first value in the list for X, increment the index value, and return None if necessary
    # We'll create a node using the integer value of the string and increment the index value
    # then we'll recursively build the nodes left and right child nodes per preorder traversal
    # we can return the node itself at the end of the function
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data.split(',')
        self.i = 0
        def buildTree():
            if preorder[self.i] == 'X' or preorder[self.i] == '':
                self.i+=1
                return None
            node = TreeNode(int(preorder[self.i]))
            self.i+=1
            node.left = buildTree()
            node.right = buildTree()
            return node
        root = buildTree()
        return root