n = -1

n = int(input("Please input a positive integer: "))

while n <= 0:
        print("Not a positive integer")
        n = int(input("Please input a positive integer: "))

numbers = []

for i in range(n):
        numbers.append(int(input("Please input a number: ")))

x = int(input("Please input a number to see if it is in the list: "))

index = -1

for i in range(len(numbers)):
        if x == numbers[i]:
                print(i)
                index = i
                break

if index < 0:
        print(-1)
