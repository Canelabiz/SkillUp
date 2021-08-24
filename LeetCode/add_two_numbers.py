# LeetCode - Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # sum = int("".join(str(d) for d in l1)[::-1]) + int("".join(str(d) for d in l2)[::-1])
        # return [int(d) for d in reversed(str(sum))]
        return l1.val


base = [1, 2, 3]
a = Solution.addTwoNumbers(base, base)
