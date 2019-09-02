# Arrays

Arrays is a small library of array utility functions compiled for personal needs. There's 
nothing too fancy nor anything you can't find from another library, but Arrays consists of
smaller functions to be used rather than relying on larger packages.

Functions include things like chunk, contains all, diff, swap, remove all, etc

## Personal Note

Arrays is only on Github because I reference it in other projects. I don't have any plans 
to maintain this project, but I will update it from time to time. 

# Install

You can install this project directly from Github via:

```bash
$ pip3.7 install git+https://github.com/kelmore5/python-array-utilities.git
```

### Dependencies

- Python 3.7

# Usage

Once installed, you can import the main class like so:

    >>> from kelmore_arrays import ArrayTools as Arrays
    >>>
    >>> w = [1, 2, None, 4, 5]
    >>> x = [1, 2, 3, 4]
    >>> y = [3, 4, 5, 6]
    >>> z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>>
    >>> Arrays.check.any_none(w)                # True
    >>> Arrays.check.all_not_null(w)            # False
    >>>
    >>> Arrays.transform.chunk(z, 2)            # [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    >>> Arrays.transform.complement(x, y)       # [1, 2]
    >>> Arrays.transform.diff(x, y)             # [1, 2, 5, 6]
    .
    .
    .

# Documentation

To be updated
