class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return not bool(self.items)

    def push(self, item):
        if not self.full():
            self.items.append(item)

            return True
        return False

    def pop(self):
        if not self.isEmpty():

            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and len(self.items) >= self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        return -1
