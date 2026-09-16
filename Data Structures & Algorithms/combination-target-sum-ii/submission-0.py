class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return

            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                cur.append(candidates[j])
                backtrack(j + 1, cur, total + candidates[j])
                cur.pop()
                prev = candidates[j]

        backtrack(0, [], 0)
        return res