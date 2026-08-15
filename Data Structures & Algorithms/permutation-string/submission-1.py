class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_counts = defaultdict(int)
        for el in s1:
            s1_counts[el] += 1
        window_count = defaultdict(int)
        for right, ch in enumerate(s2):
            window_count[ch] += 1
            while window_count[ch] > s1_counts[ch]:
                window_count[s2[left]] -= 1
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False