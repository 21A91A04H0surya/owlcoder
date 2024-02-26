class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both nodes are None
        if not p and not q:
            return True
        # If only one of the nodes is None or their values are not equal
        if not p or not q or p.val != q.val:
            return False
        # Recur for left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
