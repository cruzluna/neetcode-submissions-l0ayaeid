class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()
        for i in range(len(nums) - 2): 
            j, k = i + 1, len(nums) - 1
            target = -nums[i] 
            while j < k: 
                val = nums[j] + nums[k]
                if  val < target: 
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else: 
                    # found the val, need to skip the targets
                    res.add(tuple(sorted([nums[i], nums[j] , nums[k]])))
                    j += 1
                    k -= 1
        return [list(t) for t in res]


