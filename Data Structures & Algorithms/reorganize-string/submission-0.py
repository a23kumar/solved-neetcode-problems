class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(pq)
        
        # Need to pop topmost element in the heap
        # check if res and prev char == popped char
        # if true, pop next value and push the already popped value back into the heap - decr count
        # if false, pop top value off heap, add char to res and decr the count

        #  only push back to heap if count > 0
        while pq:
            count, char = heapq.heappop(pq)
            print(count, char)

            if res and char == res[-1]:
                if not pq:
                    return ""
                count2, char2 = heapq.heappop(pq)
                heapq.heappush(pq, (count, char))
                res.append(char2)
                count2 += 1
                if count2 < 0:
                    heapq.heappush(pq, (count2, char2))
            else:
                res.append(char)
                count += 1
                if count < 0:
                    heapq.heappush(pq, (count, char))
        return "".join(res)

        

        