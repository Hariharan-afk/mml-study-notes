---

title: "2.2 Matrices"
description: "Understanding matrices, matrix operations, matrix multiplication, inverse, transpose, and their role in machine learning."
---

# 2.2 Matrices

## Why This Section Matters

In the previous section, we studied systems of linear equations.

For example,

$$
2x_1 + 3x_2 + 5x_3 = 1
$$

$$
4x_1 - 2x_2 - 7x_3 = 8
$$

$$
9x_1 + 5x_2 - 3x_3 = 2.
$$

Writing many equations like this quickly becomes messy.

Matrices give us a compact and powerful way to store the coefficients of a system of equations. Instead of writing every equation separately, we can write the whole system as

$$
Ax = b.
$$

where, 

$$
A = 
\begin{bmatrix}
2 & 3 & 5 \\
4 & -2 & -7 \\
9 & 5 & -3
\end{bmatrix}, 
$$ 

$$ 
x = 
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}, 
$$ 

and

$$ 
b = 
\begin{bmatrix}
1 \\
8 \\
2
\end{bmatrix}. 
$$ 


Matrices are not just notation. They are one of the main objects in linear algebra and machine learning.

In machine learning, matrices are used to represent:

* datasets,
* images,
* word embeddings,
* model weights,
* linear transformations,
* neural network layers,
* covariance matrices,
* attention scores,
* batches of data.

---

## 1. What Is a Matrix?

A **matrix** is a rectangular arrangement of numbers.

For example,

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

is a matrix with 2 rows and 3 columns.

We say

$$
A \in \mathbb{R}^{2 \times 3}.
$$

This means $A$ is a real-valued matrix with 2 rows and 3 columns.

!!! intuition
A matrix is a structured table of numbers. The structure matters because rows and columns often have different meanings.

---

## 2. Matrix Shape

If a matrix has $m$ rows and $n$ columns, we write

$$
A \in \mathbb{R}^{m \times n}.
$$

A general matrix looks like

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}.
$$

The entry $a_{ij}$ means:

* $i$ tells us the row,
* $j$ tells us the column.

So $a_{23}$ means the entry in row 2, column 3.

!!! note
Matrix indexing in mathematics usually starts at 1. In Python and NumPy, indexing starts at 0.

---

## 3. Rows and Columns

A matrix has two natural views.

### Row View

Each row can represent one observation, one equation, or one constraint.

For example,

$$
A =
\begin{bmatrix}
2 & 3 & 5 \\
4 & -2 & -7 \\
9 & 5 & -3
\end{bmatrix}
$$

has rows

$$
[2,3,5],
$$

$$
[4,-2,-7],
$$

and

$$
[9,5,-3].
$$

In a system of equations, each row contains the coefficients of one equation.

---

### Column View

Each column can represent one variable, one feature, or one direction.

For the same matrix,

$$
A =
\begin{bmatrix}
2 & 3 & 5 \\
4 & -2 & -7 \\
9 & 5 & -3
\end{bmatrix},
$$

the columns are

$$
\begin{bmatrix}
2 \\
4 \\
9
\end{bmatrix},
\quad
\begin{bmatrix}
3 \\
-2 \\
5
\end{bmatrix},
\quad
\begin{bmatrix}
5 \\
-7 \\
-3
\end{bmatrix}.
$$

In machine learning, columns often represent features.

!!! intuition
Rows often describe examples or constraints. Columns often describe features or directions.

---

## 4. Row Vectors and Column Vectors

A matrix with one row is called a **row vector**.

Example:

$$
r =
\begin{bmatrix}
1 & 2 & 3
\end{bmatrix}
\in \mathbb{R}^{1 \times 3}.
$$

A matrix with one column is called a **column vector**.

Example:

$$
x =
\begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}
\in \mathbb{R}^{3 \times 1}.
$$

In this chapter, vectors are usually written as column vectors.

---

## 5. Matrices as Data Tables

Matrices are natural for storing tabular data.

Suppose we have three houses and two features:

* size in square feet,
* number of bedrooms.

We can store the dataset as

$$
X =
\begin{array}{cl}
  \begin{array}{cc}
    \text{size} & \text{bedrooms}
  \end{array} & \\
  \begin{bmatrix}
    1200 & 2 \\
    1800 & 3 \\
    2400 & 4
  \end{bmatrix} &
  \begin{array}{l}
    \text{house 1} \\
    \text{house 2} \\
    \text{house 3}
  \end{array}
\end{array}
$$

Here:

* each row is one house,
* each column is one feature.

So

$$
X \in \mathbb{R}^{3 \times 2}.
$$

This is exactly how many machine learning datasets are represented.

!!! example
If a dataset has 1000 examples and 20 features, its data matrix has shape

$$
X \in \mathbb{R}^{1000 \times 20}.
$$

---

## 6. Matrix Addition

Two matrices can be added only if they have the same shape.

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
10 & 20 \\
30 & 40
\end{bmatrix},
$$

then

$$
A + B =
\begin{bmatrix}
1+10 & 2+20 \\
3+30 & 4+40
\end{bmatrix}
=

\begin{bmatrix}
11 & 22 \\
33 & 44
\end{bmatrix}.
$$

Matrix addition is an element-wise operation.
<br>

In general, if

$$
A, B \in \mathbb{R}^{m \times n},
$$

then

$$
A + B \in \mathbb{R}^{m \times n}.
$$

The entry-wise rule is

$$
(A+B)_{ij} = A_{ij} + B_{ij}.
$$

!!! warning
You cannot add matrices with different shapes.


For example,

$$
\mathbb{R}^{2 \times 3} + \mathbb{R}^{3 \times 2}
$$

is not defined.


---

## 7. Scalar Multiplication

A matrix can be multiplied by a scalar.

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
\lambda = 3,
$$

then

$$
\lambda A =
3
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
=

\begin{bmatrix}
3 & 6 \\
9 & 12
\end{bmatrix}.
$$

Every entry is scaled by the scalar.
<br>

In general,

$$
\lambda (A)_{ij} = \lambda A_{ij}.
$$

!!! intuition
Scalar multiplication stretches or shrinks every entry of the matrix by the same factor.

---

## 8. Matrix Multiplication

Matrix multiplication is more subtle than matrix addition.

Suppose

$$
A \in \mathbb{R}^{m \times n}
$$

and

$$
B \in \mathbb{R}^{n \times k}.
$$

Then the product

$$
AB
$$

is defined, and

$$
AB \in \mathbb{R}^{m \times k}.
$$

The inner dimensions must match:

$$
(m \times n)(n \times k) = m \times k.
$$

The result has the outer dimensions.

!!! intuition
Matrix multiplication combines rows of the first matrix with columns of the second matrix.

### Entry-Wise Formula for Matrix Multiplication

Let

$$
C = AB.
$$

Then the entry $c_{ij}$ is computed as

$$
c_{ij} =
\sum_{\ell=1}^{n} a_{i\ell}b_{\ell j}.
$$

This means:

> To compute entry $(i,j)$ of $C$, multiply row $i$ of $A$ with column $j$ of $B$ and sum the products.

### Worked Example: Matrix Multiplication

Let

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
3 & 2 & 1
\end{bmatrix}
\in \mathbb{R}^{2 \times 3}
$$

and

$$
B =
\begin{bmatrix}
0 & 2 \\
1 & -1 \\
0 & 1
\end{bmatrix}
\in \mathbb{R}^{3 \times 2}.
$$

Since $A$ is $2 \times 3$ and $B$ is $3 \times 2$, the product $AB$ is defined.

The result will be a $2 \times 2$ matrix.

Compute each entry.

First row, first column:

$$
1(0) + 2(1) + 3(0) = 2.
$$

First row, second column:

$$
1(2) + 2(-1) + 3(1) = 3.
$$

Second row, first column:

$$
3(0) + 2(1) + 1(0) = 2.
$$

Second row, second column:

$$
3(2) + 2(-1) + 1(1) = 5.
$$

Therefore,

$$
AB =
\begin{bmatrix}
2 & 3 \\
2 & 5
\end{bmatrix}.
$$

---

## 9. Matrix Multiplication Is Not Element-Wise

A common mistake is to think that matrix multiplication means multiplying entries in the same position.

That is not matrix multiplication.

For example, if

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
10 & 20 \\
30 & 40
\end{bmatrix},
$$

then matrix multiplication is

$$
AB =
\begin{bmatrix}
1(10)+2(30) & 1(20)+2(40) \\
3(10)+4(30) & 3(20)+4(40)
\end{bmatrix}
=

\begin{bmatrix}
70 & 100 \\
150 & 220
\end{bmatrix}.
$$

The element-wise product would be

$$
A \odot B =
\begin{bmatrix}
1(10) & 2(20) \\
3(30) & 4(40)
\end{bmatrix}
=

\begin{bmatrix}
10 & 40 \\
90 & 160
\end{bmatrix}.
$$

These are different operations.

!!! warning
Matrix multiplication and element-wise multiplication are not the same.


In NumPy:

```python
A @ B
```

performs matrix multiplication, while

```python
A * B
```

performs element-wise multiplication.


---

## 10. Matrix Multiplication Is Not Commutative

For real numbers,

$$
ab = ba.
$$

But for matrices, generally,

$$
AB \neq BA.
$$

Sometimes $AB$ is defined but $BA$ is not even defined.

Example:

$$
A \in \mathbb{R}^{2 \times 3},
\quad
B \in \mathbb{R}^{3 \times 2}.
$$

Then

$$
AB \in \mathbb{R}^{2 \times 2},
$$

but

$$
BA \in \mathbb{R}^{3 \times 3}.
$$

Both products exist, but they have different shapes.

So they cannot be equal.

!!! intuition
Matrix multiplication represents ordered operations. Changing the order usually changes the result.

---

## 11. Identity Matrix

The **identity matrix** is the matrix version of the number 1.

For example,

$$
I_3 =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}.
$$

Multiplying a matrix by the identity matrix leaves it unchanged.

If

$$
A \in \mathbb{R}^{m \times n},
$$

then

$$
I_m A = A
$$

and

$$
A I_n = A.
$$

Notice the sizes:

* $I_m$ goes on the left,
* $I_n$ goes on the right.

!!! intuition
The identity matrix does nothing. It preserves the matrix it multiplies.

---

## 12. Matrix Inverse

For a nonzero real number $a$, the inverse is

$$
a^{-1} = \frac{1}{a}
$$

because

$$
aa^{-1} = 1.
$$

For a square matrix $A$, the inverse matrix $A^{-1}$ is defined by

$$
AA^{-1} = I
$$

and

$$
A^{-1}A = I.
$$

Only square matrices can have inverses.

A matrix that has an inverse is called **invertible** or **nonsingular**.

A matrix that does not have an inverse is called **singular** or **noninvertible**.

!!! warning
Not every square matrix has an inverse.

### Example of a Matrix Inverse

Let

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}.
$$

The inverse is

$$
A^{-1}
=

\begin{bmatrix}
-2 & 1 \\
\frac{3}{2} & -\frac{1}{2}
\end{bmatrix}.
$$

Check:

$$
AA^{-1}
=

\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\begin{bmatrix}
-2 & 1 \\
\frac{3}{2} & -\frac{1}{2}
\end{bmatrix}.
$$

Compute:

$$
AA^{-1}
=

\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
=

I_2.
$$

So $A^{-1}$ really undoes $A$.

!!! intuition
If a matrix represents an operation, its inverse represents the operation that reverses it.

### Inverse of a 2 by 2 Matrix

For

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix},
$$

the inverse is

$$
A^{-1}
=

\frac{1}{ad-bc}
\begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix},
$$

as long as

$$
ad - bc \neq 0.
$$

The quantity

$$
ad - bc
$$

is the determinant of the matrix.
<br>

If

$$
ad - bc = 0,
$$

then the matrix has no inverse.

---

## 13. Transpose

The **transpose** of a matrix switches rows and columns.

If

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix},
$$

then

$$
A^\top =
\begin{bmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{bmatrix}.
$$

So if

$$
A \in \mathbb{R}^{m \times n},
$$

then

$$
A^\top \in \mathbb{R}^{n \times m}.
$$

!!! intuition
The transpose flips the matrix across its main diagonal.

---

## 14. Inverse and Transpose Properties

The inverse and transpose have several useful properties:

$$
AA^{-1} = I = A^{-1}A
$$

$$
(AB)^{-1} = B^{-1}A^{-1}
$$

$$
(A+B)^{-1} \neq A^{-1} + B^{-1}
$$

$$
(A^\top)^\top = A
$$

$$
(A + B)^\top = A^\top + B^\top
$$

$$
(AB)^\top = B^\top A^\top
$$


!!! Important
When inverting or transposing matrix products, **reverse the order**.

---

## 15. Symmetric Matrices

A square matrix is **symmetric** if

$$
A = A^\top.
$$

Example:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
2 & 5 & 4 \\
3 & 4 & 9
\end{bmatrix}.
$$

This matrix is symmetric because the entries mirror across the main diagonal.

The top-right entry equals the bottom-left entry, and so on.

!!! intuition
A symmetric matrix contains mirrored information across its diagonal.

Symmetric matrices appear often in machine learning, especially in covariance matrices, kernel matrices, and second-derivative matrices.

---

## 16. Compact Representation of Linear Systems

Consider the system

$$
2x_1 + 3x_2 + 5x_3 = 1
$$

$$
4x_1 - 2x_2 - 7x_3 = 8
$$

$$
9x_1 + 5x_2 - 3x_3 = 2.
$$

This can be written as

$$
\begin{bmatrix}
2 & 3 & 5 \\
4 & -2 & -7 \\
9 & 5 & -3
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}
=

\begin{bmatrix}
1 \\
8 \\
2
\end{bmatrix}.
$$

So the compact form is

$$
Ax = b.
$$

Here,

$$
A =
\begin{bmatrix}
2 & 3 & 5 \\
4 & -2 & -7 \\
9 & 5 & -3
\end{bmatrix},
$$

$$
x =
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix},
$$

and

$$
b =
\begin{bmatrix}
1 \\
8 \\
2
\end{bmatrix}.
$$

---

## 17. Column Interpretation of Matrix-Vector Multiplication

The product

$$
Ax
$$

can be understood as a weighted combination of the columns of $A$.

If

$$
A =
\begin{bmatrix}
2 & 3 & 5 \\
4 & -2 & -7 \\
9 & 5 & -3
\end{bmatrix},
$$

then

$$
Ax
==

x_1
\begin{bmatrix}
2 \\
4 \\
9
\end{bmatrix}
+
x_2
\begin{bmatrix}
3 \\
-2 \\
5
\end{bmatrix}
+
x_3
\begin{bmatrix}
5 \\
-7 \\
-3
\end{bmatrix}.
$$

So solving

$$
Ax = b
$$

means finding weights $x_1,x_2,x_3$ so that the columns of $A$ combine to produce $b$.

!!! intuition
Matrix-vector multiplication asks: how do we combine the columns of the matrix?

---

## 18. Geometric Interpretation

Matrices can be interpreted geometrically in two important ways.

### Matrix as a Collection of Vectors

A matrix can be viewed as a set of column vectors.

For example,

$$
A =
\begin{bmatrix}
1 & 2 \\
0 & 1
\end{bmatrix}
$$

has columns

$$
a_1 =
\begin{bmatrix}
1 \\
0
\end{bmatrix},
\quad
a_2 =
\begin{bmatrix}
2 \\
1
\end{bmatrix}.
$$

The product

$$
Ax
$$

combines these columns:

$$
Ax = x_1a_1 + x_2a_2.
$$

So the columns of $A$ define the directions we can combine.

---

### Matrix as a Transformation

A matrix can also be viewed as a function that transforms one vector into another vector.

For example,

$$
A =
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix}
$$

maps

$$
x =
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
$$

to

$$
Ax =
\begin{bmatrix}
2x_1 \\
x_2
\end{bmatrix}.
$$

This stretches the vector horizontally by a factor of 2 and keeps the vertical direction unchanged.

!!! intuition
A matrix can move, stretch, rotate, shear, or project vectors depending on its entries.

---

## 19. Original Example: Student Scores Matrix

Suppose three students take two exams.

Their scores are:

| Student | Exam 1 | Exam 2 |
| ------- | -----: | -----: |
| A       |     80 |     90 |
| B       |     70 |     85 |
| C       |     95 |     88 |

We can store this as a matrix:

$$
X =
\begin{bmatrix}
80 & 90 \\
70 & 85 \\
95 & 88
\end{bmatrix}.
$$

Here,

$$
X \in \mathbb{R}^{3 \times 2}.
$$

Each row is a student.
Each column is an exam.

Suppose the final grade is calculated as:

* 40% Exam 1,
* 60% Exam 2.

Then the weight vector is

$$
w =
\begin{bmatrix}
0.4 \\
0.6
\end{bmatrix}.
$$

The final grades are

$$
Xw.
$$

Compute:

$$
Xw =
\begin{bmatrix}
80 & 90 \\
70 & 85 \\
95 & 88
\end{bmatrix}
\begin{bmatrix}
0.4 \\
0.6
\end{bmatrix}
=

\begin{bmatrix}
86 \\
79 \\
90.8
\end{bmatrix}.
$$

So the final grades are:

$$
86,\quad 79,\quad 90.8.
$$

This is a simple example of matrix-vector multiplication.

---

## 20. Machine Learning Connections

### Data Matrix

In machine learning, we often store data in a matrix

$$
X \in \mathbb{R}^{N \times D}.
$$

Here:

| Symbol | Meaning               |
| ------ | --------------------- |
| $N$    | number of data points |
| $D$    | number of features    |
| $X$    | data matrix           |

Each row is one data point.

Each column is one feature.

---

### Linear Regression

Linear regression uses the form

$$
X\theta \approx y.
$$

Here:

* $X$ is the data matrix,
* $\theta$ is the parameter vector,
* $y$ is the target vector.

The product

$$
X\theta
$$

computes predictions.

Each prediction is a weighted combination of the input features.

---

### Neural Network Layers

A fully connected neural network layer often has the form

$$
z = Wx + b.
$$

Here:

* $x$ is the input vector,
* $W$ is a weight matrix,
* $b$ is a bias vector,
* $z$ is the output vector.

The matrix $W$ determines how input features are mixed to produce output features.

---

### Images as Matrices

A grayscale image can be represented as a matrix of pixel intensities.

For example, a $28 \times 28$ grayscale image can be represented as

$$
X \in \mathbb{R}^{28 \times 28}.
$$

Each entry stores the brightness of one pixel.

Color images are often represented using multiple matrices, one for each color channel.

---

### Embedding Matrices

In natural language processing, words or tokens can be represented using embeddings.

An embedding matrix may look like

$$
E \in \mathbb{R}^{V \times d},
$$

where:

* $V$ is the vocabulary size,
* $d$ is the embedding dimension.

Each row stores the vector representation of one token.

---

## 21. Common Confusions

### Confusion 1: A matrix is just a table

A matrix can be stored as a table, but mathematically it is more than that.

A matrix can represent:

* a system of equations,
* a linear transformation,
* a dataset,
* a feature map,
* a model parameter object.

So a matrix is both a storage structure and an algebraic object.

---

## 22. Summary

A matrix is a rectangular array of numbers.

A matrix with $m$ rows and $n$ columns has shape

$$
m \times n.
$$

We write

$$
A \in \mathbb{R}^{m \times n}.
$$

Matrix addition is element-wise and requires equal shapes.

Scalar multiplication scales every entry.

Matrix multiplication combines rows of the first matrix with columns of the second matrix.

If

$$
A \in \mathbb{R}^{m \times n}
$$

and

$$
B \in \mathbb{R}^{n \times k},
$$

then

$$
AB \in \mathbb{R}^{m \times k}.
$$

The identity matrix behaves like the number 1.

The inverse matrix, when it exists, reverses the effect of a matrix.

The transpose flips rows and columns.

A symmetric matrix satisfies

$$
A = A^\top.
$$

Systems of linear equations can be written compactly as

$$
Ax = b.
$$

Matrices are central to machine learning because they represent data, model weights, transformations, images, embeddings, and linear systems.

---

## 23. Quick Check

1. What does the shape $m \times n$ mean?
2. When can two matrices be added?
3. When is matrix multiplication $AB$ defined?
4. If $A \in \mathbb{R}^{4 \times 3}$ and $B \in \mathbb{R}^{3 \times 2}$, what is the shape of $AB$?
5. Why is matrix multiplication not the same as element-wise multiplication?
6. What does the identity matrix do?
7. What does the inverse of a matrix do?
8. What does the transpose of a matrix do?
9. What does it mean for a matrix to be symmetric?
10. How is the matrix form $Ax=b$ connected to systems of linear equations?

---

## 24. Key Formula Sheet

Matrix shape:

$$
A \in \mathbb{R}^{m \times n}
$$

Matrix addition:

$$
(A+B)*{ij} = A*{ij} + B_{ij}
$$

Scalar multiplication:

$$
(\lambda A)*{ij} = \lambda A*{ij}
$$

Matrix multiplication:

$$
C = AB
$$

$$
c_{ij} =
\sum_{\ell=1}^{n} a_{i\ell}b_{\ell j}
$$

Shape rule:

$$
(m \times n)(n \times k) = m \times k
$$

Identity matrix:

$$
I_mA = A,
\quad
AI_n = A
$$

Inverse matrix:

$$
AA^{-1} = I,
\quad
A^{-1}A = I
$$

Transpose:

$$
(A^\top)^\top = A
$$

$$
(AB)^\top = B^\top A^\top
$$

Symmetric matrix:

$$
A = A^\top
$$

Compact system representation:

$$
Ax = b
$$

Column interpretation:

$$
Ax = x_1a_1 + x_2a_2 + \cdots + x_na_n
$$

Linear regression form:

$$
X\theta \approx y
$$

Neural network layer:

$$
z = Wx + b
$$
