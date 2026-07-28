class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_to_word = dict()

        for el in strs:
            key = ''.join(sorted(el))
            if key in key_to_word:
                key_to_word[key].append(el)
            else:
                key_to_word[key] = [el]
        
        result = []

        for _, val in key_to_word.items():
            result.append(val)

        return result