class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        all_nums = set(nums)
        for el in nums:
            if (el - 1) not in all_nums:
                long = 1
                while el + long in all_nums:
                    long += 1
                longest = max(long, longest)
        return longest
            
                
            
        
        