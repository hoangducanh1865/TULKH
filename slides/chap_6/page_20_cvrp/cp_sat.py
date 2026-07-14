from ortools.sat.python import cp_model


def main():
    pass
    # Input
    N, K = map(int, input().split())
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    V = N + 2 * K
    d = [list(map(int, input().split())) for _ in range(V)]

    # Model & Solver
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    # Bien
    # oo = 10**9
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

                X[k, i, j] = model.NewBoolVar(f"X_{k}_{i}_{j}")

    Y = {}  # Bien tai trong
    for k in range(K):
        for i in range(V):
            Y[k, i] = model.NewIntVar(0, MAX_Y, f"Y_{k}_{i}")

    U = {}  # Bien thu tu tham khach hang, dung de loai subtour
    for k in range(K):
        for i in range(N):
            U[k, i] = model.NewIntVar(0, N, f"U_{k}_{i}")

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

        model.Add(sum(out_deg) == 1)
        model.Add(sum(in_deg) == 1)

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

            model.Add(cnt_out == cnt_in)

    # Rang buoc 3: Moi xe xuat phat va ket thuc dung 1 lan
    for k in range(K):
        start = N + k
        end = N + K + k

        cnt_out = 0
        for j in range(V):
            if (k, start, j) in X:
                cnt_out += X[k, start, j]

        model.Add(cnt_out == 1)

        cnt_in = 0
        for j in range(V):
            if (k, j, end) in X:
                cnt_in += X[k, j, end]

        model.Add(cnt_in == 1)

    # Rang buoc 4: Khoi tao tai trong
    def demand(node):
        if node < N:
            return r[node]
        return 0

    for k in range(K):
        start = N + k

        model.Add(Y[k, start] == 0)

        for i in range(V):
            model.Add(Y[k, i] <= c[k])

    # Rang buoc 5: Lan truyen tai trong
    for (k, i, j), x in X.items():
        dj = demand(j)
        model.Add(Y[k, j] == Y[k, i] + dj).OnlyEnforceIf(x)

    # Rang buoc 6: Loai subtour, ke ca khi r[i] = 0
    for k in range(K):

        for i in range(N):
            in_deg = []

            for j in range(V):
                if (k, j, i) in X:
                    in_deg.append(X[k, j, i])

            visit = sum(in_deg)

            model.Add(U[k, i] >= visit)
            model.Add(U[k, i] <= N * visit)

        for i in range(N):
            for j in range(N):

                if i == j:
                    continue

                if (k, i, j) not in X:
                    continue

                model.Add(U[k, j] >= U[k, i] + 1).OnlyEnforceIf(X[k, i, j])

    # Ham muc tieu
    F = []

    for (k, i, j), x in X.items():
        F.append(d[i][j] * x)

    model.Minimize(sum(F))

    # Solve
    solver.parameters.num_search_workers = 8
    solver.parameters.max_time_in_seconds = 300

    status = solver.Solve(model)

    # Output
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(round(solver.ObjectiveValue()))
    else:
        print("-1")


if __name__ == "__main__":
    main()
