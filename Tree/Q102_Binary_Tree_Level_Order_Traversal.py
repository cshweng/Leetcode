# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results
        
        from collections import deque
        que = deque([root])
        
        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root, depth):
            if not root: return []
            if len(res) == depth: res.append([]) # start the current depth
            res[depth].append(root.val) # fulfil the current depth
            if  root.left: helper(root.left, depth + 1) # process child nodes for the next depth
            if  root.right: helper(root.right, depth + 1)
        helper(root, 0)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.root = root
        if root == None:
            return []
        self.L = [[root.val]]
        if self.root.left==None and self.root.right==None:
            return self.L
        return self.recurcive([self.root], self.L)
    def recurcive(self, root, L):
        S = []
        for i in root:
            if i and i.left != None:
                S.append(i.left)
            if i and i.right != None:
                S.append(i.right)
        if len(S)>0:
            L.append(map(lambda x: x.val, S))
            return self.recurcive(S,L)
        return L
