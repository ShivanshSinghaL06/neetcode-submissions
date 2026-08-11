class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i, n in enumerate(nums):
            dif  = target - n
            if dif in mapp:
                return [mapp[dif], i]
            mapp[n] = i
