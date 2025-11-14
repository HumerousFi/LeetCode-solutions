class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i != 2:
            for e in nums:
                ans.append(e)
            i += 1
        return ans