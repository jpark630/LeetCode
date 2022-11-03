class Solution:
    def average(self, salary: List[int]) -> float:
        import numpy as np
        salary.sort()
        del salary[0]
        del salary[-1]
        result = np.mean(salary)
        return result
