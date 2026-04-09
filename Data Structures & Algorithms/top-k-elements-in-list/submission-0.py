class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums: 
            count[n] = count.get(n, 0) + 1
        print(count)
        # buckets (len(nums))
        # [[],[],[]]
        buckets = [[] for _ in range(len(nums))]
        # fill the buckets from the counts
        for item,count in count.items(): 
            buckets[count - 1].append(item)
        k_buckets = []
        for b in reversed(buckets): 
            if len(b) == 0: 
                continue
            
            if len(k_buckets) == k: 
                return k_buckets

            # iterate throught the bucket
            for b_i in b: 
                if len(k_buckets) == k: 
                    return k_buckets
                
                k_buckets.append(b_i)
        return k_buckets
            