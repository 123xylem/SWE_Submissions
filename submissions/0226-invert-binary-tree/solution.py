class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive function that switches the left and right of each Node  
        # Then Drills down to next Left,Right node to do it again.
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
