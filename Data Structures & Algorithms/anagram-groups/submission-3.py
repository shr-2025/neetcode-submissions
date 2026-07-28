from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_to_str = defaultdict(list)

        for el in strs:
            arr_fr = [0]*26

            for ch in el:
                arr_fr[ord(ch)-ord('a')] += 1
            
            key_to_str[tuple(arr_fr)].append(el)


        result = list(key_to_str.values())
        

        return result