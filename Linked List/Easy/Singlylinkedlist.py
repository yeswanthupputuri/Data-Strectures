"""
singly linked list operations   

"""
class LinkedNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def traversal(self, head):
        st = []
        temp = head 
        while temp:
            st.append(temp.data)
            temp = temp.next 
        return st
    
    # Insertion of an element at head of the linked list
    def insertathead(self, head, data):
        newnode = LinkedNode(data)
        newnode.next = head
        head = newnode
        return head
    
    # insertion of an element at tail of the linked list
    def insertattail(self, head, data):
        newnode = LinkedNode(data)
        if head is None:
            return LinkedNode(data)
        temp = head
        while temp.next is not None:
            temp = temp.next 
        newnode = LinkedNode(data)
        temp.next = newnode
        return head
    
    # insertion at kth position of an linked list
    def insertatk(self, head, data, k):
        if head is None:
            if k == 1:
                return LinkedNode(data)
            else:
                return head
        if k == 1:
            return self.insertathead(head, data)
        temp = head 
        cnt = 0
        while temp is not None:
            cnt += 1
            if cnt == k -1:
                newnode = LinkedNode(data)
                newnode.next = temp.next
                temp.next = newnode
            temp = temp.next 
        return head
    
    # Insertion before the a particular value in Linked list  
    def insertbeforevalue(self, head, x, val):
        if head is None:
            return head
        if head.val == x:
            return self.insertathead(val, head)
        temp = head
        while temp.next is not None:
            if temp.next.val == x:
                newnode = LinkedNode(val, temp.next)
                temp.next = newnode
                break
            temp = temp.next 
        return head
    
    # deletion of the head of the linked list
    def deletehead(self, head):
        if head is None:
            return head
        temp = head
        head = head.next
        del temp
        return head
    
    def deletetail(self, head):
        if head is None or head.next is None:
            return None
        temp = head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        return head 
    
    # delete a node at kth position of the linked list
    def deleteatk(self, head, k):
        if head is None:
            return head
        if k == 1:
            head = head.next 
            return head 
        temp = head 
        for i in range(k - 2):
            if temp is None:
                break 
            temp = temp.next 
        if temp is None or temp.next is None:
            return head
        temp.next = temp.next.next
        return head
    
    #Delete a element with value x from the linked list
    def deletevalue(self, head, x):
        if head is None:
            return head
        if head.data == x:
            head = head.next 
            return head
        temp = head 
        while temp.next is not None:
            if temp.next.data == x:
                temp.next = temp.next.next
                break
            temp = temp.next 
        return head
            
        
        
    
                