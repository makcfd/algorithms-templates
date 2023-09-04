test = """3
3 7
R.R.R.G
.Y.G.G.
B.Y.V.V
4 8
Y.R.B.B.
.R.R.B.V
B.R.B.R.
.B.B.R.R
2 7
G.B.R.G
.G.G.G.""".split('\n')


def input():
    global test
    return test.pop(0)

from collections import deque

def bfs(x, y, c, grid, visited):
    n, m = len(grid), len(grid[0])
    dx = [-1, -1, 0, 0, 1, 1]
    dy = [-1, 0, -1, 1, 0, 1]
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == c:
                visited[nx][ny] = True
                q.append((nx, ny))

def is_valid(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] != '.':
                bfs(i, j, grid[i][j], grid, visited)
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] != '.':
                return False
    return True

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    print(grid)
    print("YES" if is_valid(grid) else "NO")
