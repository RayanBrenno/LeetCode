from collections import deque


def shortestDistanceAfterQueries(n, queries):

    adj = [[i + 1] for i in range(n)]
    

    def shortest_path():
        q = deque()
        q.append((0, 0))
        visit = set()
        visit.add((0, 0))
        while q:
            print(q)
            cur, length = q.popleft()
            print(cur, length)
            if cur == n - 1:
                return length
            for nei in adj[cur]:
                if nei not in visit:
                    q.append((nei, length + 1))
                    visit.add(nei)

    res = []
    for src, dst in queries:
        adj[src].append(dst)
        print(adj)
        res.append(shortest_path())
    return res


n = 5
queries = [[2, 4], [0, 2], [0, 4]]
print(shortestDistanceAfterQueries(n, queries))
