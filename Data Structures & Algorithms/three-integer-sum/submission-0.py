class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        for i in range(len(nums) - 2): 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
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
                    res.append([nums[i], nums[j] , nums[k]])
                    j += 1
                    k -= 1
                    # need to skip duplicates 
                    while j < k and nums[j] == nums[j - 1]: 
                        j += 1
                    while j < k and nums[k] == nums[k + 1]: 
                        k -= 1
        return res


