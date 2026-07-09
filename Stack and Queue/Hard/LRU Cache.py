class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.mpp = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def insertafterhead(self, node):
        nextnode = self.head.next
        self.head.next = node
        nextnode.prev = node
        node.prev = self.head
        node.next = nextnode
        
    def deletenode(self, node):
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
        
    def put(self, val, key):
        if key in self.mpp:
            node = self.mpp[key]
            node.val = val
            self.deletenode(node)
            self.insertafterhead(node)
            return 
        if len(self.mpp) == self.cap:
            node = self.tail.prev 
            del self.mpp[node.key]
            self.deletenode(node)
        newnode = Node(key, val)
        self.mpp[key] = newnode
        self.insertafterhead(newnode)
        
    def get(self, key):
        if key not in self.mpp:
            return -1 
        node = self.mpp[key]
        val = node.val 
        self.deletenode(node)
        self.insertafterhead(node)
        return val
            
        