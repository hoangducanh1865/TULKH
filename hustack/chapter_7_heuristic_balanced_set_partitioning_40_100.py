from ortools.linear_solver import pywraplp

def main():
    pass
    # Input
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    
    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP") # ["SCIP", "GLOP"]
    if not solver:
        print("SOLVER NOT OK")
        return
    
    # Bien
    x = {}
    oo = solver.infinity()
    for i in range(n):
        for j in range(m):
            x[i, j] = solver.IntVar(0, 1, f"x_{i}_{j}")
    load = {}
    total_w = sum(w)
    for j in range(m):
        load[j] = solver.NumVar(0, total_w, f"load_{j}")
    mx = solver.NumVar(0, total_w, "mx")
    mn = solver.NumVar(0, total_w, "mn")
    
    # Rang buoc 1: Moi vat thuoc dung 1 tap
    for i in range(n):
        cnt = 0
        for j in range(m):
            cnt += x[i, j]
        solver.Add(cnt == 1)
    
    # Rang buoc 2: Tong trong so moi tap
    for j in range(m):
        cnt = 0
        for i in range(n):
            cnt += w[i] * x[i, j]
        solver.Add(load[j] == cnt)
    
    # Rang buoc 3: mx, mn
    for j in range(m):
        solver.Add(load[j] <= mx)
        solver.Add(load[j] >= mn)
    
    # Ham muc tieu
    obj = mx - mn
    solver.Minimize(obj) # ["Minimize", "Maximize"]
    
    # Solve
    status = solver.Solve()
    
    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        # print(int(solver.Objective().Value()))
        # print(int(x.solution_value()))
        print(n)
        for i in range(n):
            for j in range(m):
                if int(x[i, j].solution_value()) == 1:
                    print(j + 1, end=" ")
                    break
    else:
        print("-1")
    
if __name__ == "__main__":
    main()