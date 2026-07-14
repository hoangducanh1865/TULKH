from ortools.linear_solver import pywraplp


def main():
    pass
    # Input
    N, K = map(int, input().split())
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    V = N + 2 * K
    d = [list(map(int, input().split())) for _ in range(V)]

    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP")  # ["SCIP", "GLOP"]

    # Bien
    # oo = solver.infinity()
    M_Y = sum(r) + max(c)
    MAX_Y = sum(r)
    starts = {N + k for k in range(K)}
    ends = {N + K + k for k in range(K)}
    X = {}
    for k in range(K):
        start = N + k
        end = N + K + k
        for i in range(V):
            for j in range(V):
                if i == j:
                    continue
                if j in starts:
                    continue
                if i in ends:
                    continue
                if i in starts and i != start:
                    continue
                if j in ends and j != end:
                    continue
                if i == start and j == end:
                    continue
                X[k, i, j] = solver.IntVar(0, 1, f"X_{k}_{i}_{j}")

    Y = {}  # Bien tai trong
    for k in range(K):
        for i in range(V):
            Y[k, i] = solver.IntVar(0, MAX_Y, f"Y_{k}_{i}")

    U = {}  # Bien thu tu tham khach hang, dung de loai subtour
    for k in range(K):
        for i in range(N):
            U[k, i] = solver.IntVar(0, N, f"U_{k}_{i}")

    # Rang buoc 1: Moi khach hang duoc tham dung 1 lan
    for i in range(N):
        out_deg = []
        in_deg = []
        for k in range(K):
            for j in range(V):
                if (k, i, j) in X:
                    out_deg.append(X[k, i, j])
                if (k, j, i) in X:
                    in_deg.append(X[k, j, i])
        solver.Add(sum(out_deg) == 1)
        solver.Add(sum(in_deg) == 1)

    # Rang buoc 2: Bao toan luong tren moi xe
    for k in range(K):
        for i in range(N):
            cnt_out = 0
            cnt_in = 0
            for j in range(V):
                if (k, i, j) in X:
                    cnt_out += X[k, i, j]
                if (k, j, i) in X:
                    cnt_in += X[k, j, i]
            solver.Add(cnt_out == cnt_in)

    # Rang buoc 3: Moi xe xuat phat va ket thuc dung 1 lan
    for k in range(K):
        start = N + k
        end = N + K + k
        
        cnt_out = 0
        for j in range(V):
            if (k, start, j) in X:
                cnt_out += X[k, start, j]
        solver.Add(cnt_out == 1)
        
        cnt_in = 0
        for j in range(V):
            if (k, j, end) in X:
                cnt_in += X[k, j, end]
        solver.Add(cnt_in == 1)
        
    # Rang buoc 4: Khoi tao tai trong
    def demand(node):
        if node < N:
            return r[node]
        return 0

    for k in range(K):
        start = N + k
        end = N + K + k
        solver.Add(Y[k, start] == 0)
        for i in range(V):
            solver.Add(Y[k, i] <= c[k])
    
    # Rang buoc 5: Lan truyen tai trong
    for (k, i, j), x in X.items():
        dj = demand(j)
        solver.Add(Y[k, j] >= Y[k, i] + dj - M_Y * (1 - x))
        solver.Add(Y[k, j] <= Y[k, i] + dj + M_Y * (1 - x))

    # Rang buoc 6: Loai subtour, ke ca khi r[i] = 0
    for k in range(K):
        for i in range(N):
            in_deg = []
            for j in range(V):
                if (k, j, i) in X:
                    in_deg.append(X[k, j, i])
            visit = sum(in_deg)
            solver.Add(U[k, i] >= visit)
            solver.Add(U[k, i] <= N * visit)

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if (k, i, j) in X:
                    solver.Add(U[k, j] >= U[k, i] + 1 - N * (1 - X[k, i, j]))

    # Ham muc tieu
    F = 0
    for (k, i, j), x in X.items():
        F += d[i][j] * x
    solver.Minimize(F)  # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve()

    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        # print(int(x.solution_value()))
        print(round(solver.Objective().Value()))
    else:
        print("-1")


if __name__ == "__main__":
    main()
