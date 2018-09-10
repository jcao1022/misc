class Stack:

    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def get(self, index=0):
        return self.stack.pop(index)


s = Stack()

s.add('a')
s.add('b')
s.add('c')
s.add('d')
s.add('e')
s.add('f')

print(s.get())
print(s.get())
print(s.get(-1))
