import math

def quadratic_equation(a, b, c):
    """Solve the quadratic equation"""
    # calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # calculate the roots
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"
