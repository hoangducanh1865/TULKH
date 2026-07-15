from ortools.linear_solver import pywraplp


def main():
    pass
    # Input

    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP")  # ["SCIP", "GLOP"]

    # Bien
    # oo = solver.infinity()
    X = {}

    # Rang buoc

    # Ham muc tieu
    F = ...
    solver.Minimize(F)  # ["Minimize", "Maximize"]

    # Solve
    status = solver.Solve()

    # Output
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        # print(int(x.solution_value()))
        print(round(solver.Objective().Value()))
    else:
        print("-1")


if __name__ == "__main__":
    main()
