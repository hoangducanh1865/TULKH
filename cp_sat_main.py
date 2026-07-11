from ortools.sat.python import cp_model

def main():
    pass
    # Input

    # Model & Solver
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    # Bien
    # oo = 10**9
    x = {}

    # Rang buoc

    # Ham muc tieu
    obj = ...
    model.Minimize(obj) # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve(model)

    # Output
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(int(solver.ObjectiveValue()))
        # print(int(solver.Value(x)))
    else:
        print("-1")

if __name__ == "__main__":
    main()