from ortools.linear_solver import pywraplp

def main():
    pass
    # Input
    
    # Solver
    solver = pywraplp.Solver.CreateSolver("SCIP") # ["SCIP", "GLOP"]
    if not solver:
        print("SOLVER NOT OK")
        return
    
    # Bien
    x = {}
    oo = solver.infinity()
    
    # Rang buoc
    
    # Ham muc tieu
    obj = ...
    solver.Minimize(obj) # ["Minimize", "Maximize"]
    
    # Solve
    status = solver.Solve()
    
    # Output
    if status == pywraplp.Solver.OPTIMAL:
        print(int(solver.Objective().Value()))
        # print(int(x.solution_value()))
    else:
        print("-1")
    
if __name__ == "__main__":
    main()