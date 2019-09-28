li = []
li.append(1)
print(li)
li.append(2)
print(li)
li.append(3)
print(li)
li.pop()
print(li)
li.pop()
li.pop()
print(li)

if li != []:
    li.pop()
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
        print("push item",self.items)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if self.items == []:
            return  True
        return False
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    while not s.is_empty():
        item = s.pop()
        print("pop item:",item)


