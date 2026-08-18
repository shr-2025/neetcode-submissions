class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        s = []
        for inx, el in enumerate(temperatures):
            while s and el > temperatures[s[-1]]:
                key =  s.pop()
                result[key] = inx - key
            s.append(inx)
        return result