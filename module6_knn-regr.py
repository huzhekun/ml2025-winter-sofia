import numpy

n = -1

n = int(input("Please input a positive integer: "))

while n <= 0:
        print("Not a positive integer")
        n = int(input("Please input a positive integer: "))

points = numpy.empty((2, n))

for i in range(n):
        points[0][i] = float(input("Please input x value: "))
        points[1][i] = float(input("Please input y value: "))

k = int(input("Please input k for k-NN regression: "))
while k > n:
        print("K cannot be larger than number of points")
        k = int(input("Please input k for k-NN regression: "))

x = float(input("Please input x to see k-NN regression: "))

distanceSortedPoints = numpy.argsort(numpy.array(numpy.abs(points[0] - x)))

estimate = 0
for i in range(k):
        estimate += points[1][distanceSortedPoints[i]]
estimate = estimate / k
print(str(k) + "-NN estimate: " + str(estimate))
