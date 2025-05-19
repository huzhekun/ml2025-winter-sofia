import numpy

n = -1

n = int(input("Please input a positive integer: "))

while n <= 0:
        print("Not a positive integer")
        n = int(input("Please input a positive integer: "))

points = numpy.empty((2, n))

for i in range(n):
        print(i)
        points[0][i] = float(input("Please input x value: "))
        points[1][i] = float(input("Please input y value: "))

x = float(input("Please input x to see k-NN for all k <= n regression: "))

distanceSortedPoints = numpy.argsort(numpy.array(numpy.abs(points[0] - x)))

for i in range(1,n):
        estimate = 0
        for k in range(i):
                estimate += points[1][distanceSortedPoints[k]]
        estimate = estimate / i
        print(str(i) + "-NN estimate: " + str(estimate))
