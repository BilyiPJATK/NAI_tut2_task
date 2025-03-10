import math


def calculateDistances(training_vectors, test_vector):
    value = 0
    list = []
    for i in range(len(training_vectors)):
        for j in range(len(training_vectors[i])):
            value += (training_vectors[i][j] - test_vector[j])**2
        list.append(round(math.sqrt(value), 3))
        value = 0
    return list

print(calculateDistances([[1,2,3],[3,2,1],[1,3,2]],[1,3,2]))