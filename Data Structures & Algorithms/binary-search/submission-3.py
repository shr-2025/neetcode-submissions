class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def perform_search(down: int, up: int, nums: List[int], target: int):
            if down > up:
                return -1
            mid = (down + up) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                return perform_search(down=mid + 1, up=up, nums=nums, target=target)
            else:
                return perform_search(down=down, up=mid - 1, nums=nums, target=target)
        
        down = 0 
        up = len(nums) - 1

        return perform_search(down=down, up=up, nums=nums, target=target) 
        