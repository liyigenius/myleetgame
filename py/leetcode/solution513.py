# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """

        :param root:
        :return:
        """
        ll = []
        self.iter(root, ll)
        res = ll[0]
        return res

    def iter(self, root, ll):
        if not root:
            return

        self.iter(root.left, ll)
        ll.append(root.val)
        self.iter(root.right, ll)

