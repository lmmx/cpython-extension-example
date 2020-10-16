# C extension example

Following the guide by Dan Foreman-Mackey ([Python modules in C](https://dfm.io/posts/python-c-extensions/), 2012)
with edits found [here](https://gist.github.com/douglas-larocca/099bf7460d853abb7c17) (posted in the
comments below Dan's tutorial).

A module is called using the command:

```sh
python setup.py build_ext --inplace
```

The original code used the deprecated NumPy API, and to use the current API requires some changes to
the code, which I've implemented separately

- [Example code](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#example) from the NumPy
  docs was informative on how to use the `PyArrayObject` type (rather than the `PyObject` in the old
  API)
- [shap](https://github.com/slundberg/shap/blob/master/shap/_cext.cc) also gives a useful example of
  using the new NumPy API ("an interface for a fast Tree SHAP implementation" in machine learning
  explainability)

To test the code, the example given by Dan is

```py
import _chi2
_chi2.chi2(2.0, 1.0, [-1.0, 4.2, 30.6], [-1.5, 8.0, 63.0], [1.0, 1.5, 0.6])
```
