import numpy as np

class Game:
    def __init__(self, count):
        self.count = count
    
    def __repr__(self) -> str:
        np_arr = np.random.randint(0,high=101, size=self.count)
        result_1 =f'Array     = {np_arr}'
        max_arr = np.max(np_arr)
        result_2 = f'Max value = {max_arr:>4}'
        output = 'WIN' if max_arr > 70 else 'FAIL'
        result_3 = f'    Output    = {output:>8}'
        
        return result_1 + result_2 + result_3