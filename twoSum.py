
class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        my = [0]*2
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i]+nums[j] == target:
                    return [i, j]


nums = [7, 2, 11, 15]
now = Solution()
now.twoSum(nums, 9)
