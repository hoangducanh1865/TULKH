from ortools.linear_solver import pywraplp

def main():
    pass
    # Input
    m, n = map(int, input().split())
    f = list(map(int, input().split()))
    K = list(map(int, input().split()))
    d = list(map(int, input().split()))
    C = [list(map(int, input().split())) for _ in range(n)] # n x m
    
    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        print("SOLVER NOT OK")
        return
    
    # Bien
    y = []
    for j in range(m):
        y.append(solver.IntVar(0, 1, f'y_{j}'))
    
    x = {}
    for i in range(n):
        for j in range(m):
            x[i, j] = solver.NumVar(0, solver.infinity(), f'x_{i}_{j}')
    
    # Rang buoc 1: Kho j co cong suat luu tru toi da la K[j]
    for j in range(m):
        cnt = 0
        for i in range(n):
            cnt += x[i, j]
        solver.Add(cnt <= K[j] * y[j]) # Neu khong mo cua hang j (y[j] == 0) thi cnt chi can <= 0
        
    # Rang buoc 2: Cua hang i co muc tieu thu bat buoc la d[i]
    for i in range(n):
        cnt = 0
        for j in range(m):
            cnt += x[i, j]
        solver.Add(cnt == d[i])
    
    # Ham muc tieu
    obj = 0
    for j in range(m):
        obj += f[j] * y[j]
    for i in range(n):
        for j in range(m):
            obj += x[i, j] * C[i][j]
    solver.Minimize(obj)
    
    # Solve
    status = solver.Solve()
    
    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print(round(solver.Objective().Value()))
        for j in range(m):
            print(round(y[j].solution_value()), end=" ")
        print("")
        for i in range(n):
            for j in range(m):
                print(round(x[i, j].solution_value(), 2), end=" ")
            print("")
    else:
        print("-1")
    
if __name__ == "__main__":
    main()