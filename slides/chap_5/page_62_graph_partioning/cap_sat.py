from ortools.sat.python import cp_model


def main():
    pass
    # Input
    n, m = map(int, input().split())
    e = [tuple(map(int, input().split())) for _ in range(m)]
    
    if n % 2 != 0:
        print("-1")
        return

    # Model & Solver
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    # Bien
    # oo = 10**9
    X = {}
    for i in range(n):
        X[i] = model.NewBoolVar(f"X_{i}")
        
    Y = {}
    for j in range(m):
        Y[j] = model.NewBoolVar(f"Y_{j}")
    
    # Rang buoc 1
    cnt = 0
    for i in range(n):
        cnt += X[i]
    model.Add(cnt == n // 2)
    
    # Rang buoc 2
    b = {}
    for j in range(m):
        (u, v, c) = e[j]
        
        model.Add(X[u] != X[v]).OnlyEnforceIf(Y[j])
        model.Add(X[u] == X[v]).OnlyEnforceIf(Y[j].Not())        
        
    # Ham muc tieu
    F = 0
    for j in range(m):
        _, _, c = e[j]
        F += c * Y[j]
    model.Minimize(F)  # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve(model)

    # Output
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        # print(int(solver.Value(x)))
        print(round(solver.ObjectiveValue()))
    else:
        print("-1")


if __name__ == "__main__":
    main()
