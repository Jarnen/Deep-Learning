# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
import numpy as np


def softmax(L):
    exp_L = np.exp(L)
    sum_exp_L = np.sum(exp_L)

    result = []
    for num in exp_L:
        result.append(num / sum_exp_L)

    return result


softmxresult = softmax([2, 1, 0])
for i in softmxresult:
    print(i)