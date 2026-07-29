from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        result = [el[0] for el in counter.most_common()[:k]]
        return result
        
        