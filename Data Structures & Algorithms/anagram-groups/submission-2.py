class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_to_str = dict()

        for el in strs:
            arr_fr = [0]*26

            for ch in el:
                arr_fr[ord(ch)-ord('a')] += 1
            
            key = tuple(arr_fr)

            if key in key_to_str:
                key_to_str[key].append(el)
            else:
                key_to_str[key] = [el]

        result = []
        for _, val in key_to_str.items():
            result.append(val)

        return result