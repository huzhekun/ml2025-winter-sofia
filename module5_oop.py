class MyList:
        numbers = []
        def append(self, num):
                self.numbers.append(num)

        def findNumber(self, number):
                index = -1
                for i in range(len(self.numbers)):
                        if number == self.numbers[i]:
                                index = i
                                break
                return index

n = -1

n = int(input("Please input a positive integer: "))

while n <= 0:
        print("Not a positive integer")
        n = int(input("Please input a positive integer: "))

numbers = MyList()

for i in range(n):
        numbers.append(int(input("Please input a number: ")))

x = int(input("Please input a number to see if it is in the list: "))

print(numbers.findNumber(x))
