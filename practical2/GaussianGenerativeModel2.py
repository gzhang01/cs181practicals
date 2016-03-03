from scipy.stats import multivariate_normal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as c

# Please implement the fit and predict methods of this class. You can add additional private methods
# by beginning them with two underscores. It may look like the __dummyPrivateMethod below.
# You can feel free to change any of the class attributes, as long as you do not change any of 
# the given function headers (they must take and return the same arguments), and as long as you
# don't change anything in the .visualize() method. 
class GaussianGenerativeModel:
    def __init__(self, isSharedCovariance=False):
        self.isSharedCovariance = isSharedCovariance

    # Just to show how to make 'private' methods
    def __dummyPrivateMethod(self, input):
        return None

    # TODO: Implement this method!
    def fit(self, X, Y):
        self.X = X
        self.Y = Y
        self.numFeatures = X.shape[1]
        self.k = max(Y)
        self.mu = [0] * (self.k + 1)
        self.sigma = []
        self.pi = []

        # Calculating pi
        counts = np.bincount(Y)
        self.pi = counts * 1.0 / Y.shape[0]

        # Calculating mu_k
        for k in xrange(len(self.mu)):
            count = 0
            sumPhi = [0] * self.numFeatures
            for i in xrange(len(Y)):
                if Y[i] == k:
                    sumPhi += X[i]
                    count += 1
            self.mu[k] = 1.0 / count * sumPhi

        # Calculating sigma_k
        if self.isSharedCovariance:
            self.sigma = [np.cov(X.T)] * (self.k + 1)
        else:
            d = [[] for i in xrange(self.k + 1)]
            for i in xrange(len(X)):
                d[Y[i]].append(X[i])
            for i in xrange(len(d)):
                self.sigma.append(np.cov(np.matrix(d[i]).T))

        return


    # TODO: Implement this method!
    def predict(self, X_to_predict):
        # The code in this method should be removed and replaced! We included it just so that the distribution code
        # is runnable and produces a (currently meaningless) visualization.
        Y = []
        for x in X_to_predict:
            probs = []
            for i in xrange(len(self.mu)):
                prob = self.pi[i] * multivariate_normal.pdf(x, mean=self.mu[i], cov=self.sigma[i], allow_singular=True)
                probs.append(prob)
            max_val = max(probs)
            # print probs.index(max_val)
            Y.append(probs.index(max_val))
        return np.array(Y)

    # Do not modify this method!
    def visualize(self, output_file, width=3, show_charts=False):
        X = self.X

        # Create a grid of points
        x_min, x_max = min(X[:, 0] - width), max(X[:, 0] + width)
        y_min, y_max = min(X[:, 1] - width), max(X[:, 1] + width)
        xx,yy = np.meshgrid(np.arange(x_min, x_max, .05), np.arange(y_min,
            y_max, .05))

        # Flatten the grid so the values match spec for self.predict
        xx_flat = xx.flatten()
        yy_flat = yy.flatten()
        X_topredict = np.vstack((xx_flat,yy_flat)).T

        # Get the class predictions
        Y_hat = self.predict(X_topredict)
        Y_hat = Y_hat.reshape((xx.shape[0], xx.shape[1]))

        cMap = c.ListedColormap(['r','b','g'])

        # Visualize them.
        plt.figure()
        plt.pcolormesh(xx,yy,Y_hat, cmap=cMap)
        plt.scatter(X[:, 0], X[:, 1], c=self.Y, cmap=cMap)
        plt.savefig(output_file)
        if show_charts:
            plt.show()
