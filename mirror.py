class TreeNode:
    
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Mirror:
    def mirror(self, root):
        if root != None:
            root.left, root.right = root.right, right.left
            self.Mirror(root.left)
            self.Mirror(root.right)
