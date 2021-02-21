import numpy as np
import sklearn.preprocessing as sp

Input_data = np.array([[2.1, -1.9, 5.5],
                      [-1.5, 2.4, 3.5],
                      [0.5, -7.9, 5.6],
                      [5.9, 2.3, -5.8]])

data_binarized = sp.Binarizer(threshold=0.5).transform(Input_data)
print("\nBinarized data: \n", data_binarized)

print("Mean = ", Input_data.mean(axis=0))
print("Std deviation = ", Input_data.std(axis=0))

data_scaled = sp.scale(Input_data)

print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", data_scaled.std(axis=0))
