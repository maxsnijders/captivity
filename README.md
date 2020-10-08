# Getting started with Captivity

The only purpose of `captivity` is to support you in writing better `pandas` code by caging in
some of its worst excentricities. `pandas` is great, but `import captivity; import pandas as pd` is better.

## Example

To find a comprehensive set of examples, check out the `captivity/tests/` directory. To pique your interest, consider the following:

```python
import pandas as pd

a = pd.DataFrame({
    "x": [1, 2], 
    "y": [3, 4]}
)

b = pd.DataFrame({
    "z": [5, 6],
    "x": [9, 0]
})

a_b = pd.concat([a, b], axis=1)

print(a_b)
>>    x  y  z  x
>> 0  1  3  5  9
>> 1  2  4  6  0 

``` 

Woa! That should definitely not be allowed by default. With `captivity`, it's not.

```python
...
a_b = pd.concat([a, b], axis=1)

>> Traceback (most recent call last):
>> ...
>> captivity.CaptivityException: Column-wise concatenation would result in duplicate column labels for column: {'x'}

```

In addition, captivity currently supports:
* **sensible checks on vertical concatenation (column sets must match)**
* **sensible checks on merges (no more `_x` and `_y` columns - but exceptions!)**
* turning `CaptivityExceptions` into `CaptivityWarnings` - useful when first using `captivity` in an existing codebase


 ## Running the tests
 
 To test `captivity`, run `pytest --cov` in the root directory of this project.
 
 ## Installation
 To install `captivity`, simply run `pip install git+https://github.com/maxsnijders/captivity.git`. 

