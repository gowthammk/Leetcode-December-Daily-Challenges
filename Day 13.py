# Burst Balloons
#
# Solution
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
class Solution:
    def maxCoins(self, A: List[int]) -> int:
        @functools.lru_cache(None)
        def f(l, r):  # balloon l+1 ~ r-1 are all burst
            if l + 1 >= r: return 0
            return max(f(l,i) + f(i,r) + A[l]*A[i]*A[r] for i in range(l+1, r))
        A.append(1)  # make A[-1] and A[n] equals to 1
        return f(-1, len(A)-1)