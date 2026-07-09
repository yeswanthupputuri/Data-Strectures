class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverse(self, head):
        temp = head 
        back = None
        while temp:
            front = temp.next 
            temp.next = back
            back = temp 
            temp = front 
        return back 
            