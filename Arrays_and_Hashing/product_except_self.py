class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1

        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = pref[i] * suff[i]
       
        return res
            
    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = res[j] * postfix
            postfix = postfix * nums[j]
        
        return res

        