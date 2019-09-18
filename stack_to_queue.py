class StackToQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()
test = StackToQueue()
test.push(1)
test.push(2)
test.push(3)
print(test.pop())
print(test.pop())
print(test.pop())
