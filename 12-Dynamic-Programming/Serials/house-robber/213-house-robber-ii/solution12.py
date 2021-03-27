class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]


        def helper(nums):
            if not nums: return 0
            if len(nums) == 1: return nums[0]

            n = len(nums)
            dp = [0] * (n + 1)
            dp[1] = nums[0]

            for i in range(2, n + 1):
                # 假定dp[i]不偷，只和dp[i-1],dp[i-2]有关
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            return dp[-1]

        return max(helper(nums[1:]), helper(nums[:-1]))
