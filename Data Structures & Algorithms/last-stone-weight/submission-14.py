class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # in each interation we pop 2 stones
        # we run the comparisons
        # we keep this running in a loop until there is one stone left
        # otherwise we break out of the loop and just return zero

        # edge cases:
        # there is only one stone in the array, in that case we just break out and return that value

        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 1:
            if len(heap) == 1:
                return -heap[0]

            y = heapq.heappop(heap) * -1
            x = heapq.heappop(heap) * -1

            if x < y:
                heapq.heappush(heap, -(y - x))

        return 0