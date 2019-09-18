class LinkNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class StackbyLink:
    def __init__(self):
        self.size = 0

    def push(self, x):
        node = LinkNode(x)
        self.size += 1
        return node.value, node.next

    def __len__(self):
        return self.size

    def pop(self):
        pass

test = StackbyLink()
x = test.push(1)
print(x)
