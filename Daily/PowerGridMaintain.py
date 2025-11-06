# 3607
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        online = set()
        station_groups = {}
        minheaps = defaultdict(list)

        def dfs(station, group_id):
            if station in online:
                return
            online.add(station)
            station_groups[station] = group_id
            heappush(minheaps[group_id], station)

            for nei in graph[station]:
                dfs(nei, group_id)

        for s in range(1,c + 1):
            dfs(s, s)

        res = []
        for op, station in queries:
            if op == 1:
                if station in online:
                    res.append(station)
                    continue
                group_id = station_groups[station]
                heap = minheaps[group_id]
                while heap and heap[0] not in online:
                    heappop(heap)
                if heap:
                    res.append(heap[0])
                else:
                    res.append(-1)
            else:
                online.discard(station)
        return res