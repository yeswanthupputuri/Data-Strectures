"""  
Design a stack that supports the following operations in constant time: push, pop, top, and retrieving the minimum element.

Implement the MinStack class:

MinStack(): Initializes the stack object.
void push(int val): Pushes the element val onto the stack.
void pop(): removes the element on the top of the stack.
int top(): gets the top element of the stack.
int getMin(): retrieves the minimum element in the stack.

"""

class minstack:
    def __init__(self):
        self.st = []
        self.mini = None
    def push(self, val):
        if not self.st:
            self.mini = val
            self.st.append(val)
            return 
        if val > self.mini:
            self.st.append(val)
        else:
            self.st.append(2 * val - self.mini)
            self.mini = val
    def pop(self):
        if not self.st:
            return None 
        x = self.st.pop()
        if x < self.mini:
            self.mini = 2 * self.mini - x 
            
    def top(self):
        if not self.st:
            return -1
        x = self.st[-1]
        if x > self.mini:
            return x
        return self.mini
    
    def getmin(self):
        return self.mini