import math

G = []
P = []
const = 10

#------------------------------------------------------------
def CreateQ(Open):
    for i in range(const):
        Open.append([float('inf'), -1])

#------------------------------------------------------------
def EmptyQ(Open):
    return len(Open) - Open.count(Open[0]) == 0

#------------------------------------------------------------
def AddQ(Open, n, value, index):
    n = n + 1
    if n >= len(Open):
        Open.append([value, index])
    else:
        Open[n][0] = value
        Open[n][1] = index
    i = n
    while i > 1:
        j = int(i / 2)
        if Open[i][0] < Open[j][0]:
            Open[i], Open[j] = Open[j], Open[i]
        i = j
    return n

#------------------------------------------------------------
def RemoveQ(Open):
    value = Open[1][0]
    index = Open[1][1]
    n = len(Open) - Open.count([float('inf'), -1])
    if n > 1:
        Open[1][0] = Open[n][0]
        Open[1][1] = Open[n][1]
    Open[n] = [float('inf'), -1]
    n = n - 1
    i = 1
    while i * 2 <= n:
        j = i * 2
        if j < n and Open[j][0] > Open[j + 1][0]:
            j = j + 1
        if Open[i][0] <= Open[j][0]:
            break
        Open[i], Open[j] = Open[j], Open[i]
        i = j
    return value, index, n

#--------------------------------------------------------------------
def Split(string):
    k = string.index(' ')
    a = int(string[0:k])
    m = string.index(' ', k + 1, -1)
    b = int(string[k + 1:m])
    c = int(string[m + 1:len(string)])
    return a, b, c

#---------------------------------------------------------------------
def Init(path, G):
    with open(path) as f:
        string = f.readline()
        n, a, z = Split(string.replace('\t', ' '))
        for i in range(n + 1):
            G.append([0] * (n + 1))
        while True:
            string = f.readline()
            if not string:
                break
            i, j, x = Split(string.replace('\t', ' '))
            G[i][j] = G[j][i] = x
    return n, a, z

#----------------------------------------------------------------------
def Check(M, n, u):
    for i in range(1, n + 1):
        if M[i] == u:
            return True
    return False

#----------------------------------------------------------------------
def heuristic(u, g):
    # Hàm heuristic đơn giản: khoảng cách trực tiếp giữa các đỉnh
    return 0
#-------------------------------------------------------------- ------------
def A_Star(G, P, n, s, g):
    resul = 0
    Close = [0] * (n + 1)
    O = [0] * (n + 1)
    P = [0] * (n + 1)
    Open = []
    CreateQ(Open)
    m = AddQ(Open, 0, heuristic(s, g), s)
    O[s] = 1
    P[s] = s
    while not EmptyQ(Open):
        value, u, m = RemoveQ(Open)
        if u == g:
            resul = value
            break
        for v in range(1, n + 1):
            if G[u][v] != 0 and O[v] == 0 and Close[v] == 0:
                x = value + G[u][v] + heuristic(v, g) - heuristic(u, g)
                m = AddQ(Open, m, x, v)
                O[v] = 1
                P[v] = u
        Close[u] = 1
        O[u] = 0
    
    # Tạo đường đi từ P
    path = []
    current = g
    while current != s:
        path.append(current)
        current = P[current]
    path.append(s)
    path.reverse()

    return resul, path

#------------------------------------------------------------------------


def main():
    n, s, g = Init("Graph.inp", G)
    resul, path = A_Star(G, P, n, s, g)
    print(f"Đường đi ngắn nhất từ {s} to {g}: {' -> '.join(map(str, path))}")
    print(f"\nResul: {resul}")

if __name__ == "__main__":
    main()
# Ma Tran
# 8 1 8
# 1 2 1
# 1 3 4
# 2 3 2
# 2 4 5
# 3 5 3
# 4 6 2
# 5 4 1
# 5 6 4
# 6 7 3
# 7 8 1