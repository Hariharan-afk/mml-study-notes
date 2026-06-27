---

title: "2.4 Vector Spaces"
description: "Understanding vector spaces, groups, vector subspaces, closure, and why these structures matter in machine learning."
---

# 2.4 Vector Spaces

## Why This Section Matters

So far, we have worked with vectors and matrices mostly as arrays of numbers.

But linear algebra is not only about arrays.

It is about **structured spaces** where objects can be added and scaled in a consistent way.

A **vector space** is the mathematical structure that tells us what it means for a collection of objects to behave like vectors.

This matters because many machine learning objects can be treated as vectors:

* data points,
* feature vectors,
* model parameters,
* images,
* word embeddings,
* audio signals,
* functions,
* matrices.

The key idea is:

> A vector space is a set of objects where addition and scalar multiplication make sense and keep us inside the same set.

---

## 1. The Big Idea

A vector is not just an arrow.

A vector can be any object that supports two operations:

1. vector addition,
2. scalar multiplication.

For example, if $x$ and $y$ are vectors, then

$$
x + y
$$

should also be a vector of the same type.

If $\lambda$ is a scalar, then

$$
\lambda x
$$

should also be a vector of the same type.

!!! intuition
    A vector space is a safe playground for vectors. If you add vectors or scale them, you never leave the playground.

---

## 2. Why Do We Need Formal Rules?

Informally, we know that vectors can be added and scaled.

But mathematics needs precision.

For example, if we say “vectors can be added,” we must also ask:

* Does the result stay in the same set?
* Is addition associative?
* Is there a zero vector?
* Does every vector have an additive inverse?
* Does scalar multiplication behave consistently?

These rules make vector spaces reliable.

---

## 3. Groups: A Small Detour

Before defining vector spaces, the book introduces the idea of a **group**.

A group is a mathematical structure that describes a set of objects together with an operation that combines two objects from the set.

### Operation

An **operation** is a rule that takes two elements and combines them to produce another element.

For a set $G$, we write an operation as

$$
\otimes : G \times G \to G.
$$

This means for elements:

$$
x,y \in G
$$

the result of the operation is 

$$
x \otimes y \in G
$$

Here, $\otimes$ is a general symbol for an operation. Depending on the context, it could represent addition, multiplication, matrix multiplication, function composition, or something else.

---

### Definition of a Group

A **group** is a pair

$$
(G,\otimes),
$$

where:

* $G$ is a set,
* $\otimes$ is an operation on $G$,

such that the following four properties hold.

---

#### Property 1: Closure

For all

$$
x,y \in G,
$$

we must have

$$
x \otimes y \in G.
$$

This means combining two elements of the set must keep us inside the same set.

---

#### Property 2: Associativity

For all

$$
x,y,z \in G,
$$

we must have

$$
(x \otimes y) \otimes z = x \otimes (y \otimes z).
$$

This means grouping does not change the result.

---

#### Property 3: Neutral Element

There must exist an element

$$
e \in G
$$

such that for every

$$
x \in G,
$$

we have

$$
x \otimes e = x
$$

and

$$
e \otimes x = x.
$$

The element $e$ is called the **neutral element** or **identity element**.

---

#### Property 4: Inverse Element

For every

$$
x \in G,
$$

there must exist an element

$$
y \in G
$$

such that

$$
x \otimes y = e
$$

and

$$
y \otimes x = e.
$$

The element $y$ is called the **inverse element** of $x$.

It is often written as

$$
x^{-1}.
$$

!!! warning
    The inverse depends on the operation.

    It does not always mean the reciprocal $\frac{1}{x}$.

    For addition, the inverse of $x$ is $-x$ because

    $$
    x + (-x) = 0.
    $$

    For multiplication, the inverse of $x$ is $\frac{1}{x}$ because

    $$
    x \cdot \frac{1}{x} = 1.
    $$

---

### Example: Real Numbers with Addition

Now let us consider an example to verify the above 4 properties.

Consider the set of real numbers with ordinary addition, denoted as

$$
(\mathbb{R}, +)
$$

is a group.

Here:

* the set is $\mathbb{R}$, the set of real numbers,
* the operation is $+$, ordinary addition.

So in this example,

$$
G = \mathbb{R}
$$

and

$$
\otimes = +.
$$

#### 1. Closure

Take any two real numbers

$$
x,y \in \mathbb{R}.
$$

Their sum is also a real number:

$$
x + y \in \mathbb{R}.
$$

For example,

$$
2 + 5 = 7,
$$

and $7$ is still a real number.

So closure holds.

#### 2. Associativity

For any real numbers

$$
x,y,z \in \mathbb{R},
$$

addition satisfies

$$
(x+y)+z = x+(y+z).
$$

For example,

$$
(2+5)+3 = 7+3 = 10,
$$

and

$$
2+(5+3) = 2+8 = 10.
$$

Both groupings give the same result.

So associativity holds.

#### 3. Neutral Element

For addition, the neutral element is

$$
0.
$$

For any real number

$$
x \in \mathbb{R},
$$

we have

$$
x + 0 = x
$$

and

$$
0 + x = x.
$$

For example,

$$
5 + 0 = 5.
$$

So the neutral element exists.

#### 4. Inverse Element

For addition, the inverse of a real number $x$ is

$$
-x.
$$

This is because

$$
x + (-x) = 0
$$

and

$$
(-x) + x = 0.
$$

For example, the inverse of $5$ under addition is $-5$ because

$$
5 + (-5) = 0.
$$

So every real number has an inverse under addition.

All four properties are satisfied. Hence,
$$ (\mathbb{R}, +) $$
is a group.

---

## 4. Abelian Group

A group is called **Abelian** if the order of operation does not matter.

That means

$$
x + y = y + x.
$$

For example,

$$
(\mathbb{R}, +)
$$

is Abelian because

$$
2 + 5 = 5 + 2.
$$

Vector addition is expected to behave like this.

If $x$ and $y$ are vectors, then

$$
x + y = y + x.
$$

!!! intuition
    Abelian means “order does not matter.”

---

## 5. What Is a Vector Space?

A **vector space** is a set $V$ with two operations:

1. addition of vectors,
2. multiplication of vectors by scalars.

We write a vector space as

$$
V = (V, +, \cdot).
$$

Here:

* $V$ is the set of vectors,
* $+$ is vector addition,
* $\cdot$ is scalar multiplication.

For a real-valued vector space, the scalars come from

$$
\mathbb{R} (\text{real numbers}).
$$

---

## 6. Vector Space Rules

A set $V$ is a vector space if it satisfies the following ideas.

### Addition Rules

For vectors $x,y,z \in V$:

$$
x + y \in V
$$

$$
x + y = y + x
$$

$$
(x+y)+z = x+(y+z)
$$

There must be a zero vector $0 \in V$ such that

$$
x + 0 = x.
$$

Every vector $x$ must have an additive inverse $-x$ such that

$$
x + (-x) = 0.
$$

### Scalar Multiplication Rules

For scalars $\lambda,\psi \in \mathbb{R}$ and vectors $x,y \in V$:

$$
\lambda x \in V
$$

$$
\lambda(x+y) = \lambda x + \lambda y
$$

$$
(\lambda+\psi)x = \lambda x + \psi x
$$

$$
\lambda(\psi x) = (\lambda \psi)x
$$

$$
1x = x.
$$

!!! intuition
    These rules guarantee that adding, scaling, and combining vectors behaves predictably.

---

## 7. Examples of Vector Spaces

### 7.1. $\mathbb{R}^n$ Is a Vector Space

More generally,

$$
\mathbb{R}^n
$$

is a vector space.

A vector in $\mathbb{R}^n$ looks like

$$
x =
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}.
$$

Vector addition is component-wise:

$$
x+y =
\begin{bmatrix}
x_1+y_1 \\
x_2+y_2 \\
\vdots \\
x_n+y_n
\end{bmatrix}.
$$

Scalar multiplication is also component-wise:

$$
\lambda x =
\begin{bmatrix}
\lambda x_1 \\
\lambda x_2 \\
\vdots \\
\lambda x_n
\end{bmatrix}.
$$

---

### 7.2. Matrices Can Form Vector Spaces

Matrices of the same shape also form vector spaces.

For example,

$$
\mathbb{R}^{2 \times 2}
$$

is the set of all real-valued $2 \times 2$ matrices.

If

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

and

$$
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix},
$$

then

$$
A+B =
\begin{bmatrix}
6 & 8 \\
10 & 12
\end{bmatrix}.
$$

This is still a $2 \times 2$ matrix.

If

$$
\lambda = 2,
$$

then

$$
2A =
\begin{bmatrix}
2 & 4 \\
6 & 8
\end{bmatrix}.
$$

This is also still a $2 \times 2$ matrix.

Therefore,

$$
\mathbb{R}^{2 \times 2}
$$

is a vector space.

!!! intuition
    Matrices can be treated as vectors because we can add them and scale them while staying inside the same set.

---

### 7.3. Polynomials Can Form Vector Spaces

Vectors do not always have to look like columns of numbers.

Polynomials can also form vector spaces.

Consider the set of all polynomials of degree at most 2:

$$
p(t) = a + bt + ct^2.
$$

If

$$
p(t) = 1 + 2t + 3t^2
$$

and

$$
q(t) = 4 + t - t^2,
$$

then

$$
p(t) + q(t) =
5 + 3t + 2t^2.
$$

This is still a polynomial of degree at most 2.

If

$$
\lambda = 3,
$$

then

$$
3p(t) = 3 + 6t + 9t^2.
$$

This is also still a polynomial of degree at most 2.

So this set is a vector space.

!!! intuition
    A vector is not defined by how it looks. It is defined by how it behaves under addition and scaling.

---

## 8. What Is Closure?

Closure means that an operation keeps us inside the same set.

For vector spaces, closure means:

### Closure under addition

If

$$
x,y \in V,
$$

then

$$
x+y \in V.
$$

### Closure under scalar multiplication

If

$$
x \in V
$$

and

$$
\lambda \in \mathbb{R},
$$

then

$$
\lambda x \in V.
$$

!!! intuition
    Closure means the operation does not throw us outside the space.

---

## 9. Vector Subspaces

A **vector subspace** is a smaller vector space inside a larger vector space.

If

$$
U \subseteq V
$$

and $U$ is itself a vector space using the same addition and scalar multiplication as $V$, then $U$ is a subspace of $V$.

---

### Subspace Test

To check whether a nonempty subset $U$ is a subspace of $V$, we only need to check:

1. the zero vector is in $U$,
2. $U$ is closed under addition,
3. $U$ is closed under scalar multiplication.

Equivalently:

If

$$
x,y \in U
$$

and

$$
\lambda \in \mathbb{R},
$$

then

$$
x+y \in U
$$

and

$$
\lambda x \in U.
$$

---
## 10. Examples and Non-Examples of Subspaces
### 10.1. A Line Through the Origin Is a Subspace

Consider the line

$$
U =
\left\{
\begin{bmatrix}
t \\
2t
\end{bmatrix}
:
t \in \mathbb{R}
\right\}.
$$

This is a line through the origin in $\mathbb{R}^2$.

Check the subspace conditions.

#### Zero vector

Choose

$$
t=0.
$$

Then

$$
\begin{bmatrix}
t \\
2t
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}.
$$

So $0 \in U$.

#### Closure under addition

Take

$$
x =
\begin{bmatrix}
s \\
2s
\end{bmatrix}
$$

and

$$
y =
\begin{bmatrix}
t \\
2t
\end{bmatrix}.
$$

Then

$$
x+y =
\begin{bmatrix}
s+t \\
2s+2t
\end{bmatrix}
=
\begin{bmatrix}
s+t \\
2(s+t)
\end{bmatrix}.
$$

This is still in $U$.

#### Closure under scalar multiplication

Take

$$
\lambda \in \mathbb{R}.
$$

Then

$$
\lambda x =
\lambda
\begin{bmatrix}
s \\
2s
\end{bmatrix}
=
\begin{bmatrix}
\lambda s \\
2\lambda s
\end{bmatrix}.
$$

This is still in $U$.

Therefore, $U$ is a subspace of $\mathbb{R}^2$.

---

### 10.2. A Line Not Through the Origin Is Not a Subspace

Consider

$$
U =
\left\{
\begin{bmatrix}
t \\
2t+1
\end{bmatrix}
:
t \in \mathbb{R}
\right\}.
$$

This is a line in $\mathbb{R}^2$, but it does not pass through the origin.

To be a subspace, $U$ must contain the zero vector.

Can we find $t$ such that

$$
\begin{bmatrix}
t \\
2t+1
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}?
$$

The first coordinate gives

$$
t=0.
$$

But then the second coordinate becomes

$$
2(0)+1 = 1.
$$

So we get

$$
\begin{bmatrix}
0 \\
1
\end{bmatrix},
$$

not

$$
\begin{bmatrix}
0 \\
0
\end{bmatrix}.
$$

Therefore, the zero vector is not in $U$.

So $U$ is not a subspace.

!!! intuition
    A line must pass through the origin to be a subspace.

---

### 10.3. Homogeneous Systems Create Subspaces

The solution set of a homogeneous system

$$
Ax = 0
$$

is always a subspace.

Why?

Let $x$ and $y$ be two solutions.

That means

$$
Ax = 0
$$

and

$$
Ay = 0.
$$

Now check addition:

$$
A(x+y) = Ax + Ay = 0 + 0 = 0.
$$

So $x+y$ is also a solution.

Now check scalar multiplication:

$$
A(\lambda x) = \lambda Ax = \lambda 0 = 0.
$$

So $\lambda x$ is also a solution.

Therefore, the solution set of

$$
Ax=0
$$

is closed under addition and scalar multiplication.

So it is a subspace.

---

### 10.4. Inhomogeneous Systems Usually Do Not Create Subspaces

The solution set of

$$
Ax=b,
\quad b \neq 0,
$$

is generally not a subspace.

Why?

A subspace must contain the zero vector.

But if

$$
x=0,
$$

then

$$
A0 = 0.
$$

So $x=0$ cannot solve

$$
Ax=b
$$

unless

$$
b=0.
$$

Therefore, when $b \neq 0$, the solution set is shifted away from the origin.

It may be a line or plane, but it is not a subspace.

!!! intuition
    Homogeneous solution sets pass through the origin. Inhomogeneous solution sets are usually shifted away from the origin.

---

## 11. Geometric Interpretation

In $\mathbb{R}^2$:

* the zero vector ${0}$ is a subspace,
* any line through the origin is a subspace,
* the whole plane $\mathbb{R}^2$ is a subspace.

A line not through the origin is not a subspace.

In $\mathbb{R}^3$:

* the zero vector ${0}$ is a subspace,
* any line through the origin is a subspace,
* any plane through the origin is a subspace,
* the whole space $\mathbb{R}^3$ is a subspace.

A plane not through the origin is not a subspace.

!!! intuition
    Geometrically, subspaces are flat spaces that pass through the origin.

---

## 12. Machine Learning Connection

Vector spaces matter in machine learning because they provide the mathematical setting in which data, parameters, and transformations live.

A data point is often represented as a vector in a space such as

$$
\mathbb{R}^D.
$$

For example, if a house is described using size, number of bedrooms, and age, then it can be represented as a vector in

$$
\mathbb{R}^3.
$$

Subspaces become important when we want to represent high-dimensional data using a smaller set of directions.

This idea appears later in dimensionality reduction methods such as PCA, where data is approximated using a lower-dimensional subspace.

!!! intuition
    A vector space is the universe of possible vectors. A subspace is a smaller structured region inside that universe.

---

<!-- ## 22. Common Confusions

### Confusion 1: Every set of vectors is a vector space

No.

A vector space must satisfy specific rules.

Most importantly, it must be closed under addition and scalar multiplication.

For example, the set of vectors with only positive entries is not a vector space because multiplying by a negative scalar leaves the set.

---

### Confusion 2: Every line is a subspace

No.

Only lines that pass through the origin are subspaces.

A line not passing through the origin does not contain the zero vector, so it cannot be a subspace.

---

### Confusion 3: A vector must be a column of numbers

No.

A vector can be any object that supports addition and scalar multiplication.

Examples include:

* geometric arrows,
* arrays of numbers,
* matrices,
* polynomials,
* functions,
* signals.

The object matters less than the operations it supports.

---

### Confusion 4: Subspace means smaller dimension only

Not always.

A subspace can be the entire vector space itself.

For every vector space $V$, both

$$
V
$$

and

$$
{0}
$$

are subspaces.

These are called trivial subspaces.

---

### Confusion 5: Inhomogeneous solution sets are subspaces

Usually no.

The solution set of

$$
Ax=0
$$

is a subspace.

But the solution set of

$$
Ax=b,
\quad b \neq 0,
$$

is generally not a subspace because it usually does not contain the zero vector.

--- -->

## 10. Summary

A vector space is a set of objects that can be added and scaled while staying inside the same set.

The two main operations are:

$$
x+y
$$

and

$$
\lambda x.
$$

A vector space must satisfy rules such as closure, associativity, distributivity, existence of a zero vector, and existence of additive inverses.

Examples of vector spaces include:

* $\mathbb{R}^n$,
* matrices of a fixed shape,
* polynomials of bounded degree,
* certain function spaces.

A subspace is a vector space inside another vector space.

To check whether a subset is a subspace, verify:

1. it contains the zero vector,
2. it is closed under addition,
3. it is closed under scalar multiplication.

The solution set of

$$
Ax=0
$$

is always a subspace.

The solution set of

$$
Ax=b,
\quad b \neq 0,
$$

is generally not a subspace.

Geometrically, subspaces are flat spaces that pass through the origin.

Vector spaces and subspaces are foundational for machine learning because data, models, embeddings, gradients, and low-dimensional representations often live inside vector spaces.

---

## 11. Quick Check

1. What are the two operations required for a vector space?
2. What does closure mean?
3. Why is $\mathbb{R}^n$ a vector space?
4. Why are matrices of fixed shape a vector space?
5. Why is the set of positive vectors not a vector space?
6. What is a vector subspace?
7. Why must every subspace contain the zero vector?
8. Why is a line through the origin a subspace?
9. Why is a line not through the origin not a subspace?
10. Why is the solution set of $Ax=0$ a subspace?
11. Why is the solution set of $Ax=b$, $b \neq 0$, generally not a subspace?
12. How do subspaces appear in machine learning?

---

## 12. Key Formula Sheet

Vector addition:

$$
x+y \in V
$$

Scalar multiplication:

$$
\lambda x \in V
$$

Closure under addition:

$$
x,y \in V
\implies
x+y \in V
$$

Closure under scalar multiplication:

$$
x \in V,\ \lambda \in \mathbb{R}
\implies
\lambda x \in V
$$

Distributivity over vector addition:

$$
\lambda(x+y)=\lambda x+\lambda y
$$

Distributivity over scalar addition:

$$
(\lambda+\psi)x = \lambda x + \psi x
$$

Scalar associativity:

$$
\lambda(\psi x) = (\lambda \psi)x
$$

Neutral scalar:

$$
1x=x
$$

Subspace test:

$$
0 \in U
$$

$$
x,y \in U \implies x+y \in U
$$

$$
x \in U,\ \lambda \in \mathbb{R} \implies \lambda x \in U
$$

Homogeneous solution subspace:

$$
{x \in \mathbb{R}^n : Ax=0}
$$

Inhomogeneous solution set, generally not a subspace:

$$
{x \in \mathbb{R}^n : Ax=b,\ b\neq 0}
$$
