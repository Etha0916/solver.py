import math


def quadratic_solver():
    print("stanCode Quadratic Solver!")

    # Get user input for coefficients
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    # Calculate discriminant
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Two real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Two real roots: {root1} and {root2}")
    elif discriminant == 0:
        # One real root
        root = -b / (2 * a)
        print(f"One root: {root}")
    else:
        # No real roots
        print("No real roots")


# Run the program
quadratic_solver()