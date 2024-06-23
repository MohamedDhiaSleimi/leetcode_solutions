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
