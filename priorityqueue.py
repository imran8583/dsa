# priority queue is: element with highest priority will be removed first from queue

queue = []

queue.append(50)
queue.append(0)
queue.append(60)
queue.append(20)
queue.append(40)
queue.append(10)

# 1. elements with priority as their number (in ascending order)
# queue.sort()
# print(queue)
# queue.pop(0)
# print(queue)
# queue.pop(0)
# print(queue)
# queue.pop(0)
# print(queue)
# queue.pop(0)
# print(queue)
# queue.pop(0)
# print(queue)
# queue.pop(0)
# print(queue)

# 2. elements with priority as their number (in decending order)

queue.sort(reverse=True)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)