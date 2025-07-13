class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = nums[i]
            left = i+1
            right = len(nums) - 1
            while (left <= right):
                threeSum = target + nums[left] + nums[right]
                if threeSum == 0:
                    res.append[[target, nums[left], nums[right]]]
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1
            return res