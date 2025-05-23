import numpy
import sklearn
import sklearn.neighbors

n = -1

n = int(input("Please input a positive integer: "))

while n <= 0:
        print("Not a positive integer")
        n = int(input("Please input a positive integer: "))

pointsx = numpy.empty((n, 1))
pointsy = numpy.empty(n)

for i in range(n):
        pointsx[i][0] = float(input("Please input x value: "))
        pointsy[i] = float(input("Please input y value: "))

k = int(input("Please input k for k-NN regression: "))
while k > n:
        print("K cannot be larger than number of points")
        k = int(input("Please input k for k-NN regression: "))

x = float(input("Please input x to see k-NN regression: "))

knn = sklearn.neighbors.KNeighborsRegressor(n_neighbors=k)

knn.fit(pointsx, pointsy)

estimate = knn.predict([[x]])

print(str(k) + "-NN estimate: " + str(estimate))
