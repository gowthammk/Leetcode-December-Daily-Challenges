# Next Greater Element III
#
# Solution
# Given a positive integer n, find the smallest integer which has exactly the same digits
# existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.
#
# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but
# it does not fit in 32-bit integer, return -1.
#
#
#
# Example 1:
#
# Input: n = 12
# Output: 21
# Example 2:
#
# Input: n = 21
# Output: -1

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = [int(i) for i in str(n)]
        for i in range(2, len(n) + 1):
            b, f = 1, n[-i]
            for j in range(1, 10 - f):
                if f + j in n[-i + 1:]:
                    b = 0
                    break
            if b == 1: continue
            n[n.index(f + j, -i)], n[-i] = f, f + j
            n[-i + 1:] = sorted(n[-i + 1:])
            n = int("".join([str(i) for i in n]))
            return n if n < 2 ** 31 else -1
        return -1

