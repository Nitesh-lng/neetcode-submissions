class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 0
            seen[i] += 1

        new = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in new[:k]]