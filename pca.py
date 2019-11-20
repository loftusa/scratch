#%%
import numpy as np
import matplotlib.pyplot as plt

def show(array):
    return plt.imshow(array, cmap='gray_r')
N = 500

x1d = np.arange(64)
x1d = x1d / len(x1d)

Xs = np.repeat(x1d[None, :], N, axis=0)
Xs += np.random.normal(0, .1, size=Xs.shape)

mean_X = np.mean(Xs, axis=0)
mean_X.shape
differences = Xs - mean_X

# calculate covariance
def cov_matrix(Xi, mean_X):
    difference = np.atleast_2d(Xi - mean_X)
    return difference * difference.T

cov_matrix(Xs[0], mean_X)
all_cov = [cov_matrix(Xi, mean_X) for Xi in Xs]
mean_cov = np.mean(np.array(all_cov), axis=0)

show(mean_cov)