class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        temp = dummy 
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val 
                l1 = l1.next 
            if l2:
                sum += l2.val 
                l2 = l2.next 
            sum += carry 
            carry = sum // 10 
            new = ListNode(sum % 10)
            temp.next = new
            temp = temp.next
        return dummy.next





