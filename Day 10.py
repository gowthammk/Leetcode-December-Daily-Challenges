# Valid Mountain Array
# Given an array of integers arr, return true if and only if it
# is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < A[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Example 1:
#
# Input: arr = [2,1]
# Output: false
# Example 2:
#
# Input: arr = [3,5,5]
# Output: false
# Example 3:
#
# Input: arr = [0,3,2,1]
# Output: true

class Solution:
    def validMountainArray(self, arr):
        inc, dec = 1, 1
        if len(arr) < 3:
            return False
        for i in range(0, len(arr) - 1):
            if arr[i] < arr[i + 1]:
                inc += 1
                dec = 0
            if arr[i] == arr[i + 1]:
                inc = 0
                dec = 0
            elif arr[i] >= arr[i + 1]:
                dec += 1
        if (inc + dec) == len(arr):
            if inc == len(arr):
                return False
            if dec == len(arr):
                return False
            else:
                return True
        return False

