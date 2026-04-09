class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in val_idx:
                return [val_idx.get(c), i]
            val_idx[nums[i]] = i
            
