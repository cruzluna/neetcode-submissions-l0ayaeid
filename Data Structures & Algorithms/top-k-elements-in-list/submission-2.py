class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums: 
            count[n] = count.get(n, 0) + 1

        heap = [(-freq, num) for num, freq in count.items()] 
        heapq.heapify(heap)

        k_b = []
        while len(k_b) < k: 
            k_b.append(heapq.heappop(heap)[1])

        return k_b
