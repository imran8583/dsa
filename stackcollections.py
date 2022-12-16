import collections
import queue
# 1. using collections deque module
stack = collections.deque()

stack.append(10)
stack.append(20)
stack.append(30)
# print(stack)

stack.pop()
stack.pop()
stack.pop()
# print(stack)

empty = not stack
# to check if stack is empty or not
# print(empty)


# 2. using queue lifoqueue module

stack = queue.LifoQueue()
print(stack)

stack.put(10)
stack.put(20)
stack.put(30)
print(stack)


stack.get()
print(stack)
stack.get()
print(stack)
stack.get(timeout=1)
print(stack)

