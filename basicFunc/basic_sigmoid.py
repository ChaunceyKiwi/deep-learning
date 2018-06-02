import math

def basic_sigmoid(x):
    s = 1 / (1 + math.exp(-x))
    return s

# basic_sigmoid(3) = 0.9525741268224334
basic_sigmoid(3)
