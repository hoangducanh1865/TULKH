from ortools.sat.python import cp_model


def main():
    pass
    # Input
    m, n = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    B = []
    for _ in range(k):
        i, j = map(int, input().split())
        B.append((i, j))

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
        
    F = model.NewIntVar(0, n, "Z")

    # Rang buoc 1: X[i] != X[j]
    for i, j in B:
        model.Add(X[i] != X[j])
    
    # Rang buoc 2: Y[t] <= F
    for t in range(m):
        gan_cho = []
        for c in range(n):
            b = model.NewBoolVar(f"b_{t}_{c}")
            model.Add(X[c] == t).OnlyEnforceIf(b)
            model.Add(X[c] != t).OnlyEnforceIf(b.Not())
            gan_cho.append(b)
        model.Add(Y[t] == sum(gan_cho))
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
