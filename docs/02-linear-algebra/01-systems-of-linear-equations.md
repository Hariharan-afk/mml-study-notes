# Systems of Linear Equations

> Status: Draft  
> Source: Mathematics for Machine Learning, Chapter 2, Section 2.1

## 1. Why this topic matters

Systems of linear equations are one of the starting points of linear algebra.

They appear whenever we need to find unknown quantities that must satisfy multiple linear constraints at the same time.

## 2. Intuition

A single linear equation restricts the possible values of unknown variables.

A system of linear equations asks:

> Which values satisfy all equations simultaneously?

Depending on the equations, we may get:

- no solution,
- exactly one solution,
- infinitely many solutions.

## 3. Formal form

A general system of linear equations can be written as:

$$
a_{11}x_1 + \cdots + a_{1n}x_n = b_1
$$

$$
\vdots
$$

$$
a_{m1}x_1 + \cdots + a_{mn}x_n = b_m
$$

This can be written compactly as:

$$
A\mathbf{x} = \mathbf{b}
$$

where \(A\) is the coefficient matrix, \(\mathbf{x}\) is the vector of unknowns, and \(\mathbf{b}\) is the right-hand-side vector.

## 4. Simple example

Consider:

$$
x_1 + x_2 = 3
$$

$$
x_1 - x_2 = 1
$$

Adding both equations gives:

$$
2x_1 = 4
$$

So:

$$
x_1 = 2
$$

Substituting into the first equation:

$$
2 + x_2 = 3
$$

Therefore:

$$
x_2 = 1
$$

The solution is:

$$
\mathbf{x} =
\begin{bmatrix}
2 \\
1
\end{bmatrix}
$$

## 5. Geometric interpretation

In two variables, each linear equation represents a line.

Solving a system means finding where the lines intersect.

- If the lines intersect at one point, there is one solution.
- If the lines are parallel, there is no solution.
- If the lines are the same line, there are infinitely many solutions.

In three variables, each linear equation represents a plane.

## 6. Machine learning connection

In machine learning, a similar structure appears in linear regression.

Instead of writing:

$$
A\mathbf{x} = \mathbf{b}
$$

we often write:

$$
X\mathbf{w} = \mathbf{y}
$$

where:

- \(X\) is the feature matrix,
- \(\mathbf{w}\) is the vector of model weights,
- \(\mathbf{y}\) is the vector of target values.

In real datasets, we usually cannot solve this exactly because data is noisy.

So we look for an approximate solution:

$$
X\mathbf{w} \approx \mathbf{y}
$$

This leads to the least-squares problem:

$$
\min_{\mathbf{w}} \|X\mathbf{w} - \mathbf{y}\|^2
$$

## 7. Common confusion

A system having infinitely many solutions does not mean that the equations are useless.

It means that the equations do not provide enough independent information to determine one unique solution.

## 8. Python / NumPy demo

```python
import numpy as np

A = np.array([
    [1, 1],
    [1, -1]
])

b = np.array([3, 1])

x = np.linalg.solve(A, b)

print(x)
```

```python
Expected Output:
[2. 1.]
```

## 9. Summary
- A system of linear equations asks for values that satisfy multiple equations simultaneously.
- The compact matrix form is $Ax = b$.
- A system can have no solution, one solution, or infinitely many solutions.
- In ML, this structure appears in linear regression as $Xw \approx y$.