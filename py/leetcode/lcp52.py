# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        """

        :param root:
        :param ops:
        :return:
        """
        ll = []
        self.iter(root, ll)
        m1= {}
        


    def iter(self, root, ll):
        if root is None:
            return
        if root.left:
            self.iter(root.left, ll)
        ll.append(root.val)
        if root.right:
            self.iter(root.right, ll)