class Queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,itm):
        self.queue.append(itm)

    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return not(bool(self.queue))
    
    def size(self):
        return len(self.queue)
    
    def get_Queue(self):
        return self.queue
    
qu = Queue()

qu.enqueue(9)
qu.enqueue(8)
qu.enqueue(2)
print(qu.get_Queue())

print("Size of Queue:",qu.size())

print("The element dequeued:",qu.dequeue())

print(qu.get_Queue())
print("The First element:",qu.peek())

qu.dequeue()
qu.dequeue()
print(qu.get_Queue())
print("Is the Queue empty? ", qu.is_empty())
