import numpy as np
import csv
import matplotlib.pyplot as plt

# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)


def stepFunction(t):
    if t >= 0:
        return 1
    return 0


def prediction(X, W, b):
    return stepFunction((np.matmul(X, W) + b)[0])


# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate=0.01):
    # Fill in code
    for i in range(len(X)):
        y_hat = prediction(X, W, b)
        if y[i] - y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i] - y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b


# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate=0.01, num_epochs=25):
    x_min, x_max = min(X[0]), max(X[0])
    y_min, y_max = min(X[1]), max(X[1])
    W = np.array(np.random.rand(2, 1))
    # b = np.random.rand(1)[0] + x_max
    b = np.random.rand(1)[0]
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0] / W[1], -b / W[1]))
    return boundary_lines


X = []
Y = []
with open('data.csv') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        x = row[0:2]
        y = row[2]
        X.append([float(x[0]), float(x[1])])
        Y.append(float(y))

fig = plt.figure()
ax1 = fig.add_subplot(111)
for row in range(len(X)):
    ax1.scatter(X[row][0], X[row][1], marker='x')

W = trainPerceptronAlgorithm(X, Y)
x = np.linspace(-1, 1, 100)
for w in W:
    y = w[0]*x + w[1]
# y = (-W[0] - W[1] * x)/W[2]
    plt.plot(x, y)
plt.show()