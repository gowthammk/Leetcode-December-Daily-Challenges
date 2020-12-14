# Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
#
# A palindrome string is a string that reads the same backward as forward.
#
#
#
# Example 1:
#
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
#
# Input: s = "a"
# Output: [["a"]]

class Solution:
    def partition(self, s):
        self.res = []
        if len(s) > 16:
            return

        def palindrome(s):
            if s == s[::-1]:
                return s

        def dfs(s, path):
            if not s:
                self.res.append(path)
            else:
                for i in range(1, len(s) + 1):
                    if palindrome(s[:i]):
                        dfs(s[i:], path + [s[:i]])

        dfs(s, [])
        return self.res
