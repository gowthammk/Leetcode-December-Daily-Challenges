# Swap Nodes in Pairs
#
# Solution
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes. Only nodes itself may be changed.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:
#
# Input: head = []
# Output: []
# Example 3:
#
# Input: head = [1]
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        dummy = p = ListNode(0)
        dummy.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            p.next = tmp
            head = head.next
            p = tmp.next
        return dummy.next