import numpy as np

data = [np.array([3, 2, 8, 9]), np.array([4, 12, 34, 25, 78]), np.array([23, 12, 67])]


means = [float(np.mean(arr)) for arr in data]

print("Means for each array:", means)
