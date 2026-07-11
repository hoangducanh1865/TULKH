from ortools.linear_solver import pywraplp

def main():
    pass
    # Input
    n = int(input())
    C = [list(map(int, input().split())) for _ in range(n)]
    
    # Solver 
    solver = pywraplp.Solver.CreateSolver("SCIP")
    
    # Bien x[i, j]
    x = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                x[i, j] = solver.IntVar(0, 1, f"x_{i}_{j}")

    # Bien MTZ: de loai bo cac chu trinh con
    u = {}
    for i in range(n):
        u[i] = solver.NumVar(0, n - 1, f"u_{i}")
    
    # Rang buoc 1: Moi dinh co dung 1 cung di ra
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i != j:
                cnt += x[i, j]
        solver.Add(cnt == 1)
    
    # Rang buoc 2: Moi dinh co dung 1 cung di vao
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i != j:
                cnt += x[j, i]  
        solver.Add(cnt == 1)
    
    # Rang buoc 3: MTZ loai bo chu trinh con
    solver.Add(u[0] == 0)
    
    for i in range(1, n):
        solver.Add(u[i] >= 1)
        solver.Add(u[i] <= n - 1)
    
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                solver.Add(
                    u[i] - u[j] + n * x[i, j] <= n - 1
                )
    
    # Ham muc tieu
    obj = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                obj += C[i][j] * x[i, j]
    
    solver.Minimize(obj)
    
    # Solve
    status = solver.Solve()
    
    # Output
    if status == pywraplp.Solver.OPTIMAL:
        print(round(solver.Objective().Value()))
        
        tour = [0]
        cur = 0
        
        while True:
            nxt = -1
            for j in range(n):
                if cur != j and round(x[cur, j].solution_value()) == 1:
                    nxt = j
                    break
            
            tour.append(nxt)

            if nxt == 0:
                break
            
            cur = nxt
            
        for i in range(n + 1):
            print(tour[i], end=" ")
    else:
        print("-1")
    
if __name__ == "__main__":
    main()