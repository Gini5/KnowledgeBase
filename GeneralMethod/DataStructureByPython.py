class Stack(object):
    def __init(self):
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