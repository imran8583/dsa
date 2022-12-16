import queue
q = queue.PriorityQueue()

# we dont need to use sort function for priority
# priporty queue method does that ofr us
q.put(20)
q.put(10)
q.put(50)
q.put(80)
q.put(50)
q.put(90)
q.put(30)
q.put(105)

# # numbers are removed in ascending priority
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

# numbers are removed in ascending priority
print(q.get())

