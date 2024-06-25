class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_in_order_traversal(node: TreeNode, acc_sum: int) -> int:
            if not node:
                return acc_sum
            acc_sum: int = reverse_in_order_traversal(node.right, acc_sum)
            node.val += acc_sum
            acc_sum = node.val
            acc_sum = reverse_in_order_traversal(node.left, acc_sum)
            return acc_sum

        reverse_in_order_traversal(root, 0)
        return root
