from scipy import optimize

import one


class trainer(object):
    def __init__(self, N):
        # Make Local reference to network:
        self.N = N

    def callbackF(self, params):
        self.N.setParams(params)
        self.P.append(self.N.costFunction(self.X, self.y))

    def performanceFunctionWrapper(self, params, X, y):
        self.N.setParams(params)
        perf = self.N.performanceFunction(X, y)
        grad = self.N.computeGradients(X, y)

        return perf, grad

    def train(self, x, y):
        # Make an internal variable for the callback function:
        self.X = x
        self.y = y

        # Make empty list to store costs:
        self.P = []

        params0 = self.N.getParams()

        options = {'maxiter': 200, 'disp': True}
        _res = optimize.minimize(self.performanceFunctionWrapper, params0, jac=True, method='BFGS',
                                 args=(x, y), options=options, callback=self.callbackF)

        self.N.setParams(_res.x)
        self.optimizationResults = _res


x = np.array(([3, 5], [5, 1], [10, 2]), dtype=float)
y = np.array(([75], [82], [93]), dtype=float)

NN = Neural_Network()

T = trainer(NN)
T.train(x, y)

