# Time: O(N) we need to visit every node
# Space: 
# O(N): for the BFS solution we must use space for the queue.
# O(1): for the pointer solutions we only use space for the pointers.
from typing import Optional
from TreeNode import Node
from collections import deque
class Solution:
# Algorithm: 
#   For the BFS solution we visit every level in the tree to make the connections
#   Starting at the root we only process nodes at the current level within the q.
#   This is accomplished by getting the size of the q before creating the connections.
#   This algorithm works for perfect and imperfect trees
    def connectBFS(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if i < size-1:
                    cur.next = q[0]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root
# Algorithm:
#   This solution uses two pointers to create the connections
#   Starting at the root we create two pointers.
#   One to hold the position for the leftmost node in the level.
#   A second to make the connections. 
#   The first connection we make is between the two child nodes of the parent node.
#   We create a second connection between descendant nodes as we get deeper into the tree structure. 
#   Here we accomplish this by moving the pointer making connections between the nodes we have made connections for.
#   We repeat this process until we have reached the leftmost leaf node in the tree.
#   This algorithm only works for perfect trees.
    def connectPointer1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right # make the connection between the child nodes, which will allow us to travel between the nodes like in a linked list.
                if head.next: # after the connection is made we want to create connections between descendants(left childs right node and right childs left node).
                    head.right.next = head.next.left # its easier to make the connection between the inner nodes this way as we have a reference between the two parent nodes.
                head = head.next # move the head pointer to the next node.
            leftmost = leftmost.left
        
        return root
# Algorithm:
#   For this solution we use three pointers as well as a helper function.
#   The leftmost pointer starts at the root and only traverses to the leftmost nodes in the tree.
#   The curr pointer traverses all the nodes in the tree and is used to check for left and right children.
#   The prev pointer is used to make the connections between nodes. 
#   The helper function takes child nodes of the curr pointer, the prev pointer, and the leftmost pointer.
#   The purpose of the helper function is to create the connections between child nodes of a level, assigns the leftmost pointer (at most once) and reassigns the prev pointer.
#   This algorithm can be used for both perfect and imperfect trees.
    def connectPointer2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def makeConnection(child, prev, leftmost,):
            if child:
                if prev:
                    prev.next = child
                else:
                    leftmost = child
                prev = child
            return prev, leftmost
            
        if not root:
            return None
        leftmost = root
        while leftmost:
            curr = leftmost
            prev = None
            leftmost = None
            while curr:
                prev, leftmost = makeConnection(curr.left, prev, leftmost)
                prev, leftmost = makeConnection(curr.right, prev, leftmost)
                curr = curr.next
        return root
# Algorithm:
#   For this algorithm we use three pointers.
#   The head pointer starts at the root, enables connections between children to be made, and traverses the entire tree. 
#   Dummy is created as a node and is used to maintain reference to the head of the linked list so that the head pointer can travel to all nodes in the tree.
#   The temp pointer starts at the dummy node, is used to make the connections for the head nodes children, also traverses the entire tree.
#   We can use this algorithm for both perfect and imperfect trees.
    def connectPointer3(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        head = root
        while head:
            # initialize dummy node and temp pointer
            dummy = Node(0)
            temp = dummy

            while head: # we continue this loop until the head pointer reaches the end of the current level (None)
                # make connections in the next level down using temp 
                if head.left:
                    temp.next = head.left
                    temp=temp.next
                if head.right:
                    temp.next=head.right
                    temp=temp.next
                head=head.next
            
            # use the dummy node to move the head pointer to the next level to process. 
            head=dummy.next
        
        return root