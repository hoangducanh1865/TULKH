from ortools.sat.python import cp_model


def main():
    pass
    # Input
    m, n, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(m)]
    B = [tuple(map(int, input().split())) for _ in range(k)]

    # Model & Solver
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    # Bien
    # oo = 10**9
    X = {} # X[c]: Giao vien day lop c
    for c in range(n):
        domain = []
        for t in range(m):
            if A[t][c] == 1:
                domain.append(t)
        X[c] = model.NewIntVarFromDomain(cp_model.Domain.FromValues(domain), f"X_{c}")
    
    Y = {} # Y[t]: Load cua giao vien t
    for t in range(m):
        Y[t] = model.NewIntVar(0, n, f"Y_{t}")   
        
    Z = {}
    for t in range(m):
        for c in range(n):
            Z[t, c] = model.NewBoolVar(f"Z_{t}_{c}")       
        
    F = model.NewIntVar(0, n, "Z")

    # Rang buoc 1: X[i] != X[j]
    for i, j in B:
        model.Add(X[i] != X[j])
    
    # Rang buoc 2:
    for t in range(m):
        for c in range(n):
            model.Add(X[c] == t).OnlyEnforceIf(Z[t, c])
            model.Add(X[c] != t).OnlyEnforceIf(Z[t, c].Not())
            
    # Rang buoc 3: 
    for t in range(m):
        cnt = 0
        for c in range(n):
            cnt += Z[t, c]
        model.Add(Y[t] == cnt)
        model.Add(Y[t] <= F)

    # Ham muc tieu
    model.Minimize(F)  # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve(model)

    # Output
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        # print(int(solver.Value(x)))
        print(int(solver.ObjectiveValue()))
        for c in range(n):
            print(int(solver.Value(X[c])), end=" ")
    else:
        print("-1")


if __name__ == "__main__":
    main()
