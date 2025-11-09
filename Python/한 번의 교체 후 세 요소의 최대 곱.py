class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        # 가짓수 
        # 1. 양수 * 양수가 큰지
        # 2. 음수 * 음수가 큰지
        # 3. 양수 * 음수가 큰지
        P_num = 100000
        N_num = -100000
        candle1 = nums[-1] * nums[-2] * P_num
        candle2 = nums[0] * nums[1] * P_num
        candle3 = nums[-1] * nums[0] * N_num
        return max(candle1, candle2, candle3)