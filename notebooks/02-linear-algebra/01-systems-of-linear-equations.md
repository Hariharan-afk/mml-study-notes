# 2.1 Systems of Linear Equations

## Big Picture

A **system of linear equations** is a collection of equations that must all be true at the same time.

A single linear equation gives one constraint.
A system of linear equations gives multiple constraints.

Solving the system means finding values of the unknown variables that satisfy every constraint simultaneously.

In machine learning, this idea appears everywhere: fitting linear models, solving least-squares problems, understanding feature redundancy, and studying when data constraints are consistent or inconsistent.

---

## 1. What Is a Linear Equation?

A linear equation is an equation where the unknown variables appear only to the first power and are not multiplied by each other.

For example,

$$
2x_1 + 3x_2 = 8
$$

is linear because $x_1$ and $x_2$ appear only as scaled terms.

But the following are not linear:

$$
x_1^2 + x_2 = 5
$$

$$
x_1x_2 = 7
$$

$$
\sin(x_1) + x_2 = 3
$$

A general linear equation with $n$ unknowns looks like

$$
a_1x_1 + a_2x_2 + \cdots + a_nx_n = b
$$

where:

* $x_1, x_2, \ldots, x_n$ are the unknowns,
* $a_1, a_2, \ldots, a_n$ are known coefficients,
* $b$ is the known right-hand side.

---

## 2. What Is a System of Linear Equations?

A system of $m$ linear equations with $n$ unknowns has the form

$$
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1
$$

$$
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2
$$

$$
\vdots
$$

$$
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
$$

Compactly, for each equation $i$,

$$
a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n = b_i
$$

where

$$
i = 1, 2, \ldots, m
$$

and

$$
j = 1, 2, \ldots, n.
$$

The goal is to find

$$
(x_1, x_2, \ldots, x_n)
$$

such that all $m$ equations are true at the same time.

---

## 3. Intuition

A system of linear equations is like a set of conditions.

Each equation says:

> “The unknowns must combine in this specific way to produce this specific value.”

A solution is a choice of unknowns that satisfies all conditions simultaneously.

For example, suppose

$$
x_1 + x_2 = 10
$$

and

$$
2x_1 + x_2 = 14.
$$

The first equation says the two quantities add up to $10$.
The second equation says twice the first quantity plus the second equals $14$.

Subtracting the first equation from the second gives

$$
x_1 = 4.
$$

Then

$$
x_2 = 6.
$$

So the solution is

$$
(x_1, x_2) = (4, 6).
$$

This pair works because it satisfies both equations:

$$
4 + 6 = 10
$$

and

$$
2(4) + 6 = 14.
$$

---

## 4. Three Possible Outcomes

A real-valued system of linear equations can have only three types of solution behavior:

1. No solution
2. Exactly one solution
3. Infinitely many solutions

It cannot have exactly two, exactly three, or any other finite number of solutions.

---

## 5. Case 1: No Solution

Consider

$$
x_1 + x_2 = 5
$$

and

$$
2x_1 + 2x_2 = 12.
$$

The second equation has the same left-hand side pattern as twice the first equation.

If

$$
x_1 + x_2 = 5,
$$

then multiplying both sides by $2$ gives

$$
2x_1 + 2x_2 = 10.
$$

But the second equation says

$$
2x_1 + 2x_2 = 12.
$$

That is impossible.

So the system has **no solution**.

### Intuition

The equations contradict each other.

One equation says the variables must behave one way.
Another equation demands something incompatible.

---

## 6. Case 2: Exactly One Solution

Consider

$$
x_1 + x_2 = 10
$$

and

$$
2x_1 + x_2 = 14.
$$

Subtract the first equation from the second:

$$
(2x_1 + x_2) - (x_1 + x_2) = 14 - 10
$$

so

$$
x_1 = 4.
$$

Substitute into the first equation:

$$
4 + x_2 = 10
$$

so

$$
x_2 = 6.
$$

Therefore, the unique solution is

$$
(x_1, x_2) = (4, 6).
$$

### Intuition

The constraints are independent enough to pin down one exact answer.

---

## 7. Case 3: Infinitely Many Solutions

Consider

$$
x_1 + x_2 = 5
$$

and

$$
2x_1 + 2x_2 = 10.
$$

The second equation is just twice the first equation.

So it does not give new information.

The system is really just

$$
x_1 + x_2 = 5.
$$

We can choose one variable freely.

Let

$$
x_1 = t.
$$

Then

$$
x_2 = 5 - t.
$$

So the solution set is

$$
(x_1, x_2) = (t, 5 - t), \quad t \in \mathbb{R}.
$$

There are infinitely many solutions because $t$ can be any real number.

Examples:

$$
(0, 5), (1, 4), (2, 3), (10, -5)
$$

are all valid solutions.

### Intuition

The system does not provide enough independent information to determine one exact answer.

At least one variable remains free.

---

## 8. Why Can’t a Linear System Have Exactly Two Solutions?

Suppose a system has two different solutions:

$$
x
$$

and

$$
y.
$$

That means

$$
Ax = b
$$

and

$$
Ay = b.
$$

Now take any point between them:

$$
z = (1 - t)x + ty
$$

where

$$
t \in \mathbb{R}.
$$

Then

$$
Az = A((1 - t)x + ty).
$$

Using linearity,

$$
Az = (1 - t)Ax + tAy.
$$

Since $Ax = b$ and $Ay = b$,

$$
Az = (1 - t)b + tb.
$$

So

$$
Az = b.
$$

Therefore, every point on the line through $x$ and $y$ is also a solution.

So if there are two distinct solutions, there must be infinitely many solutions.

That is why a linear system can have no solution, one solution, or infinitely many solutions — but not exactly two.

---

## 9. Geometric Interpretation

### Two Variables

In two variables, each linear equation represents a line.

For example,

$$
x_1 + x_2 = 5
$$

is a line in the $x_1x_2$-plane.

A system of two linear equations means we are looking for the intersection of two lines.

There are three possibilities:

### 1. Lines intersect at one point

Then the system has exactly one solution.

Example:

$$
x_1 + x_2 = 10
$$

$$
2x_1 + x_2 = 14
$$

The lines meet at one point:

$$
(4, 6).
$$

### 2. Lines are parallel

Then the system has no solution.

Example:

$$
x_1 + x_2 = 5
$$

$$
x_1 + x_2 = 8
$$

These equations describe parallel lines that never meet.

### 3. Lines are the same

Then the system has infinitely many solutions.

Example:

$$
x_1 + x_2 = 5
$$

$$
2x_1 + 2x_2 = 10
$$

Both equations describe the same line.

Every point on that line is a solution.

---

## 10. Three Variables

In three variables, each linear equation represents a plane.

A system of linear equations asks where the planes intersect.

The solution set can be:

* empty,
* a single point,
* a line,
* a plane.

For example, if three planes meet at one common point, the system has a unique solution.

If two equations are redundant, the intersection may be a line.

If the planes are inconsistent, there may be no common intersection.

---

## 11. Matrix Form

Systems of linear equations can be written compactly using matrices.

The general system

$$
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1
$$

$$
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2
$$

$$
\vdots
$$

$$
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
$$

can be written as

$$
Ax = b
$$

where

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix},
$$

$$
x =
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix},
$$

and

$$
b =
\begin{bmatrix}
b_1 \\
b_2 \\
\vdots \\
b_m
\end{bmatrix}.
$$

Here:

* $A$ is the coefficient matrix,
* $x$ is the vector of unknowns,
* $b$ is the right-hand-side vector.

---

## 12. Row View

In the row view, each row of $A$ gives one equation.

If the first row of $A$ is

$$
[a_{11}, a_{12}, \ldots, a_{1n}],
$$

then the first equation is

$$
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1.
$$

So each row is one constraint.

This is useful when thinking geometrically:

* one row gives one line in 2D,
* one row gives one plane in 3D,
* one row gives one hyperplane in higher dimensions.

---

## 13. Column View

In the column view, the system

$$
Ax = b
$$

can be understood as

$$
x_1a_1 + x_2a_2 + \cdots + x_na_n = b,
$$

where $a_1, a_2, \ldots, a_n$ are the columns of $A$.

This means:

> Find weights $x_1, x_2, \ldots, x_n$ so that the columns of $A$ combine to produce $b$.

This view is extremely important in linear algebra and machine learning.

For example, if

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 1
\end{bmatrix},
\quad
x =
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix},
\quad
b =
\begin{bmatrix}
8 \\
9
\end{bmatrix},
$$

then

$$
Ax = b
$$

means

$$
x_1
\begin{bmatrix}
1 \\
3
\end{bmatrix}
+
x_2
\begin{bmatrix}
2 \\
1
\end{bmatrix}
=============

\begin{bmatrix}
8 \\
9
\end{bmatrix}.
$$

So we are asking:

> What combination of the two column vectors gives the target vector $b$?

---

## 14. Original Example: Coffee Shop Ingredient Planning

Suppose a coffee shop makes two drinks:

* latte,
* mocha.

Let

$$
x_1 = \text{number of lattes}
$$

and

$$
x_2 = \text{number of mochas}.
$$

Each latte uses:

* 2 units of milk,
* 1 unit of espresso.

Each mocha uses:

* 1 unit of milk,
* 2 units of espresso.

Suppose the shop wants to use exactly:

* 11 units of milk,
* 10 units of espresso.

Then the system is

$$
2x_1 + x_2 = 11
$$

$$
x_1 + 2x_2 = 10.
$$

From the first equation,

$$
x_2 = 11 - 2x_1.
$$

Substitute into the second equation:

$$
x_1 + 2(11 - 2x_1) = 10.
$$

So

$$
x_1 + 22 - 4x_1 = 10.
$$

Then

$$
-3x_1 = -12.
$$

Therefore,

$$
x_1 = 4.
$$

Now substitute back:

$$
2(4) + x_2 = 11
$$

so

$$
x_2 = 3.
$$

The solution is

$$
(x_1, x_2) = (4, 3).
$$

So the shop should make 4 lattes and 3 mochas.

---

## 15. Machine Learning Connection

### Linear Regression as an Approximate Linear System

In linear regression, we often try to fit a model of the form

$$
X\theta = y.
$$

Here:

* $X$ is the data matrix,
* $\theta$ is the vector of model parameters,
* $y$ is the vector of target values.

This looks exactly like a system of linear equations.

But in real data, the system is often not exactly solvable because data contains noise.

So instead of solving

$$
X\theta = y
$$

exactly, linear regression solves

$$
X\theta \approx y.
$$

That means we look for parameters $\theta$ that make the predictions as close as possible to the observed targets.

This is one reason systems of linear equations are foundational for machine learning.

---

## 16. Feature Redundancy and Infinite Solutions

In machine learning, columns of the data matrix often represent features.

If one feature is a perfect combination of other features, then the system may have redundant information.

For example, suppose a dataset has these features:

$$
\text{total price}
$$

and

$$
\text{price before tax}.
$$

If total price is always calculated directly from price before tax, then the two features are strongly dependent.

This can cause the model parameters to become non-unique.

In linear algebra language, the system may have infinitely many solutions.

In machine learning language, the model may have identifiability problems or multicollinearity.

---

## 17. Inconsistent Data and No Exact Solution

Suppose a dataset gives contradictory information.

For the same input, it gives two different target values.

Then an exact linear system may have no solution.

In machine learning, this is normal because real-world data is noisy.

Instead of demanding a perfect solution, we usually search for the best approximate solution.

This leads to least squares and linear regression.

---

## 18. Common Confusions

### Confusion 1: More equations always means fewer solutions

More equations usually add more constraints, but not always.

If an added equation is redundant, it does not reduce the solution set.

Example:

$$
x_1 + x_2 = 5
$$

and

$$
2x_1 + 2x_2 = 10
$$

represent the same constraint.

The second equation adds no new information.

---

### Confusion 2: Same number of equations and unknowns means unique solution

A system with $n$ equations and $n$ unknowns does not automatically have a unique solution.

For example,

$$
x_1 + x_2 = 5
$$

$$
2x_1 + 2x_2 = 10
$$

has two equations and two unknowns, but infinitely many solutions.

Similarly,

$$
x_1 + x_2 = 5
$$

$$
2x_1 + 2x_2 = 12
$$

has two equations and two unknowns, but no solution.

The number of equations matters, but independence and consistency matter more.

---

### Confusion 3: A redundant equation is useless

A redundant equation does not change the solution set, but it can reveal structure.

In data science, redundancy can indicate repeated information or dependent features.

---

### Confusion 4: No solution means we cannot do anything

No exact solution does not mean the problem is useless.

In machine learning, many systems have no exact solution because of noisy data.

Instead, we solve an approximate problem.

That is the foundation of least-squares regression.

---

### Confusion 5: Matrix notation changes the problem

Writing

$$
Ax = b
$$

does not create a new problem.

It is just a compact way to represent the same system of equations.

The matrix form makes it easier to reason about large systems, implement algorithms, and connect the problem to geometry.

---

## 19. Key Takeaways

A system of linear equations is a set of linear constraints that must be satisfied simultaneously.

A solution is a vector of unknown values that satisfies every equation.

A real-valued linear system can have:

* no solution,
* exactly one solution,
* infinitely many solutions.

Geometrically:

* in two variables, equations are lines,
* in three variables, equations are planes,
* in higher dimensions, equations are hyperplanes.

The compact form is

$$
Ax = b.
$$

The row view treats each equation as a constraint.

The column view treats the solution as weights for combining the columns of $A$ to produce $b$.

Machine learning often uses systems of linear equations directly or approximately, especially in linear regression and least-squares problems.
