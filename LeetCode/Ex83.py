class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None

        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next 
            else:
                current = current.next 

        return head




def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


# Example usage:
lst = [1, 1, 2]
head = create_linked_list(lst)

solution = Solution()
head = solution.deleteDuplicates(head)

# Print the result
print_linked_list(head)
