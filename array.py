# list in python can be considered as array
# array is heterogenous (multiple data types) in python/
# array doesn't have fixed size in python
#array can add, deletd, update, fetch the data

class Array:
    def __init__(self,fixed_size):
        self.fixed_size = fixed_size
        self.length = 0
        self.data = []

    def add(self,element):
        if self.length < self.fixed_size:
            self.data.append(element)
            self.length += 1
        else:
            print("Array is already full")

    def remove(self, index):
        if index < 0 or self.length >= index:
            print("Array index is out of Index")
        else:
            del self.data[index]
            self.length -= 1

    def display(self):
        for i in range(self.length):
            print(self.data[i])

    def update(self,index,element):
        if index > self.fixed_size or index < 0:
            print("Index out of range")
        else:
            self.data[index] = element
            self.length += 1    


    def insert(self, index, element):
        if index > self.fixed_size or index < 0:
            print("Index out of range")
        elif self.fixed_size == self.length:
            print("Array is fulll")
        else:
            self.data.insert(index,element)
            self.length += 1



obj = Array(5)
obj.add(10)
obj.add(20)
obj.add(30)
obj.add(40)
obj.add(50)
obj.add(60)
print(obj.data)
# obj.display()

print(obj.data)

obj.remove(1)
print(obj.data)

obj.add(90)
print(obj.data)

obj.update(2,100)
print(obj.data)

obj.remove(0)
print(obj.data)

obj.insert(1,200)
print(obj.data)


