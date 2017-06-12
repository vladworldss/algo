# coding: utf-8
"""
Алгоритм обхода графа в глубину (DFS).
"""
n, m = map(int, input().split())  # количество вершин и ребер в графе
adj = [[] for i in range(n)]  # список смежности
used = [False for i in range(n)]  # массив для хранения информации о пройденных и не пройденных вершинах

# считываем граф, заданный списком ребер
for _ in range(m):
    v, w = map(int, input().split())
    v -= 1
    w -= 1
    adj[v].append(w)
    adj[w].append(v)


def dfs(v):  # процедура обхода в глубину
    if used[v]:  # если вершина является пройденной, то не производим из нее вызов процедуры
        return
    used[v] = True  # помечаем вершину как пройденную
    print(v + 1, end=' ')
    for w in adj[v]:
        dfs(w)  # запускаем обход из всех вершин, смежных с вершиной v


def run():
    for v in range(n):
        dfs(v)

run()
