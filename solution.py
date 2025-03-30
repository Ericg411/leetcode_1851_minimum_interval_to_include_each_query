from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = []
        sorted_intervals = sorted(intervals, key=lambda x: x[1] - x[0] + 1)
        for q in queries: 
            added = False
            for i in sorted_intervals:
                if i[0] <= q and q <= i[1]:
                    result.append(i[1] - i[0] + 1)
                    added = True
                    break
            if not added:
                result.append(-1)
            
        return result