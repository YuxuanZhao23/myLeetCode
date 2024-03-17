# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = curr = ListNode()
        while l1 or l2 or carry != 0:
            num = carry
            if l1: num += l1.val
            if l2: num += l2.val
            num, carry = num%10, num//10
            if l1:
                curr.next = l1
                l1.val = num
            elif l2:
                curr.next = l2
                l2.val = num
            else:
                curr.next = ListNode(num)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next