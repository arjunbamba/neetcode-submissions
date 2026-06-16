class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, w in times:
            adj[src].append((dst, w))
        

        minHeap = [[0, k]]
        shortest = {}

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 in shortest:
                    continue
                heapq.heappush(minHeap, (w1+w2, n2))
        
        return max(shortest.values()) if len(shortest) == n else -1