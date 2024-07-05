# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import *


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        cPI: list[int] = []  # criticalPointIndex
        cache: list[int] = []
        i: int = -2
        while head != None:
            i += 1
            cache.append(head.val)
            if len(cache) > 3:
                cache.pop(0)
            if len(cache) == 3:
                if (cache[1] > cache[0] and cache[1] > cache[2]) or (
                    cache[1] < cache[0] and cache[1] < cache[2]
                ):
                    cPI.append(i)
            head = head.next
        if len(cPI) < 2:
            return [-1, -1]
        maxDistance: int = cPI[-1] - cPI[0]
        minDistance: int = maxDistance
        for i in range(1, len(cPI)):
            if cPI[i] - cPI[i - 1] < minDistance:
                minDistance = cPI[i] - cPI[i - 1]
        return [minDistance, maxDistance]


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
]
warn_list: list[str] = []


def testing(res, test) -> bool:
    if isinstance(test, (tuple, list, dict, str, int, float)):
        return res == test
    else:
        raise Exception("did not implement testing function for this class")


for test in test_cases:
    res: bool = a.nodesBetweenCriticalPoints(list_to_linked_list(test[0]))
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
