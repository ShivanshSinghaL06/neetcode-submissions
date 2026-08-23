class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sett  = set(nums)

        for n in nums:
            if n-1 not in sett:
                lengths = 1
                while (n + lengths) in sett:
                    lengths +=1 
                longest = max(lengths,longest)
        
        return longest 


        