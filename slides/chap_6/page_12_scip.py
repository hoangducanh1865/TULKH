from ortools.linear_solver import pywraplp

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

    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP") # ["SCIP", "GLOP"]

    # Bien
    # oo = solver.infinity()
    x = {}
    for t in range(m):
        for c in range(n):
            x[t, c] = solver.IntVar(0, 1, f"x_{t}_{c}")
    load = {}
    for t in range(m):
        load[t] = solver.IntVar(0, n, f"load_{t}")
    max_load = solver.IntVar(0, n, "max_load") # obj

    # Rang buoc 1: Moi lop co dung 1 giao vien
    for c in range(n):
        cnt = 0
        for t in range(m):
            cnt += x[t, c]  
        solver.Add(cnt == 1)
        
    # Rang buoc 2: Nang luc giao vien
    for t in range(m):
        for c in range(n):
            if A[t][c] == 0:
                solver.Add(x[t, c] == 0)
    
    # Rang buoc 3: Trung lich
    for (i, j) in B:
        for t in range(m):
            solver.Add(x[t, i] + x[t, j] <= 1)
    
    # Rang buoc 4: Load cua moi giao vien
    for t in range(m):
        cnt = 0
        for c in range(n):
            cnt += x[t, c]
        solver.Add(load[t] == cnt)
        solver.Add(load[t] <= max_load)

    # Ham muc tieu
    solver.Minimize(max_load) # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve()

    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print("Max load =", int(solver.Objective().Value()))
        for c in range(n):
            for t in range(m):
                if int(x[t, c].solution_value()) == 1:
                    print(f"Class {c} -> Teacher {t}")
    else:
        print("-1")

if __name__ == "__main__":
    main()