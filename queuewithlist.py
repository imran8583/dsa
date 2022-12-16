# queue = []

# # 1. Normal direction
# queue.append(10)
# queue.append(20)   
# queue.append(30)
# # print(queue)

# queue.pop(0)
# # print(queue)
# queue.pop(0)
# # print(queue)
# queue.pop(0)
# # print(queue)

# # 2. In other direction
# queue = []

# queue.insert(0,10)
# queue.insert(0,20)
# queue.insert(0,30)

# print(queue)

# queue.pop()
# print(queue)
# queue.pop()
# print(queue)
# queue.pop()
# print(queue)

queue = []

def enqueue():
    ele = input("Eneter an element: ")
    queue.append(ele)
    print(f"{ele} has added to queue")

def dequeue():
    if not queue:
        print("Queue is already empty!")
    else:
        ele = queue.pop(0)
        print(f"{ele} has removed from queue")

def display():
    print(f"Current queue is {queue}")


while True:
    options = int(input("Enter 1.To add 2.To remove 3.To display 4.To quit: "))

    if options == 1:
        enqueue()
    elif options == 2:
        dequeue()
    elif options == 3:
        display()
    elif options == 4:
        break
    else:
        print("Wrong option")
