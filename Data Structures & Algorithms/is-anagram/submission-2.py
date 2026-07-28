from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counter(text: str) -> dict:
            counts = dict()
            for i in range(len(text)):
                if text[i] not in counts:
                    counts[text[i]] = 1
                else:
                    counts[text[i]] += 1
            return counts
        
        count_s = counter(s)
        count_t = counter(t)
        return count_s == count_t