
try:
    # Ask the user to enter A
    A = float(input("Enter A: "))
    
    # Ask the user to enter B
    B = float(input("Enter B: "))
    
    # Calculate the right side
    rhs = B - A - 1

    if A == 0:
        if B == 1:
            print("Any real number x is a solution (infinitely many solutions).")
        else:
            print("No solution exists (contradiction).")
    else:
        # Solve for x
        x = rhs / A
        print("Solution: x =", x)

except ValueError:
    # Handle invalid input
    print("Invalid input. Please enter valid numbers.")