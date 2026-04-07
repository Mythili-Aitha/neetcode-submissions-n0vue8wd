class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        w = max(nums[:k])
        res = []
        for r in range(k, len(nums)+1):
            w = max(nums[r-k:r])
            res.append(w)
        return res

        