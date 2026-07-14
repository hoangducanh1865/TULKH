from ortools.linear_solver import pywraplp


def main():
    pass
    # Input
    M, N = map(int, input().split())
    f = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    d = list(map(int, input().split()))
    c = [list(map(int, input().split())) for _ in range(M)]

    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP")  # ["SCIP", "GLOP"]

    # Bien
    oo = solver.infinity()
    Y = {}
    for i in range(M):
        Y[i] = solver.IntVar(0, 1, f"Y_{i}")
    
    X = {}
    for i in range(M):
        for j in range(N):
            X[i, j] = solver.IntVar(0, oo, f"X_{i}_{j}")
    
    # Rang buoc 1
    for j in range(N):
        cnt = 0
        for i in range(M):
            cnt += X[i, j]
        solver.Add(cnt == d[j])
        
    # Rang buoc 2
    for i in range(M):
        cnt = 0
        for j in range(N):
            cnt += X[i, j]
        solver.Add(cnt <= Q[i])
    
    # Rang buoc 3
    for i in range(M):
        for j in range(N):
            solver.Add(X[i, j] >= 0)
            solver.Add(X[i, j] <= d[j] * Y[i])

    # Ham muc tieu
    F = 0
    for i in range(M):
        F += f[i] * Y[i]
        for j in range(N):
            F += X[i, j] * c[i][j]
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
