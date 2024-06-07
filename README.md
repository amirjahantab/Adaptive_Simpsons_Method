# Adaptive Simpson's Method for Numerical Integration

This repository provides an implementation of the Adaptive Simpson's Method for numerical integration in Python, along with a demonstration using a specific example function. The implementation includes a detailed example of using the method to integrate a given function and visualizing the function's curve using Matplotlib.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Function Definition](#function-definition)
  - [Adaptive Simpson's Method](#adaptive-simpsons-method)
  - [Example Usage](#example-usage)
- [Visualization](#visualization)
- [Detailed Explanation of Adaptive Simpson's Method](#detailed-explanation-of-adaptive-simpsons-method)
- [Contributing](#contributing)

## Introduction

The Adaptive Simpson's Method is a numerical technique used to approximate the definite integral of a function. It adapts the interval size based on the function's behavior to achieve a desired accuracy within a specified tolerance. This method is particularly useful for functions that are difficult to integrate using standard techniques.

## Installation

Ensure you have Python and the necessary libraries installed. You can install the required libraries using pip:

```bash
pip install numpy matplotlib
```

## Usage

### Function Definition

Define the function you wish to integrate. In this example, we use the function:

$\ f(x) = \frac{100}{x^2} \sin \left( \frac{10}{x} \right) \$

### Adaptive Simpson's Method

The `adaptive_simpsons` function is defined to perform the integration:

```python
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
```

### Example Usage

To use the `adaptive_simpsons` function, define the function to be integrated and specify the interval and tolerance:

```python
def f(x):
    return (100 / x**2) * np.sin(10 / x)

a = 1.0
b = 3.0
tol = 1e-4

# Execute the algorithm
approximation = adaptive_simpsons(f, a, b, tol)
print(f"Approximate integral: {approximation}")
```

## Visualization

The provided code also includes a visualization of the function curve using Matplotlib:

```python
# Plotting the function curve
x = np.linspace(a, b, 400)
y = f(x)

plt.plot(x, y, label=r'$f(x) = \frac{100}{x^2} \sin \left(\frac{10}{x}\right)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function Curve')
plt.legend()
plt.grid(True)
plt.show()
```

This will generate a plot of the function over the specified interval `[a, b]`.

## Detailed Explanation of Adaptive Simpson's Method

### Introduction

The Adaptive Simpson's Method is an advanced numerical technique used to compute the definite integral of a function over a given interval. It is an extension of Simpson's Rule, which is a method for numerical integration that approximates the integral of a function using parabolic segments.

### Simpson's Rule

Simpson's Rule approximates the integral of a function \( f(x) \) over an interval \([a, b]\) by dividing the interval into two subintervals \([a, c]\) and \([c, b]\), where \( c = (a + b) / 2 \). The integral is then approximated by:

$\ \int_{a}^{b} f(x) \, dx \approx \frac{b - a}{6} \left[ f(a) + 4f(c) + f(b) \right] \$

This formula assumes that \( f(x) \) can be approximated by a quadratic polynomial over the interval.

### Adaptive Simpson's Method

The Adaptive Simpson's Method improves upon Simpson's Rule by recursively applying it to subintervals of the original interval, adjusting the subinterval sizes to achieve a desired accuracy.

#### Steps of Adaptive Simpson's Method

1. **Initial Approximation**: Compute the initial approximation of the integral using Simpson's Rule over the entire interval \([a, b]\).

2. **Recursive Subdivision**: Divide the interval into two subintervals \([a, c]\) and \([c, b]\), where \( c = (a + b) / 2 \). Apply Simpson's Rule to each subinterval to get two new approximations.

3. **Error Estimation**: Compare the sum of the approximations for the two subintervals with the initial approximation for the entire interval. If the difference is within the specified tolerance, accept the result. Otherwise, recursively apply the same process to each subinterval.

4. **Recursion Depth Control**: To prevent infinite recursion, set a maximum recursion depth. If this depth is exceeded, the method will stop and return the current approximation.

The implementation uses the following structure:

- `simpsons_rule(f, a, b)`: Computes the integral of `f` over \([a, b]\) using Simpson's Rule.
- `adaptive_aux(f, a, b, tol, whole, max_recursion_depth, depth)`: Recursively applies Simpson's Rule to subintervals, adjusting the tolerance and controlling recursion depth.
- `adaptive_simpsons(f, a, b, tol, max_recursion_depth)`: Initializes the process and returns the final approximation.

By dynamically adjusting the interval sizes, the Adaptive Simpson's Method provides a more accurate result compared to the standard Simpson's Rule, especially for functions with varying behavior over the interval.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please create an issue or submit a pull request.

