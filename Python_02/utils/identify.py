import numpy as np

def judge(input_array):
    return "Win" if np.max(input_array) >=70 else "Fail"