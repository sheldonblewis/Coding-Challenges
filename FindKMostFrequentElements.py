class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list = {}
        for num in nums:
            if num not in list:
                list[num] = 1
            else:
                list[num] += 1
        
        return [key for key, _ in sorted(list.items(), key=lambda x: x[1], reverse=True)[:k]]
