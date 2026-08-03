class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        n = len(nums)

        for i in range(n):
            # Skip duplicate fixed numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since array is sorted, no possible triplet after this
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # Need a larger sum
                    left += 1

                else:
                    # Need a smaller sum
                    right -= 1

        return result