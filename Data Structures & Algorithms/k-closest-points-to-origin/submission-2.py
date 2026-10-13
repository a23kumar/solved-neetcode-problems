import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate_distance(x1, y1):
            return math.sqrt((x1)**2 + (y1)**2)

        # instantiate a heap
        # first go through and calculate all distances for the points
        # for each one, we push it to the heap

        # then we go back and pop k elements from the heap and append them to the result array then return
        heap = []
        res = []
        for x1, y1 in points:
            dist = calculate_distance(x1, y1)
            heapq.heappush(heap, [dist, x1, y1])
        
        for _ in range(k):
            _, x1, y1 = heapq.heappop(heap)
            res.append([x1, y1])
        
        return res