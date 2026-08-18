class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        s = []

        for inx, el in enumerate(temperatures):
            while s and el > s[-1][0]:
                val, key =  s.pop()
                result[key] = inx - key
            s.append((el, inx))
        return result