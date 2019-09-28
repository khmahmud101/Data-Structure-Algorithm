class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        if self.items == []:
            return True
        return False


if __name__ == "__main__":
    s = Queue()
    s.enqueue("Hridoy")
    s.enqueue("Emdad")
    s.enqueue("Shanku")

    while  s.is_empty() == False:
       person = s.dequeue()
       print(person)
