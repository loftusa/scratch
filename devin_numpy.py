#%%
import numpy as np


# make function that creates an array of arbitrary dimensionality
# arguments: dimension (d)
# shape: (n, n+1, n+2, ...), where n is max(3, d)
# len(shape) == d
# must start at minimum of 3
# e.g., if d is 3, then it'll be
# shape = (3, 4, 5)
# fill with
# final result is fin.
# fin.ravel() == np.arange(a.size)




# Case where d = 3
d = 3
a = np.array(
    [
        [
            [ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
        ],
        [
            [20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29],
            [30, 31, 32, 33, 34],
            [35, 36, 37, 38, 39],
        ],
        [
            [40, 41, 42, 43, 44],
            [45, 46, 47, 48, 49],
            [50, 51, 52, 53, 54],
            [55, 56, 57, 58, 59],
        ],
    ]
)


a.shape
a.size


def make_dimensionality_array(d):
    start = max(3, d)
    end = start + d
    dims = np.arange(start, end)
    prod = np.prod(dims)
    a = np.arange(prod).reshape(*dims)  # aha!
    return a

for i in range(1,5):
    print(i, make_dimensionality_array(i).shape)



'''
in the continuing adventures of our young padawan...

def foo(array, dim, index, fill):
    # do stuff
    return fin

fin[?,?,?,... index, ...] = fill, where there are dim ?'s.
'''

#%%
import matplotlib.pyplot as plt
x = np.arange(-10, 10, step=.2)
np.trunc(x)
# %%
