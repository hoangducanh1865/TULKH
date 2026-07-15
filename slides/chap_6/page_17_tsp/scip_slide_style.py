from ortools.linear_solver import pywraplp


def main():
    pass
    # Input
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]

    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP")  # ["SCIP", "GLOP"]

    # Bien
    # oo = solver.infinity()
    X = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                X[i, j] = solver.IntVar(0, 1, f"X_{i}_{j}")
    
    Y = {} # Phuc vu MTZ
    for i in range(n):
        Y[i] = solver.IntVar(0, n - 1, f"Y_{i}")

    # Rang buoc 1: Moi dinh co dung 1 canh di vao va dung 1 canh di ra
    for i in range(n):
        cnt_in = 0
        cnt_out = 0
        for j in range(n):
            if i != j:
                cnt_out += X[i, j]
                cnt_in += X[j, i]
        solver.Add(cnt_in == 1)
        solver.Add(cnt_out == 1)
        
    # Rang buoc 2: Cam tao chu trinh con bang MTZ
    solver.Add(Y[0] == 0)
    for i in range(1, n):
        solver.Add(Y[i] >= 1)
        solver.Add(Y[i] <= n - 1)
    
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                solver.Add(Y[i] - Y[j] + n * X[i, j] <= n - 1)    
        
    # Ham muc tieu
    F = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                F += d[i][j] * X[i, j]
                
    solver.Minimize(F)  # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve()

    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        # print(int(x.solution_value()))
        print(round(solver.Objective().Value()))
        tour = [0]
        cur = 0
        while True:
            nxt = -1
            for i in range(n):
                if cur != i and round(X[cur, i].solution_value()) == 1:
                    nxt = i
                    break
            tour.append(nxt)
            if nxt == 0:
                break
            cur = nxt
        for i in range(n + 1):
            print(tour[i] + 1, end=" ")
    else:
        print("-1")


if __name__ == "__main__":
    main()
