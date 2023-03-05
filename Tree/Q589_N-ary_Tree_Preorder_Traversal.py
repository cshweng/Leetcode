"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.root = root 
        if not root:
            return []
        else:
            self.L = [root.val]
            if len(root.children)==0:
                return self.L
            self.root_children = root.children
            return self.recursive(self.root_children, self.L)

    def recursive(self, root_children, L):
        for i in root_children:
            if len(i.children)!=0:
                L.append(i.val)
                self.recursive(i.children,L)
            else:
                L.append(i.val)
        return(L)
