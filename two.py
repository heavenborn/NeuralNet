from one import *
import matplotlib.pyplot as plt




X = np.array(([3, 5], [5, 1], [10, 2]), dtype=float)
y = np.array(([75], [82], [93]), dtype=float)



NN = Neural_Network()
yHat = NN.forward(X)
print(yHat)

djdW1, djdW2 = NN.costFunctionPrime(X, y)
