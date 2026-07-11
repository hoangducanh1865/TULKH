from ortools.linear_solver import pywraplp

def main():
    pass
    # Input
    n, m = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    tq = []
    for _ in range(m):
        u, v = map(int, input().split())
        tq.append((u, v))
    
    # Solver
    solver = pywraplp.Solver.CreateSolver("GLOP") # ["SCIP", "GLOP"]
    if not solver:
        print("SOLVER NOT OK")
        return
    
    # Bien
    x = {}
    oo = solver.infinity()
    for i in range(1, n + 1):
        x[i] = solver.NumVar(0, oo, f"x_{i}")
    obj = solver.NumVar(0, oo, "obj")
    
    # Rang buoc 1: obj la thoi diem hoan thanh muon nhat
    for i in range(1, n + 1):
        solver.Add(x[i] + d[i] <= obj)
        
    # Rang buoc 2: Quan he tien quyet
    for u, v in tq:
        solver.Add(x[v] >= x[u] + d[u])
    
    # Ham muc tieu
    solver.Minimize(obj) # ["Minimize", "Maximize"]
    
    # Solve
    status = solver.Solve()
    
    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print(int(solver.Objective().Value()))
        # print(int(x.solution_value()))
    else:
        print("-1")
    
if __name__ == "__main__":
    main()