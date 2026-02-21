class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expectedSum = n * (n + 1) // 2
        actualSum = sum(nums)
        missing = expectedSum - sum(set(nums))
        duplicate = actualSum - (expectedSum - missing)
        return [duplicate, missing]
                
        
