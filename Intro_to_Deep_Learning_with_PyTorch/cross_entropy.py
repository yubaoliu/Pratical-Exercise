import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.


def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y)*np.log(1-P))


def cross_entropy_draft(Y, P):
    s = 0.
    for y, p in zip(Y, P):
        s += y * np.log(p) + (1-y)*np.log(1-p)
    return - s


Y=[1,0,1,1]
P=[0.4,0.6,0.1,0.5]
res = cross_entropy(Y, P)
print(res)


# The correct answer is 4.8283137373
