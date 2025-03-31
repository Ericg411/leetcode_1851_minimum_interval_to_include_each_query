from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        indexed_queries = [(q, i) for i, q in enumerate(queries)]
        indexed_queries.sort()

        result = [-1] * len(queries)
        heap = []
        i = 0

        for q, idx in indexed_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, start, end))
                i += 1
            
            while heap and heap[0][2] < q:
                heapq.heappop(heap)

            if heap: 
                result[idx] = heap[0][0]
            
        return result