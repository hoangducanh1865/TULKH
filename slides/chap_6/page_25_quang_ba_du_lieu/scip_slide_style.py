from ortools.linear_solver import pywraplp


def main():
    pass
    # Input
    N, M, s, L = map(int, input().split())
    s -= 1
    adj = [[] for _ in range(N)]
    for e in range(M):
        u, v, t, c = map(int, input().split())
        u -= 1
        v -=1 
        adj[u].append((v, t, c))
        adj[v].append((u, t, c))

    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP")  # ["SCIP", "GLOP"]

    # Bien
    # oo = solver.infinity()
    BIG_M = 10**9
    X = {}
    for i in range(N):
        for (j, t, c) in adj[i]:
            X[i, j] = solver.IntVar(0, 1, f"X_{i}_{j}")
    
    Y = {}
    for i in range(N):
        Y[i] = solver.IntVar(0, L, F"Y_{i}")

    # Rang buoc 1
    for j in range(N):
        if j == s:
            continue 
        cnt_in = 0
        for (i, t, c) in adj[j]:
            cnt_in += X[i, j]
        solver.Add(cnt_in == 1)
    
    # Rang buoc 2
    for i in range(N):
        for (j, t, c) in adj[i]:
            solver.Add(Y[i] + t + BIG_M * (1 - X[i, j]) >= Y[j])
            solver.Add(Y[i] + t - BIG_M * (1 - X[i, j]) <= Y[j])
    
    # Rang buoc 3
    for i in range(N):
        if i != s:
            solver.Add(Y[i] <= L)
    
    # Rang buoc 4
    solver.Add(Y[s] == 0)

    # Ham muc tieu
    F = 0
    for i in range(N):
        for (j, t, c) in adj[i]:
            F += c * X[i, j]
    solver.Minimize(F)  # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve()

    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        # print(int(x.solution_value()))
        print(int(solver.Objective().Value()))
    else:
        print("-1")
    

if __name__ == "__main__":
    main()
