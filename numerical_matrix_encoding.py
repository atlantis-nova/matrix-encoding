import numpy as np

def M_sorted_encoding(arr1):
    arr1 = np.array(arr1)
    arr1 = arr1.flatten()
    arr1 = arr1.flatten()
    arr1.sort()
    return arr1

def T_sorted_encoding(arr1):
    arr1 = np.array(arr1)
    arr1 = arr1.transpose()
    arr1.sort()
    return arr1

def Spre_count_encoding(arr1, vector_length):
    arr1 = np.array(arr1)
    arr1_zeros = np.zeros(vector_length)
    for el in arr1:
        arr1_zeros[:el] += 1
    return arr1_zeros