from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        char_to_count = defaultdict(int)
        result = 0
        while right < len(s) and left <= right:
            char_to_count[s[right]] += 1
            max_f = 0
            for key in char_to_count.keys():
                max_f = max(max_f, char_to_count[key])
            valid = (right-left+1 - max_f) <= k
            if valid:
                result = max(result, right-left+1)
                right += 1
            else:
                if char_to_count[s[left]] == 1:
                    del char_to_count[s[left]]
                else:
                    char_to_count[s[left]] -= 1
                left += 1
                char_to_count[s[right]] -= 1
        return result