# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # we can utilize a min heap to get the smallest value out of n lists
        # then as wel pop each value from the heap, we add it to the res 
        # at the point it just like your typical merge linked lists type of prob

        heap = []

        for i, node in enumerate(lists):
            if node:
                # push nodes into heap
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        tail = dummy

        while heap:
            _, i, node = heapq.heappop(heap)

            tail.next = ListNode(node.val)
            tail = tail.next

            if node.next:
                next_node = node.next
                heapq.heappush(heap, (next_node.val, i, next_node))
            
        return dummy.next

            