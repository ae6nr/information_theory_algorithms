from math import log2
from math import ceil
import numpy as np

def i(p):
    """
    Self-information
    :param: p probability of individual outcome
    :return: self-information
    """
    if p == 0:
        return 0
    else:
        return -p*log2(p)

def H(X):
    """
    Entropy of source X
    :param: X is a list of probabilities of the individual outcomes of X
    """
    Hx = 0
    prob = 0
    for p_i in X:
        prob += p_i
        Hx += i(p_i)

    if prob != 1.0:
        print("Warning: the sum of the probabilities supplied to H(X) do not sum to one.")
        print("X: ", X)
        print("sum: ", prob)

    return Hx

def shannon_length(p):
    """
    The Shannon Length of a codeword with probability p
    :param: p probability of outcome
    :return: l length of codeword
    """
    return ceil(-log2(p))


if __name__=="__main__":
    print("Homework 1 Values")
    
    X = np.array([0.15, 0.3, 0.22, 0.31, 0.02]) # probabilities of outcomes of X

    # Calculate Entropy of X
    print("Entropy of X:", H(X))