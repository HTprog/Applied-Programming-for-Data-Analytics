import Queue2 as q2

newQ= q2.Queue2()

newQ.enqueue(3)
newQ.enqueue("cat")
newQ.enqueue(True)
newQ.enqueue(False)

print(newQ.size())
print(newQ.dequeue())
print(newQ.is_empty())