from ortools.linear_solver import pywraplp


def main():
    pass
    # Input
    n, p, q = map(int, input().split())
    c = list(map(int, input().split()))
    Q = [tuple(map(int, input().split())) for _ in range(q)]
    alpha, beta, lamda, gamma = map(int, input().split())

    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP")  # ["SCIP", "GLOP"]

    # Bien
    # oo = solver.infinity()
    BIG_M = 10**9
    X = {}
    for i in range(n):
        for j in range(p):
            X[i, j] = solver.IntVar(0, 1, f"X_{i}_{j}")
    
    Y = {}
    for i in range(n):
        Y[i] = solver.IntVar(0, p - 1, f"Y_{i}")

    # Rang buoc 1: Tong so mon hoc phai >= alpha va <= beta
    for j in range(p):
        cnt = 0
        for i in range(n):
            cnt += X[i, j]
        solver.Add(cnt >= alpha)
        solver.Add(cnt <= beta)
    
    # Rang buoc 2: Tong so tin chi moi hoc ky phai >= lamda va <= gamma
    for j in range(p):
        cnt = 0
        for i in range(n):
            cnt += X[i, j] * c[i]
        solver.Add(cnt >= lamda)
        solver.Add(cnt <= gamma)
    
    # Rang buoc 3: Dieu kien tien quyet
    for (i, j) in Q:
        solver.Add(Y[i] + 1 <= Y[j])
    
    # Rang buoc 4: Moi mon duoc phan bo vao dung 1 hoc ky
    for i in range(n):
        cnt = 0
        for j in range(p):
            cnt += X[i, j]
        solver.Add(cnt == 1)
            
    # Rang buoc 5: Y va X
    for i in range(n):
        for j in range(p):
            solver.Add(Y[i] - BIG_M * (1 - X[i, j]) <= j)
            solver.Add(Y[i] + BIG_M * (1 - X[i, j]) >= j)

    # Ham muc tieu
    # F = ...
    # solver.Minimize(F)  # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve()

    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        # print(int(x.solution_value()))
        # print(round(solver.Objective().Value()))
        print("1")
    else:
        print("-1")


if __name__ == "__main__":
    main()
