class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if head is None or head.next is  None:
            return head 
        zeroHead = ListNode(-1)
        oneHead = ListNode(-1)
        twoHead = ListNode(-1)

        temp = head 
        zero = zeroHead
        one = oneHead
        two = twoHead

        while temp is not None:
            if temp.val == 0:
                zero.next = temp
                zero = temp 
            elif temp.val == 1:
                one.next = temp
                one = temp 
            elif temp.val == 2:
                two.next = temp 
                two = temp 
            temp = temp.next 

        zero.next = oneHead.next if oneHead.next else twoHead.next 
        one.next = twoHead.next 
        two.next = None 
        newHead = zeroHead.next 
        return newHead 





