class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_inx = dict()

        for inx, el in enumerate(nums):
            if target - el in val_to_inx:
                return [val_to_inx[target - el], inx]
            val_to_inx[el] = inx
        return []
        