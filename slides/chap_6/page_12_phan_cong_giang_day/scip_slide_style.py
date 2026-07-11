from ortools.linear_solver import pywraplp


def main():
    pass
    # Input
    m, n, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(m)]
    B = [tuple(map(int, input().split())) for _ in range(k)]

    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP")  # ["SCIP", "GLOP"]

    # Bien
    # oo = solver.infinity()
    X = {} # X[t, c] == 1 neu giao vien t day lop c
    for t in range(m):
        for c in range(n):
            X[t, c] = solver.IntVar(0, 1, f"X_{t}_{c}")
    
    Y = {} # Y[t]: Load cua giao vien t
    for t in range(m):
        Y[t] = solver.IntVar(0, n, f"Y_{t}")
    
    F = solver.IntVar(0, n, "Z") # Ham muc tieu 

    # Rang buoc 1: Moi lop co dung 1 giao vien
    for c in range(n):
        cnt = 0
        for t in range(m):
            cnt += X[t, c]
        solver.Add(cnt == 1)
    
    # Rang buoc 2: Nang luc giao vien
    for t in range(m):
        for c in range(n):
            if A[t][c] == 0:
                solver.Add(X[t, c] == 0)
    
    # Rang buoc 3: Trung lich
    for i, j in B:
        for t in range(m):
            solver.Add(X[t, i] + X[t, j] <= 1)
    
    # Rang buoc 4: Load cua giao vien 
    for t in range(m):
        cnt = 0
        for c in range(n):
            cnt += X[t, c]
        solver.Add(Y[t] == cnt)
        solver.Add(Y[t] <= F)

    # Ham muc tieu
    solver.Minimize(F)  # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve()

    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        # print(int(x.solution_value()))
        print(int(solver.Objective().Value()))
        for c in range(n):
            for t in range(m):
                if int(X[t, c].solution_value()) == 1:
                    print(t, end=" ")
                    break
    else:
        print("-1")


if __name__ == "__main__":
    main()
