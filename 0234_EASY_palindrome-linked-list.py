class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        temp: list = []
        while head:
            temp.append(head.val)
            head = head.next
        return temp == temp[::-1]
