# Conclusion and perspectives {-}

It is clear that NumPy allows to perform very sophisticated calculation on multi-dimensional data, in a very consise piece of code and rather efficiently. These are clearly strong points in favour of using of NumPy, together with the large collection of tools which come along. All these tools form a very handy and powerful ecosystem for a lot of studies that can be performed in data analysis and numerical computation fields.

However, in my opinion, this ecosystem is not always scalable to large data samples on which event-by-event complex calculations have to be executed. The fundamental reason is of course that python is not compiled but the implicit comparison here is done with C++ and more specifically ROOT software, fully designed for particle physics (while NumPy is not, so the fairness of the comparison is debatable even if conclusions remain relevant). In order to illustrate these limitations with concrete cases taken from these notes, one could focus on the three following points.

+ **Code readability.** Manipulating multi-dimensional NumPy arrays using slicing and indexing can become quite difficult to read at some point. Indeed, one needs to exactly remember how the data are stored, *i.e.* the meaning of each axis. This can be clear when one writes the code, but can become slightly convoluted when re-reading its own code few months later. The typical following lines of code might illustrate this difficulty:
```python
j1, j2 = jet_pairs[:, :, 0, :], jet_pairs[:, :, 1, :]
mjj = j1[..., 0]*j2[..., 0]
      * (np.cosh(j1[..., 1]-j2[..., 1])-np.cos(j1[..., 2]-j2[..., 2])))
```

+ **Computation methodology.** The strength of NumPy clearly relies on the vectorized computations, which requires to eradicate explicit *for* loops. If this is sometimes nicer to not have loops (shorter/clearer code), it might make life difficult for any arbitrary type of computations. The example discussed in these note of making every possible pairs of objects per event is probably a good illustration. Indeed, one had to really think how to implement the pair combinatorics in a vectorized way without *for* loops, and the solution might not always be straightforward. This effort might be redone every time there is a new complex computation that comes up.


+ **Memory.** The final point which limits this ecosystem for large and complex computations is the memory management. This wasn't mentioned at all in these note but it can quickly become a limitation *if we use the existing tools out-of-the-box*. When data are loaded, the RAM of the computer is used and if the initial data sample is large *and* complex calculations are performed (creation of intermediate arrays), the saturation of the RAM arrives rather quickly. It's one of the reason why the notebooks of these notes cannot all be ran into `mybinder` (issue of "dead kernel").
