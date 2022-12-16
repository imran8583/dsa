stack = []

def push():
    ele = input("Enter an element to push: ")
    stack.append(ele)
    print(stack)


def pop_element():

    if not stack:
        print("list is empty")
    
    else:
        popped = stack.pop()
        print(f"The element {popped} as deleted")
        print(f"current list is {stack} ")

while True:
    option = int(input("Select any one option 1.To Push 2.To Pop 3.To quit: "))

    if option == 1:
        push()
    elif option == 2:
        pop_element()
    elif option == 3:
        break
    else:
        print("choose right option")

