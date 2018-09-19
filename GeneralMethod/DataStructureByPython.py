class Stack(object):
    def __init__(self):
        self.s = []

    def push(self,v):
        self.s.append(v)

    def pop(self):
        return self.s.pop()

    def peek(self):
        if self.s: return self.s[-1]

    def is_empty(self):
        return not self.s

    def size(self):
        return len(self.s)

mystack = Stack()
print("is empty:", mystack.is_empty())
mystack.push(1)
print("size:",mystack.size())
print("peek:",mystack.peek())
mystack.push(2)
mystack.push(3)
print("size:",mystack.size())
print("peek:",mystack.peek())
mystack.pop()
print("size:",mystack.size())
print("peek:",mystack.peek())
print("is empty:", mystack.is_empty())