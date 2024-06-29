from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        while list1 and list2:
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
        if not list1:
            return list2
        else:
            return list1


def list_to_linked_list(values: list) -> ListNode:
    if not values:
        return None
    head: ListNode = ListNode(values[0])
    current: ListNode = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


a: Solution = Solution()
test_cases: list[list] = [
    [
        [1, 2, 4],
        [1, 3, 4],
        [1, 1, 2, 3, 4, 4],
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: list = linked_list_to_list(
        a.mergeTwoLists(list_to_linked_list(test[0]), list_to_linked_list(test[1]))
    )
    print(
        test,
        "got",
        res,
        "=>",
        res == test[-1],
    )
    if not (res == test[-1]):
        warn_list.append(f"there is an error in {test}")

print("_________________________________\n")
if len(warn_list) > 0:
    for warn in warn_list:
        print(warn)
    print("_________________________________\n")
