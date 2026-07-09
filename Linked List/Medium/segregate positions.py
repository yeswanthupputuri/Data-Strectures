"""   
Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list.
Consider the 1st node to have index 1 and so on. The relative order of the elements inside the odd and even group must remain the same as the given input.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head 
        odd = head 
        even = head.next 
        link = head.next 
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next 
            odd = odd.next 
            even = even.next 
        odd.next = link
        return head