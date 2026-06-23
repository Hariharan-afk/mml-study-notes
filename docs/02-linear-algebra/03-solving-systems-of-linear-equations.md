---

title: "2.3 Solving Systems of Linear Equations"
description: "Understanding how to solve linear systems using particular solutions, homogeneous solutions, row operations, row-echelon form, and Gaussian elimination."
---

# 2.3 Solving Systems of Linear Equations

## Why This Section Matters

In the previous sections, we learned that a system of linear equations can be written compactly as

$$
Ax = b.
$$

Now we want to solve it.

That means we want to find the unknown vector

$$
x
$$

such that multiplying it by the matrix $A$ gives the vector $b$.

In other words, we are asking:

> What values of the unknowns satisfy all equations at the same time?

This section introduces the main ideas behind solving linear systems:

* particular solutions,
* homogeneous systems,
* general solutions,
* elementary row operations,
* augmented matrices,
* row-echelon form,
* reduced row-echelon form,
* Gaussian elimination,
* matrix inverse computation.

These ideas are foundational for linear algebra, linear regression, optimization, numerical computing, and machine learning.

---

## 1. The Problem: Solving $Ax=b$

A system of linear equations can be written as

$$
Ax = b,
$$

where

$$
A \in \mathbb{R}^{m \times n},
$$

$$
x \in \mathbb{R}^{n},
$$

and

$$
b \in \mathbb{R}^{m}.
$$

Here:

| Symbol | Meaning                |
| ------ | ---------------------- |
| $A$    | coefficient matrix     |
| $x$    | unknown vector         |
| $b$    | right-hand-side vector |

For example,

$$
\begin{bmatrix}
1 & 1 \\
2 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
=
\begin{bmatrix}
5 \\
8
\end{bmatrix}
$$

represents the system

$$
x_1 + x_2 = 5
$$

$$
2x_1 + x_2 = 8.
$$

Solving the system gives

$$
x_1 = 3,
\quad
x_2 = 2.
$$

So

$$
x =
\begin{bmatrix}
3 \\
2
\end{bmatrix}.
$$
This is a simple example of a system of linear equations. For more complex systems, we need more sophisticated methods like Gaussian elimination, which will be covered in the later part of this section. However, the underlying principles remain the same.

!!! intuition
    Solving $Ax=b$ means finding the input vector $x$ that the matrix $A$ maps to the output vector $b$.

---

## 2. Three Possible Solution Behaviors

A linear system can have:

1. no solution,
2. exactly one solution,
3. infinitely many solutions.

This section focuses on how to systematically find the solution set.

Before diving into the Gaussian elimination, let's understand some basic concepts that are essential for solving linear systems.

---

## 3. Particular Solution 

A **particular solution** to a system of linear equations is any single, specific assignment of values to the variables that satisfies all equations in the system simultaneously.

In simpler terms, a **particular solution** is one specific solution to

$$
Ax = b.
$$

It is usually written as

$$
x_p.
$$

If

$$
Ax_p = b,
$$

then $x_p$ is a particular solution.

For example, consider

$$
x_1 + x_2 = 5.
$$

One particular solution is

$$
x_p =
\begin{bmatrix}
5 \\
0
\end{bmatrix},
$$

because

$$
5 + 0 = 5.
$$

But this is not the only solution for this system. Another particular solution would be

$$
\begin{bmatrix}
3 \\
2
\end{bmatrix}.
$$

So a particular solution is not necessarily unique.

!!! intuition
    A particular solution is just one valid answer. It does not always describe all possible answers.

---

## 4. Homogeneous System

A **homogeneous system** of linear equations is a set of equations where all of the constant terms on the right side of the equals sign are zero. 

It has the form

$$
Ax = 0.
$$

The right-hand side is the zero vector.

For example,

$$
x_1 + x_2 = 0
$$

is homogeneous.

One obvious solution is

$$
x = 0
$$

as it always satisfies

$$
Ax = 0.
$$

This is called the **trivial solution**.

But sometimes there are nonzero, or non-trivial, solutions too.

For example,

$$
x_1 + x_2 = 0
$$

has infinitely many solutions:

$$
x_1 = t,
\quad
x_2 = -t,
\quad
t \in \mathbb{R}.
$$

So

$$
x =
\begin{bmatrix}
t \\
-t
\end{bmatrix}
=
t
\begin{bmatrix}
1 \\
-1
\end{bmatrix}.
$$

!!! intuition
    The homogeneous system $Ax=0$ tells us which directions are collapsed to zero by $A$.

---

## 5. General Solution

If a system

$$
Ax = b
$$

has at least one solution, then the full solution set can be written as

$$
x = x_p + x_h,
$$

where:

| Symbol | Meaning                                       |
| ------ | --------------------------------------------- |
| $x_p$  | one particular solution to $Ax=b$             |
| $x_h$  | any solution to the homogeneous system $Ax=0$ |

So the general solution is

$$
\text{general solution}
=
\text{particular solution}
+
\text{homogeneous solution}.
$$

### Why This Works

Suppose

$$
Ax_p = b
$$

and

$$
Ax_h = 0.
$$

Then

$$
A(x_p + x_h)
=
Ax_p + Ax_h.
$$

Substitute:

$$
A(x_p + x_h)
= b + 0
= b.
$$

Therefore,

$$
x_p + x_h
$$

is also a solution to $Ax=b$.

!!! intuition
    It may seem paradoxical that adding something that equals zero changes the solution. 

    Don't just focus on the output $b$. We are here to find all the inputs $x$ that produce the desired output $b$.

    The particular solution gives one valid point. The homogeneous solutions give the directions in which we can move without changing $Ax=b$.

### Example

Consider the system

$$
x_1 + x_2 + x_3 = 6.
$$

This is one equation with three unknowns, so we expect infinitely many solutions.

A particular solution is

$$
x_p =
\begin{bmatrix}
6 \\
0 \\
0
\end{bmatrix}.
$$

Now solve the homogeneous system:

$$
x_1 + x_2 + x_3 = 0.
$$

Let

$$
x_2 = s,
\quad
x_3 = t.
$$

Then

$$
x_1 = -s - t.
$$

So

$$
x_h =
\begin{bmatrix}
-s-t \\
s \\
t
\end{bmatrix}
=
s
\begin{bmatrix}
-1 \\
1 \\
0
\end{bmatrix}
+
t
\begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix}.
$$

Therefore, the general solution is

$$
x =
\begin{bmatrix}
6 \\
0 \\
0
\end{bmatrix}
+
s
\begin{bmatrix}
-1 \\
1 \\
0
\end{bmatrix}
+
t
\begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix},
\quad
s,t \in \mathbb{R}.
$$

This describes all solutions.

!!! Intuition
    So the general approach to solving a system of linear equations consists of 3 steps:

    1. Find a particular solution.
    2. Solve the homogeneous system.
    3. Combine the two.

---

## 6. Geometric Interpretation of General Solutions

The equation

$$
x_1 + x_2 + x_3 = 6
$$

represents a plane in three-dimensional space.

The homogeneous equation

$$
x_1 + x_2 + x_3 = 0
$$

is a plane through the origin.

The particular solution

$$
x_p =
\begin{bmatrix}
6 \\
0 \\
0
\end{bmatrix}
$$

shifts the homogeneous solution plane away from the origin.

So the solution set of

$$
Ax=b
$$

can be understood as a shifted version of the solution set of

$$
Ax=0.
$$

!!! intuition
    Homogeneous solutions describe directions. A particular solution shifts those directions to the correct location.

---

## 7. Elementary Row Operations

To solve a system systematically, we transform it into a simpler system.

The key idea is to use operations that do not change the solution set.

These are called **elementary row operations**.

The three main row operations are:

1. swap the position of any two rows,
2. multiply any row by a nonzero scalar,
3. add a multiple of any row to any other row.

For example, if we have two equations,

$$
R_1: x_1 + x_2 = 5
$$

$$
R_2: 2x_1 + x_2 = 8,
$$

we can replace $R_2$ by

$$
R_2 - 2R_1.
$$

This gives

$$
(2x_1+x_2) - 2(x_1+x_2) = 8 - 10.
$$

So

$$
-x_2 = -2.
$$

Therefore,

$$
x_2 = 2.
$$

The solution set has not changed. We only rewrote the system in a simpler way.

!!! intuition
    Row operations are legal ways to rewrite the same constraints in a simpler form - Row-Echelon Form(discussed below), so that we can solve the system easily.

---

## 8. Augmented Matrix

While solving systems of linear equations, instead of writing the variables every time, we can represent the system in the form of an **augmented matrix**.

For the system

$$
x_1 + x_2 = 5
$$

$$
2x_1 + x_2 = 8,
$$

we write

$$
\left[
\begin{array}{cc|c}
1 & 1 & 5 \\
2 & 1 & 8
\end{array}
\right].
$$

The left side contains the coefficient matrix $A$.

The right side contains the vector $b$.

So the augmented matrix is

$$
[A \mid b].
$$

!!! intuition
    An augmented matrix is a compact way to write the system $Ax=b$ without repeatedly writing the variables.

---

## 9. Row-Echelon Form (REF)

A matrix is in **row-echelon form** if it has a staircase-like structure.

For example,

$$
\left[
\begin{array}{ccc|c}
1 & 2 & 1 & 7 \\
0 & 1 & 3 & 4 \\
0 & 0 & 2 & 6
\end{array}
\right]
$$

is in row-echelon form.

The first nonzero entry in each row is called a **pivot**.

Here, the pivots are:

* column 1 in row 1,
* column 2 in row 2,
* column 3 in row 3.

The pivots move strictly to the right as we go down the rows.

!!! intuition
    Row-echelon form makes the system easier to solve because later equations contain fewer variables.

### Pivot Variables and Free Variables

Variables corresponding to pivot columns are called **basic variables** or **pivot variables**.

Variables corresponding to non-pivot columns are called **free variables**.

For example, suppose the row-echelon form is

$$
\left[
\begin{array}{ccc|c}
1 & 2 & 1 & 6 \\
0 & 1 & 3 & 4
\end{array}
\right].
$$

The pivot columns are column 1 and column 2.

So:

* $x_1$ and $x_2$ are basic variables,
* $x_3$ is a free variable.

This means $x_3$ can be chosen freely, and then $x_1$ and $x_2$ are determined from it.

For instance, 

$$R_1: x_1 + 2x_2 + x_3 = 6$$

$$R_2: x_2 + 3x_3 = 4$$

if we choose $x_3 = t$, then

$$R_1: x_1 + 2x_2 + t = 6$$

$$R_2: x_2 + 3t = 4$$

solving for $x_2$ and $x_1$ respectively, we get

$$x_2 = 4 - 3t$$

$$x_1 = -2 + 5t$$


!!! intuition
    Free variables represent degrees of freedom in the solution set.

---

## 10. Reduced Row-Echelon Form (RREF)

Reduced row-echelon form is a more refined version of row-echelon form. 
A matrix is in **reduced row-echelon form** if:

1. **It is in row-echelon form**,
2. **Every pivot is 1** (In standard REF, the pivots can be any non-zero number),
3. **Each pivot is the only nonzero entry in its column** (In REF, we only clear out entries below the pivot. In RREF, we also clear out entries above the pivot).

For example,

$$
\left[
\begin{array}{ccc|c}
1 & 0 & -5 & -2 \\
0 & 1 & 3 & 4
\end{array}
\right]
$$

is in reduced row-echelon form.

This represents

$$
x_1 - 5x_3 = -2
$$

$$
x_2 + 3x_3 = 4.
$$

Let

$$
x_3 = t.
$$

Then

$$
x_1 = -2 + 5t,
$$

$$
x_2 = 4 - 3t.
$$

So

$$
x =
\begin{bmatrix}
-2 + 5t \\
4 - 3t \\
t
\end{bmatrix}
=
\begin{bmatrix}
-2 \\
4 \\
0
\end{bmatrix}
+
t
\begin{bmatrix}
5 \\
-3 \\
1
\end{bmatrix}.
$$

!!! intuition
    Reduced row-echelon form makes the solution almost readable directly from the matrix.

---

## 11. Gaussian Elimination

**Gaussian elimination** is the process of using row operations to transform a system into row-echelon form or reduced row-echelon form.

The general strategy is:

1. write the system as an augmented matrix,
2. use row operations to create zeros below pivots,
3. obtain row-echelon form,
4. solve by back-substitution,
5. optionally continue to reduced row-echelon form.

!!! intuition
    Gaussian elimination is a systematic way to simplify a system without changing its solution set.

### Worked Example: 

Consider the system

$$
x_1 + x_2 + x_3 = 6
$$

$$
2x_1 + x_2 + x_3 = 7
$$

$$
x_1 + 3x_2 + x_3 = 10.
$$

Write the augmented matrix:

$$
\left[
\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
2 & 1 & 1 & 7 \\
1 & 3 & 1 & 10
\end{array}
\right].
$$

Use the first row as the first pivot row.

Replace $R_2$ by $R_2 - 2R_1$:

$$
R_2 =
[2,1,1,7] - 2[1,1,1,6].
$$

So

$$
R_2 = [0,-1,-1,-5].
$$

Replace $R_3$ by $R_3 - R_1$:

$$
R_3 =
[1,3,1,10] - [1,1,1,6].
$$

So

$$
R_3 = [0,2,0,4].
$$

Now the matrix becomes

$$
\left[
\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & -1 & -1 & -5 \\
0 & 2 & 0 & 4
\end{array}
\right].
$$

Multiply row 2 by $-1$:

$$
\left[
\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & 1 & 5 \\
0 & 2 & 0 & 4
\end{array}
\right].
$$

Replace $R_3$ by $R_3 - 2R_2$:

$$
R_3 =
[0,2,0,4] - 2[0,1,1,5].
$$

So

$$
R_3 = [0,0,-2,-6].
$$

Now we have

$$
\left[
\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & 1 & 5 \\
0 & 0 & -2 & -6
\end{array}
\right].
$$

This is row-echelon form.

From the third row,

$$
-2x_3 = -6.
$$

So

$$
x_3 = 3.
$$

From the second row,

$$
x_2 + x_3 = 5.
$$

Substitute $x_3 = 3$:

$$
x_2 = 2.
$$

From the first row,

$$
x_1 + x_2 + x_3 = 6.
$$

Substitute $x_2 = 2$ and $x_3 = 3$:

$$
x_1 = 1.
$$

Therefore,

$$
x =
\begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}.
$$

---

## 12. Back-Substitution

Back-substitution is the process of solving from the bottom equation upward.

For example,

$$
\left[
\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & 1 & 5 \\
0 & 0 & -2 & -6
\end{array}
\right]
$$

represents

$$
x_1 + x_2 + x_3 = 6
$$

$$
x_2 + x_3 = 5
$$

$$
-2x_3 = -6.
$$

Start with the last equation:

$$
x_3 = 3.
$$

Then move upward:

$$
x_2 + 3 = 5,
$$

so

$$
x_2 = 2.
$$

Then

$$
x_1 + 2 + 3 = 6,
$$

so

$$
x_1 = 1.
$$

!!! intuition
    Row-echelon form makes the last equation simple, then each equation above becomes simple one by one.

---

## 13. Detecting No Solution

Sometimes row operations produce a contradiction.

For example,

$$
\left[
\begin{array}{cc|c}
1 & 1 & 5 \\
0 & 0 & 3
\end{array}
\right]
$$

represents

$$
x_1 + x_2 = 5
$$

and

$$
0 = 3.
$$

This is impossible.

Therefore, the system has no solution.

!!! intuition
    A row like $[0 \quad 0 \mid c]$ with $c \neq 0$ means contradiction.

---

## 14. Detecting Infinitely Many Solutions

A system has infinitely many solutions when there is at least one free variable and no contradiction.

For example,

$$
\left[
\begin{array}{ccc|c}
1 & 2 & -1 & 3 \\
0 & 1 & 4 & 5
\end{array}
\right]
$$

has three variables but only two pivot columns.

So one variable is free.

Here, $x_3$ is free.

Let

$$
x_3 = t.
$$

From the second row,

$$
x_2 + 4x_3 = 5.
$$

So

$$
x_2 = 5 - 4t.
$$

From the first row,

$$
x_1 + 2x_2 - x_3 = 3.
$$

Substitute $x_2 = 5 - 4t$:

$$
x_1 + 2(5 - 4t) - t = 3.
$$

So

$$
x_1 + 10 - 8t - t = 3.
$$

Therefore,

$$
x_1 = -7 + 9t.
$$

The general solution is

$$
x =
\begin{bmatrix}
-7 + 9t \\
5 - 4t \\
t
\end{bmatrix}
=
\begin{bmatrix}
-7 \\
5 \\
0
\end{bmatrix}
+
t
\begin{bmatrix}
9 \\
-4 \\
1
\end{bmatrix},
\quad
t \in \mathbb{R}.
$$

---

## 15. The Minus-1 Trick

The **minus-1 trick** is a shortcut for reading the solution of a homogeneous system

$$
Ax = 0
$$

from a matrix in reduced row-echelon form.

Suppose

$$
A =
\begin{bmatrix}
1 & 3 & 0 & 0 & 3 \\
0 & 0 & 1 & 0 & 9 \\
0 & 0 & 0 & 1 & -4
\end{bmatrix}.
$$

The pivot columns are columns 1, 3, and 4.

The free columns are columns 2 and 5.

To use the minus-1 trick, add rows so that each free-variable column gets a $-1$ on the diagonal:

$$
\tilde{A}
=
\begin{bmatrix}
1 & 3 & 0 & 0 & 3 \\
0 & -1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 9 \\
0 & 0 & 0 & 1 & -4 \\
0 & 0 & 0 & 0 & -1
\end{bmatrix}.
$$

Now read the columns that contain $-1$ on the diagonal.

Column 2 gives

$$
\begin{bmatrix}
3 \\
-1 \\
0 \\
0 \\
0
\end{bmatrix}.
$$

Column 5 gives

$$
\begin{bmatrix}
3 \\
0 \\
9 \\
-4 \\
-1
\end{bmatrix}.
$$

So the solution to

$$
Ax = 0
$$

is

$$
x =
\lambda_1
\begin{bmatrix}
3 \\
-1 \\
0 \\
0 \\
0
\end{bmatrix}
+
\lambda_2
\begin{bmatrix}
3 \\
0 \\
9 \\
-4 \\
-1
\end{bmatrix},
\quad
\lambda_1,\lambda_2 \in \mathbb{R}.
$$

!!! note
    The minus-1 trick is a shortcut. It is useful after you understand free variables and reduced row-echelon form.

---

## 16. Computing the Matrix Inverse Using Gaussian Elimination

Gaussian elimination can also be used to compute the inverse of a square matrix.

To find

$$
A^{-1},
$$

we solve

$$
AX = I.
$$

This means we want a matrix $X$ such that multiplying $A$ by $X$ gives the identity matrix.

The process is:

$$
[A \mid I]
\longrightarrow
[I \mid A^{-1}].
$$

That means we augment $A$ with the identity matrix and row-reduce until the left side becomes the identity matrix.

The right side then becomes the inverse.

!!! intuition
    While bringing \(A\) to reduced row-echelon form, if the left block does not become the identity matrix, then \(A\) is not invertible. In that case, \(A\) is singular.
    

### Example: Inverse of a 2 by 2 Matrix

Let

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}.
$$

Write

$$
[A \mid I]
=
\left[
\begin{array}{cc|cc}
1 & 2 & 1 & 0 \\
3 & 4 & 0 & 1
\end{array}
\right].
$$

Replace $R_2$ by $R_2 - 3R_1$:

$$
\left[
\begin{array}{cc|cc}
1 & 2 & 1 & 0 \\
0 & -2 & -3 & 1
\end{array}
\right].
$$

Divide $R_2$ by $-2$:

$$
\left[
\begin{array}{cc|cc}
1 & 2 & 1 & 0 \\
0 & 1 & \frac{3}{2} & -\frac{1}{2}
\end{array}
\right].
$$

Replace $R_1$ by $R_1 - 2R_2$:

$$
\left[
\begin{array}{cc|cc}
1 & 0 & -2 & 1 \\
0 & 1 & \frac{3}{2} & -\frac{1}{2}
\end{array}
\right].
$$

So

$$
A^{-1}
=
\begin{bmatrix}
-2 & 1 \\
\frac{3}{2} & -\frac{1}{2}
\end{bmatrix}.
$$

---

## 17. When Can We Use $x = A^{-1}b$?

If

$$
A
$$

is square and invertible, then the solution to

$$
Ax=b
$$

is

$$
x = A^{-1}b.
$$

This works because

$$
Ax=b.
$$

Multiply both sides by $A^{-1}$:

$$
A^{-1}Ax = A^{-1}b.
$$

Since

$$
A^{-1}A = I,
$$

we get

$$
Ix = A^{-1}b.
$$

So

$$
x = A^{-1}b.
$$

!!! warning
    In practice, we usually avoid explicitly computing $A^{-1}$ for numerical reasons. Algorithms solve $Ax=b$ more directly.

---

## 18. Large Systems and Numerical Solvers

Gaussian elimination is useful and systematic.

However, for very large systems, it can become computationally expensive.

In practical numerical computing and machine learning, large linear systems are often solved using specialized algorithms such as:

* iterative methods,
* conjugate gradient methods,
* least-squares solvers,
* numerical linear algebra libraries.

The goal is usually to solve

$$
Ax=b
$$

efficiently and accurately without explicitly computing

$$
A^{-1}.
$$

!!! intuition
    In theory, inverses are elegant. In practice, direct numerical solvers are usually better.

---

## 19. Connection to Least Squares

Sometimes

$$
Ax=b
$$

has no exact solution.

This happens often in machine learning because real data is noisy.

Instead of solving

$$
Ax=b
$$

exactly, we solve an approximate problem:

$$
Ax \approx b.
$$

The most common approach is least squares:

$$
\min_x \|Ax-b\|^2.
$$

This finds the vector $x$ that makes $Ax$ as close as possible to $b$.

When $A$ has linearly independent columns, a common formula is

$$
x = (A^\top A)^{-1}A^\top b.
$$

This expression is connected to the Moore-Penrose pseudoinverse.

!!! note
    Do not worry if this least-squares formula feels unfamiliar. We will study this more deeply later when learning linear regression and projections.

---

## 20. Machine Learning Connections

!!! note
    Do not worry if some ideas in this section feel unfamiliar right now.

    The goal here is only to show why solving linear systems matters in machine learning. Topics like least squares, linear regression, optimization, and numerical solvers will be explained later in more detail and depth.

    If this section feels overwhelming, you can safely skim or skip it for now and return to it after learning the later chapters.

### Linear Regression

Linear regression often tries to solve

$$
X\theta \approx y.
$$

Here:

| Symbol   | Meaning          |
| -------- | ---------------- |
| $X$      | data matrix      |
| $\theta$ | parameter vector |
| $y$      | target vector    |

If the system had an exact solution, we could find parameters $\theta$ such that

$$
X\theta = y.
$$

But real data is usually noisy, so an exact solution may not exist.

Instead, linear regression finds the best approximate solution.

---

### Feature Redundancy

If some columns of $X$ are redundant, then the system may have infinitely many parameter vectors that give the same predictions.

For example, if one feature is exactly twice another feature, then the model may not know how to assign credit uniquely between them.

This relates to free variables and non-unique solutions.

---

### Overdetermined Systems

In machine learning, we often have more data points than features.

This gives a system with more equations than unknowns.

For example,

$$
X \in \mathbb{R}^{1000 \times 20}
$$

means we have 1000 equations and 20 unknown model parameters.

Such systems usually do not have exact solutions, so least squares is used.

---

### Numerical Stability

In machine learning libraries, we usually do not compute

$$
X^{-1}
$$

directly.

Instead, numerical solvers are used because they are more stable and efficient.

This is important for large datasets and high-dimensional models.

---

## 21. Common Confusions

### Confusion 1: A particular solution is the full answer

No.

A particular solution is only one solution.

If the system has infinitely many solutions, the full answer also needs the homogeneous solution.

The general form is

$$
x = x_p + x_h.
$$

---


## 22. Summary

Solving a linear system means finding

$$
x
$$

such that

$$
Ax=b.
$$

A particular solution is one specific solution to

$$
Ax=b.
$$

A homogeneous solution solves

$$
Ax=0.
$$

If a solution exists, the general solution can be written as

$$
x = x_p + x_h.
$$

Elementary row operations preserve the solution set.

An augmented matrix

$$
[A \mid b]
$$

compactly represents a linear system.

Row-echelon form gives a staircase structure that supports back-substitution.

Reduced row-echelon form makes solutions easier to read directly.

Gaussian elimination systematically transforms systems into simpler forms.

The minus-1 trick helps read homogeneous solutions from reduced row-echelon form.

The inverse of a matrix can be found using Gaussian elimination:

$$
[A \mid I] \to [I \mid A^{-1}].
$$

In machine learning, exact solutions often do not exist, so we use approximate methods such as least squares.

---

## 23. Quick Check

1. What does it mean to solve $Ax=b$?
2. What is a particular solution?
3. What is a homogeneous system?
4. Why can the general solution be written as $x=x_p+x_h$?
5. What are the three elementary row operations?
6. What is an augmented matrix?
7. What is a pivot?
8. What is the difference between a basic variable and a free variable?
9. What is row-echelon form?
10. What is reduced row-echelon form?
11. What is Gaussian elimination?
12. What does a row like $[0 \quad 0 \mid 5]$ mean?
13. When can we use $x=A^{-1}b$?
14. Why do numerical methods often avoid explicitly computing the inverse?
15. How is least squares connected to systems with no exact solution?

---

## 24. Key Formula Sheet

Linear system:

$$
Ax=b
$$

Homogeneous system:

$$
Ax=0
$$

Particular solution:

$$
Ax_p=b
$$

Homogeneous solution:

$$
Ax_h=0
$$

General solution:

$$
x=x_p+x_h
$$

Augmented matrix:

$$
[A \mid b]
$$

Inverse-based solution, when $A$ is square and invertible:

$$
x=A^{-1}b
$$

Inverse by Gaussian elimination:

$$
[A \mid I] \to [I \mid A^{-1}]
$$

Least-squares objective:

$$
\min_x \|Ax-b\|^2.
$$

Least-squares formula under suitable conditions:

$$
x=(A^\top A)^{-1}A^\top b
$$
