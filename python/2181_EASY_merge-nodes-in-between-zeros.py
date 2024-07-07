from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res: ListNode = ListNode(0)
        pin: ListNode = res
        head = head.next
        while head is not None:
            if head.val == 0:
                if head.next:
                    res.next = ListNode(0)
                    res = res.next
            else:
                res.val += head.val
            head = head.next
        return pin


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_to_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


def list_to_linked_list(values: list) -> ListNode:
    if not values:
        return None
    head: ListNode = ListNode(values[0])
    current: ListNode = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


a: Solution = Solution()
test_cases: list[list] = [
    [
        [0, 3, 1, 0, 4, 5, 2, 0],
        [4, 11],
    ],
]
warn_list: list[str] = []


def testing(res, test) -> bool:
    if isinstance(test, (tuple, list, dict, str, int, float)):
        return res == test
    else:
        raise Exception("did not implement testing function for this class")


for test in test_cases:
    res: list = linked_list_to_list(a.mergeNodes(list_to_linked_list(test[0])))
    if not testing(res, test[-1]):
        warn_list.append(f"{test},{res}")
    else:
        print("_________________________________\n")
        print(
            test[:-1],
            res,
        )

print("=================================\n")
if warn_list:
    print("errors!!")
    for warn in warn_list:
        print(warn)
    print("_________________________________\n")
