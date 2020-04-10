# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 1
        linked_list = head
        while linked_list.next is not None:
            length += 1
            linked_list = linked_list.next

        for i in range(0, length // 2):
            head = head.next
        return head
