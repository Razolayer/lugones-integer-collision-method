# Razolayer Integer Collision Method

Experimental exploration of compositeness detection through integer collisions between algebraic structures and compressed parameterizations.

---

# Origin of the Construction

The method emerged experimentally from visual exploration of the expressions:

```text
y² = a² - 4x
```

and

```text
y = x/b - b
```

The initial goal was not factorization itself, but studying visual collision patterns between both structures.

A significant portion of the development process involved graphical and visual analysis of the generated curves, collision points, integer regions, and geometric behavior of the system.

During experimentation, it was observed that non-trivial integer collision points appeared to correlate with composite values of `x`, while prime values tended to avoid such collisions.

Substituting:

```text
(x/b - b)² = a² - 4x
```

eventually leads to a difference-of-squares structure:

```text
a² - y² = 4x
```

which implies:

```text
(a - y)(a + y) = 4x
```

This suggests that non-trivial integer collisions induce a multiplicative decomposition of `x`.

This observation later motivated the compressed parameterization:

```text
r = sqrt(x² - 4P) - x
```

and its direct reconstruction formula.

---

# Collision Hypothesis

Central experimental hypothesis:

```text
non-trivial integer collision
=> x is composite
```

Conversely:

```text
absence of non-trivial collisions
=> x behaves as prime
```

The trivial collision corresponding to:

```text
x = 1 * x
```

is excluded from analysis.

---

# Compression Stage

During experimentation, it was observed that the relevant information could be compressed into the expression:

```text
r = sqrt(x² - 4P) - x
```

where integer values of `r` correspond to exact algebraic collisions.

Later, an optional translation constant was introduced:

```text
r = sqrt(x² - 4P) - x + C
```

The constant `C` has no effect on the underlying number-theoretic structure and is only used for visualization or range shifting purposes.

---

# Direct Form

Starting from:

```text
r = y - x
```

we obtain:

```text
y = x + r
```

Substituting:

```text
(x + r)² = x² - 4P
```

Expanding:

```text
x² + 2rx + r² = x² - 4P
```

Simplifying:

```text
2rx + r² = -4P
```

Finally:

```text
x = (-4P - r²) / (2r)
```

or equivalently:

```text
x = -r/2 - 2P/r
```

This removes the need for binary search and allows direct reconstruction of candidate values from `r`.

---

# Geometric Interpretation

The direct equation:

```text
x = -r/2 - 2P/r
```

forms a discrete hyperbolic structure.

Integer collision points correspond to exact square decompositions of:

```text
x² - 4P
```

Plotting the structure reveals:

- compressed integer regions
- sparse collision points
- possible geometric regularities

A large portion of the intuition behind the method emerged visually from analyzing these plots.

---

# Experimental Results

Example:

```python
P = 2000000014
```

Result:

```text
r = -4
x = 1000000009
y = 1000000005
```

which corresponds to:

```text
2000000014 = 2 * 1000000007
```

Execution time using the direct method:

```text
0.016 s
```

---

# Prime-Like Behavior

After excluding the trivial collision:

```text
r = -2 + C
```

the method experimentally behaves as follows:

- non-trivial integer collision
  - composite number

- no non-trivial collision
  - prime-like behavior

---

# Complexity

Current direct implementation scales approximately as:

```text
O(sqrt(P))
```

because the algorithm still scans candidate integer values of `r`.

Future work includes:

- modular restrictions
- collision density analysis
- skipping impossible regions
- geometric pruning
- alternative parameterizations

---

# Important Note

This project is exploratory and experimental.

The construction emerged independently from experimental algebraic manipulation and collision analysis before connections to classical difference-of-squares structures became apparent.

No cryptographic claims are made.

---

# Repository Structure

Suggested repository structure:

```text
README.md
main.py
plots/
examples/
docs/
```

Possible future additions:

- collision heatmaps
- density analysis
- modular filters
- GPU acceleration
- geometric pruning experiments

---

# Author

Razolayer  
Argentina  
2026
