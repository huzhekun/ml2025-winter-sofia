import numpy
import sklearn
import sklearn.neighbors

n = -1

n = int(input("Please input a positive integer: "))

while n <= 0:
        print("Not a positive integer")
        n = int(input("Please input a positive integer: "))

ground = numpy.empty(n)
prediction = numpy.empty(n)

for i in range(n):
        ground[i] = int(input("Please input ground value (0 or 1): "))
        while ground[i] != 0 and ground[i] != 1:
                print("Not a value in (0,1)")
                ground[i] = int(input("Please input ground value (0 or 1): "))
        prediction[i] = int(input("Please input prediction value (0 or 1): "))
        while prediction[i] != 0 and prediction[i] != 1:
                print("Not a value in (0,1)")
                prediction[i] = int(input("Please input ground value (0 or 1): "))

precision = sklearn.metrics.precision_score(ground, prediction)
recall = sklearn.metrics.recall_score(ground, prediction)

print("Precision Score: " + str(precision))
print("Recall Score: " + str(recall))
