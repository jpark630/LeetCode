class Solution:
    def countOdds(self, low: int, high: int) -> int:
        import math
        #짝 짝 8 4 -> 2, 10 2 -> 4
        if low % 2 == 0 | high % 2 == 0:
            temp = (high-low)/2
        ## 짝 홀 8 3 -> 3, 10 3 -> 4
        elif (low + high) % 2 == 1:
            temp = math.ceil(float(high-low)/2)
        # 홀 짝 7 2 -> 3, 11 2 -> 5
        elif low % 2 == 1 | high % 2 == 1:
            temp = (high-low)/2 + 1
        temp = int(temp)
        return temp
