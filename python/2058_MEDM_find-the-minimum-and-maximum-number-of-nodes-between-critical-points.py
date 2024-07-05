from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev: ListNode = head
        curr: ListNode = head.next
        next: ListNode = head.next.next
        index: int = 1
        first: int | None = None
        last: int | None = None
        minDistance: int | None = 99999999
        number: int = 0
        while next:
            if (curr.val > next.val and curr.val > prev.val) or (
                curr.val < next.val and curr.val < prev.val
            ):
                number += 1
                if first is None:
                    first = index
                else:
                    minDistance = min(minDistance, index - last)
                last = index
            index += 1
            prev, curr, next = curr, next, next.next
        if number < 2:
            return [-1, -1]
        else:
            return [minDistance, last - first]


def linked_list_to_list(head: ListNode) -> list:
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
        [5, 3, 1, 2, 5, 1, 2],
        [1, 3],
    ],
    [
        [4, 2, 4, 1],
        [1, 1],
    ],
]
warn_list: list[str] = []


def testing(res, test) -> bool:
    if isinstance(test, (tuple, list, dict, str, int, float)):
        return res == test
    else:
        raise Exception("did not implement testing function for this class")


for test in test_cases:
    res: list[int] = a.nodesBetweenCriticalPoints(list_to_linked_list(test[0]))
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
