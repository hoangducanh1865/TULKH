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
    x = {}
    for t in range(m):
        for c in range(n):
            x[t, c] = model.NewBoolVar(f"x_{t}_{c}")
    load = {}
    for t in range(m):
        load[t] = model.NewIntVar(0, n, f"load_{t}")
    max_load = model.NewIntVar(0, n, "max_load") # obj

    # Rang buoc 1: Moi lop co dung 1 giao vien
    for c in range(n):
        cnt = 0
        for t in range(m):
            cnt += x[t, c]  
        model.Add(cnt == 1)
        
    # Rang buoc 2: Nang luc giao vien
    for t in range(m):
        for c in range(n):
            if A[t][c] == 0:
                model.Add(x[t, c] == 0)
    
    # Rang buoc 3: Trung lich
    for (i, j) in B:
        for t in range(m):
            model.Add(x[t, i] + x[t, j] <= 1)
    
    # Rang buoc 4: Load cua moi giao vien
    for t in range(m):
        cnt = 0
        for c in range(n):
            cnt += x[t, c]
        model.Add(load[t] == cnt)
        
    # Rang buoc 5: Max load
    for t in range(m):
        model.Add(load[t] <= max_load)
    """
    model.AddMaxEquality(
        max_load,
        [load[t] for t in range(m)]
    )
    """

    # Ham muc tieu
    model.Minimize(max_load) # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve(model)

    # Output
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Max load =", solver.Value(max_load))
        for c in range(n):
            for t in range(m):
                if solver.Value(x[t, c]):
                    print(f"Class {c} -> Teacher {t}")
    else:
        print("-1")

if __name__ == "__main__":
    main()