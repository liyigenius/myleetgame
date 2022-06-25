# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """

        :param nums:
        :return:
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        max1 = max(nums)
        idx1 = nums.index(max1)
        n1 = TreeNode(max1)
        sub1 = self.constructMaximumBinaryTree(nums[:idx1])
        sub2 = self.constructMaximumBinaryTree(nums[idx1+1:])
        n1.left = sub1
        n1.right = sub2
        return n1