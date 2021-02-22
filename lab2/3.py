import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt

input = "/linear.txt"
input_data = np.loadtxt(input, delimiter=",")