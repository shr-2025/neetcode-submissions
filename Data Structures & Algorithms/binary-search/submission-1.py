class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def perform_search(down: int, up: int, nums: List[int], target: int):
            mid = (down + up) // 2
            if target == nums[mid]:
                return mid

            if target == nums[up]:
                return up
            
            if target == nums[down]:
                return down
            if mid == down:
                return -1
            if target > nums[mid]:
                return perform_search(down=mid, up=up, nums=nums, target=target)
            else:
                return perform_search(down=down, up=mid, nums=nums, target=target)
        
        down = 0 
        up = len(nums) - 1

        return perform_search(down=down, up=up, nums=nums, target=target) 
        