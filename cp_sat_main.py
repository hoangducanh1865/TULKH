from ortools.sat.python import cp_model

def main():
    pass
    # Input

    # Model & Solver
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    if not model or not solver:
        print("MODEL/SOLVER NOT OK")
        return

    # Bien
    x = {}
    oo = solver.infinity()

    # Rang buoc

    # Ham muc tieu
    obj = ...
    model.Minimize(obj) # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve(model)

    # Output
    if status == cp_model.OPTIMAL:
        print(int(solver.ObjectiveValue()))
        # print(int(solver.Value(x)))
    else:
        print("-1")

if __name__ == "__main__":
    main()