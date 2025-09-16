# Fill in your details




import math
import scipy.integrate as spi


# 1. Taylor Series Approximation 
def taylor_series_ln_sinx(x0, n, x):
    """
    Compute the Taylor polynomial of ln(1 + sin(x)) of order n around point x0.

    Args:
        x0 (float): Reference point.
        n (int): Order of the Taylor series.
        x (float): Point at which to evaluate the polynomial.

    Returns:
        float: Approximation of ln(1 + sin(x)) using the Taylor series.
        
    """
    #step 1:compute  derivation at x 
    derivatives = [math.log(1 + math.sin(x0))] 
    
    if n > 0:
        derivatives.append(math.cos(x0) / (1 + math.sin(x0)))  # f'(x0)
    
    if n > 1:
        derivatives.append((math.cos(x0) ** 2 - math.sin(x0) * (1 + math.sin(x0))) / ((1 + math.sin(x0)) ** 2))  # f''(x0)
    
    # step 2:compute the Taylor series sum:
    taylor_sum = derivatives[0]
    for i in range(1, n + 1):
        taylor_sum += (derivatives[i] * ((x - x0) ** i)) / math.factorial(i)
    
    return taylor_sum
    
    pass

# 2a.Legendre Polynomials
def legendre_polynomial(n, x):
    """
    Compute the Legendre polynomial of degree n at point x.

    Args:
        n (int): Degree of the polynomial.
        x (float): Point at which to evaluate the polynomial.

    Returns:
        float: Value of the Legendre polynomial at x.
    """
    #base cases:
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legendre_polynomial(n - 1, x) - (n - 1) * legendre_polynomial(n - 2, x)) / n


    pass
# 2.b Legendre Approximation 
def approximate_ln_sinx_with_legendre(n, x, x0):
    """
    Approximate ln(1 + sin(x)) using Legendre polynomials.

    Args:
        n (int): Number of terms in the approximation.
        x (float): Point at which to evaluate the approximation.
        x0 (float): Reference point.

    Returns:
        float: Approximation of ln(1 + sin(x)) using Legendre polynomials.
    """   
    def legendre_polynomial(n, x):
        # base cases
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return ((2 * n - 1) * x * legendre_polynomial(n - 1, x) - (n - 1) * legendre_polynomial(n - 2, x)) / n
    # compute lambda
    def compute_lambda(j):
        integral, _ = spi.quad(lambda x: math.log(1 + math.sin(x)) * legendre_polynomial(j, x), -1, 1)
        return ((2 * j + 1) / 2) * integral
    # compute approximation using lambda and legendre polynomial
    approximation = sum(compute_lambda(i) * legendre_polynomial(i, x - x0) for i in range(n + 1))
    return approximation
    
    #
    
    pass

if __name__ == "__main__":
    print (f"This work is the work of:\n{full_name1} &  {full_name1}({student_ID1}, {student_ID2})")

    # Example usage for Taylor series
    x0_taylor = 0
    n_taylor = 2
    x_value = 1
    taylor_result = taylor_series_ln_sinx(x0_taylor, n_taylor, x_value)
    print(f"Taylor series approximation: {taylor_result}")

    # Example usage for Legendre polynomial approximation
    n_legendre = 3
    x0_legendre = 0
    legendre_result = approximate_ln_sinx_with_legendre(n_legendre, x_value, x0_legendre)
    print(f"Legendre polynomial approximation: {legendre_result}")
    

 #test from homework PDF:
