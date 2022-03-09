# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        node = head
        first_even_node = head.next
        last_odd_node = None
        last_even_node = None
        current_index = 1
        while node:
            if current_index %2 == 1:
                if last_odd_node:
                    last_odd_node.next = node
                last_odd_node = node
            else:
                if last_even_node:
                    last_even_node.next = node
                last_even_node = node
            current_index += 1
            node = node.next
        if last_even_node:
            last_even_node.next = None
        last_odd_node.next = first_even_node
        return head