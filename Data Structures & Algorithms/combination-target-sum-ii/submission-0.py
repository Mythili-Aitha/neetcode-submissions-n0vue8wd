class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        res = []
        c.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(c):
                return
            cur.append(c[i])
            dfs(i+1, cur, total + c[i])
            cur.pop()
            while i+1 < len(c) and c[i] == c[i+1]:
                i +=1
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res
