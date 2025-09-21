'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def LCA(self, root, n1, n2):
        # your code here
        
        def dfs (node, val1, val2):
            if node == val1:
                return val1
            if node == val2:
                return val2
            if (node.data > val1.data and node.data < val2.data) or (node.data < val1.data and node.data > val2.data):
                return node
            if node.data > val1.data and node.data > val2.data:
                return dfs(node.left, val1, val2)
            if node.data < val1.data and node.data < val2.data:
                return dfs(node.right, val1, val2)
                
        return dfs(root,n1,n2)
        
        
    