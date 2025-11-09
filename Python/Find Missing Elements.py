class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minNum = min(nums)
        maxNum = max(nums)
        temp = []
        for i in range(minNum, maxNum + 1):
            if i not in nums:
                temp.append(i)
        return temp