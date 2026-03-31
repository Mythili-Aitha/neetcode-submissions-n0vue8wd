import heapq
class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        s = [-i for i in s]
        heapq.heapify(s)
        while len(s) > 1:
            l = heapq.heappop(s)
            nl = heapq.heappop(s)
            if nl > l:
                heapq.heappush(s, l - nl)
        s.append(0)
        return abs(s[0])

            
        