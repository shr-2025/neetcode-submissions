class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        max_l = 0
        
        char_to_inx = dict()
        max_s  = ""

        for right in range(left, len(s)):
            if s[right] in char_to_inx and char_to_inx[s[right]] >=left:
                left = char_to_inx[s[right]] + 1
            #max_l = max(max_l, right-left + 1)
            if right-left + 1 > max_l:
                max_l = right-left + 1
                max_s = s[left:right+1]
            char_to_inx[s[right]] = right

        return max_l