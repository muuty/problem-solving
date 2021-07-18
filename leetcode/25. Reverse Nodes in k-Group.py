# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy_start = ListNode(0)
        dummy_start.next = head
        current_node = head
        count = 0
        reverse_start = head
        left = dummy_start
        while current_node != None:
            count += 1
            current_node = current_node.next


            if count % k == 0:
                prev, cur = reverse_start, reverse_start.next
                r = current_node
                for _ in range(k-1):
                    temp = cur.next
                    cur.next = prev
                    print(cur.val , "->" , cur.next.val)
                    prev = cur
                    cur = temp
                reverse_start.next = current_node
                left.next = prev
                print("left connect :", left.val, "->", left.next.val)
                print("right connect : ", reverse_start.val, "-> ", reverse_start.next.val)

                left = reverse_start
                reverse_start = reverse_start.next
                #print("new_reverse_start : ", reverse_start.val)


        print_nodes(dummy_start.next)
        return dummy_start.next

def print_nodes(head_node):
    node = head_node
    val_list = []
    count = 0
    while node != None and count < 10:
        val_list.append(node.val)
        node = node.next
        count += 1
    print(val_list)

def node_init(val_list):
    prev_node = None
    node_start = None
    for i in val_list:
        cur_node = ListNode(i)
        if i == val_list[0]:
            node_start = cur_node
        if prev_node != None:
            prev_node.next = cur_node
        prev_node = cur_node
    print_nodes(node_start)
    return node_start


node = node_init([1,2,3,4,5])
print(Solution().reverseKGroup(node, 2))