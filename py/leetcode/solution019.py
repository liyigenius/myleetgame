# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        m = {}
        if head == None:
            return head
        if head.next == None:
            return None
        cnt = 0
        while head:
            m[cnt] = head
            head = head.next
            cnt += 1
        rm = m[cnt - n]
        if cnt - n - 1 < 0:
            return m[1]
        prev = m[cnt - n - 1]
        tmp = rm.next
        prev.next = tmp
        return m[0]