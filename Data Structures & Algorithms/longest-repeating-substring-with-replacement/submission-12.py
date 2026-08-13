from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_to_count = defaultdict(int)
        result = 0
        max_f = 0

        for right in range(len(s)):
            char_to_count[s[right]] += 1
            max_f = max(max_f, char_to_count[s[right]]) # in taghyir karde faghat

            while (right-left+1) - max_f > k: # age invalid shod
                char_to_count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result