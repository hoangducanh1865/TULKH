from ortools.sat.python import cp_model


def main():
    pass
    # Input

    # Model & Solver
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    # Bien
    # oo = 10**9
    X = {}
    for i in range(9):
        for j in range(9):
            X[i, j] = model.NewIntVar(1, 9, f"X_{i}_{j}")

    # Rang buoc 1: Moi phan tu tren cac hang phai khac nhau
    for i in range(1, 9):
        model.AddAllDifferent([X[i, j] for j in range(9)])
    
    # Rang buoc 2: Moi phan tu tren cac cot phai khac nhau
    for j in range(1, 9):
        model.AddAllDifferent([X[i, j] for i in range(9)])
        
    # Rang buoc 3: Moi phan tu trong mot o 3 x 3 phai khac nhau
    for i in range(3):
        for j in range(3):
            model.AddAllDifferent(
                [
                    X[3 * i + k, 3 * j + l]
                    for k in range(3)
                    for l in range(3)
                ]
            )
            
    # Ham muc tieu
    # F = ...
    # model.Minimize(F)  # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve(model)

    # Output
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        # print(round(solver.Value(x)))
        # print(round(solver.ObjectiveValue()))
        print("1")
        for i in range(9):
            for j in range(9):
                print(round(solver.Value(X[i, j])), end=" ")
            print("")
    else:
        print("-1")


if __name__ == "__main__":
    main()
