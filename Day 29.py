# Pseudo-Palindromic Paths in a Binary Tree
#
# Solution
# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be
# pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
#
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
#
#
#
# Example 1:
#
#
#
# Input: root = [2,3,1,3,1,null,1]
# Output: 2
# Explanation: The figure above represents the given binary tree. There are three paths going from the root
# node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths
# only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in
# [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
# Example 2:
#
#
#
# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1
# Explanation: The figure above represents the given binary tree. There are three paths going from
# the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1].
# Among these paths only the green path is pseudo-palindromic since [2,1,1] can be
# rearranged in [1,2,1] (palindrome).
# Example 3:
#
# Input: root = [9]
# Output: 1
#
#
# Constraints:
#
# The given binary tree will have between 1 and 10^5 nodes.
# Node values are digits from 1 to 9.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def bfs(stack, root):
            count = 0
            if not root:
                return 0
            stack.append(root.val)
            if root.left == None and root.right == None:
                occurrences = collections.Counter(stack)
                for _, value in occurrences.items():
                    if value % 2 != 0:
                        count += 1
                if (count == 0) or (count == 1):
                    self.sum_ += 1
            bfs(stack, root.left)
            bfs(stack, root.right)
            stack.pop()

        self.sum_ = 0
        bfs([], root)
        return (self.sum_)
