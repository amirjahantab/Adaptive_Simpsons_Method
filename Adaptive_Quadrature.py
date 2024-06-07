import numpy as np
import matplotlib.pyplot as plt

def adaptive_simpsons(f, a, b, tol, max_recursion_depth=50):
    def simpsons_rule(f, a, b):
        c = (a + b) / 2.0
        h3 = abs(b - a) / 6.0
        return h3 * (f(a) + 4.0 * f(c) + f(b))

    def adaptive_aux(f, a, b, tol, whole, max_recursion_depth, depth):
        c = (a + b) / 2.0
        left = simpsons_rule(f, a, c)
        right = simpsons_rule(f, c, b)
        if depth > max_recursion_depth:
            print("Maximum recursion depth exceeded")
            return left + right
        if abs(left + right - whole) <= 15 * tol:
            return left + right + (left + right - whole) / 15.0
        return (adaptive_aux(f, a, c, tol / 2.0, left, max_recursion_depth, depth + 1) +
                adaptive_aux(f, c, b, tol / 2.0, right, max_recursion_depth, depth + 1))

    initial = simpsons_rule(f, a, b)
    return adaptive_aux(f, a, b, tol, initial, max_recursion_depth, 1)

# Define the function and parameters
def f(x):
    return (100 / x**2) * np.sin(10 / x)

a = 1.0
b = 3.0
tol = 1e-4

# Execute the algorithm
approximation = adaptive_simpsons(f, a, b, tol)
approximation


# رسم نمودار منحنی
x = np.linspace(a, b, 400)
y = f(x)

plt.plot(x, y, label=r'$f(x) = \frac{100}{x^2} \sin \left(\frac{10}{x}\right)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function Curve')
plt.legend()
plt.grid(True)
plt.show()
