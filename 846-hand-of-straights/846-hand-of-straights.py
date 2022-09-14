class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        
        # counter = {}
        # for n in hand:
        #     counter[n] = 1 + counter.get(n, 0)
        counter = Counter(hand)
        heap = list(counter.keys())
        heapq.heapify(heap)
        while heap:
            first = heap[0]
            
            for i in range(first, first + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        
        return True