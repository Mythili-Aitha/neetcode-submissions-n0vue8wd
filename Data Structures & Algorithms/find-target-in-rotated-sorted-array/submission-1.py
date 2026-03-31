class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0, len(nums) -1
        d = {v:i for i,v in enumerate(nums)}
        nums = sorted(nums)
        while l<=h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return d[target]
            elif nums[mid] < target:
                l +=1
            else:
                h -=1
        return -1
