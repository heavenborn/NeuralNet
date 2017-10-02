import numpy as np



class Neural_Network(object):
    def __init__(self):
        # Define Hyperparameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3

        # Weights -->   Synapse parameters syn0
        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)

        self.syn0 = self.W1
        self.syn1 = self.W2

    def forward(self, x):
        # Propagate inputs though network

        self.l0 = x  # Layer 0
        self.P1 = np.dot(x, self.W1)  # Layer 0 multiplication

        self.y = self.sigmoid(self.P1) # Layer 1 activation
        #self.l1 = self.sigmoid(self.P1) # Layer 1 activation

        self.P2 = np.dot(self.y, self.W2)  # Layer 2 activation

        #self.l2 = np.dot(self.l1, self.W2) # Layer 2 activation

        z = self.sigmoid(self.P2) # this would be l3 maybe?
        return z  # number used to determine 'how well I'm doing'

    def sigmoid(self, z):
        # Apply sigmoid activation function to scalar, vector, or matrix
        return 1 / (1 + np.exp(-z))

    def sigmoidPrime(self, z):
        # Gradient of sigmoid
        return np.exp(-z) / ((1 + np.exp(-z)) ** 2)

    def performanceFunction(self, x, d):
        # Compute performance for given X,y, use weights already stored in class.
        self.z = self.forward(x)
        p = 0.5 * sum((d - self.z) ** 2) # sum of / squared errors
        return p







    def perFunctionPrime(self, x, d):
        # Compute derivative with respect to W and W2 for a given X and y:
        self.z = self.forward(x)

        delta3 = np.multiply(-(d - self.z), self.sigmoidPrime(self.P2))
        dpdW2 = np.dot(self.y.T, delta3)

        delta2 = np.dot(delta3, self.W2.T) * self.sigmoidPrime(self.P1)
        dpdW1 = np.dot(x.T, delta2)

        return dpdW1, dpdW2
   # Helper Functions for interacting with other classes:

    def getParams(self):
        # Get W1 and W2 unrolled into vector:
        params = np.concatenate((self.W1.ravel(), self.W2.ravel()))
        return params

    def setParams(self, params):
        # Set W1 and W2 using single paramater vector.
        W1_start = 0
        W1_end = self.hiddenLayerSize * self.inputLayerSize
        self.W1 = np.reshape(params[W1_start:W1_end], (self.inputLayerSize, self.hiddenLayerSize))
        W2_end = W1_end + self.hiddenLayerSize * self.outputLayerSize
        self.W2 = np.reshape(params[W1_end:W2_end], (self.hiddenLayerSize, self.outputLayerSize))

    def computeGradients(self, x, y):
        dpdW1, dpdW2 = self.perFunctionPrime(x, y)
        return np.concatenate((dpdW1.ravel(), dpdW2.ravel()))
