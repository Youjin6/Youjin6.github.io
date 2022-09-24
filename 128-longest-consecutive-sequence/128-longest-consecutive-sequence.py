class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        numSet = set(nums)
        res = 0

        for i in nums:
            # check each nums if its the start of a sequence
            if i - 1 not in numSet:
                length = 1

                # if a start was found: using while loop to find the sequence
                while i + length in numSet:
                    length += 1
                res = max(res, length)

        return res