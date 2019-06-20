import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result =[]
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result


def softmax_draft(L):
    result = []
    sum = 0.
    for item in L:
        newItem = np.exp(item)
        result.append(newItem)
        sum += newItem
    for i in range(len(result)):
        result[i] = result[i]/sum
    return result

L = [1, 2, 3]
print(softmax(L))