from ortools.linear_solver import pywraplp

def main():
    pass
    # Input
    n, m = map(int, input().split())
    C = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(m)] # m x n
    b = list(map(int, input().split()))
    
    # Solver
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        print("SOLVER NOT OK")
        return
    
    # Bien
    x = []
    oo = solver.infinity()
    for j in range(n):
        x.append(solver.NumVar(0, oo, f'x_{j}'))
    
    # Rang buoc 
    for i in range(m):
        row = 0
        for j in range(n):
            row += A[i][j] * x[j] 
        solver.Add(row <= b[i])
        
    # Ham muc tieu
    obj = 0
    for j in range(n):
        obj += C[j] * x[j]
    solver.Maximize(obj)
    
    # Solve
    status = solver.Solve()
    
    # Output
    if status == pywraplp.Solver.OPTIMAL:
        print(n)
        for j in range(n):
            val = x[j].solution_value()
            if abs(val) < 1e-9:
                val = 0.0
            print(f"{val:.1f}", end=" ")
    else:
        print("UNBOUNDED")
    
if __name__ == "__main__":
    main()