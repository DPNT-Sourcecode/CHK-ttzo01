# noinspection PyShadowingBuiltins,PyUnusedLocal
LOWER_BOUND_INCLUSIVE = 0
UPPER_BOUND_EXCLUSIVE = 101

SUM_RANGE = range(LOWER_BOUND_INCLUSIVE, UPPER_BOUND_EXCLUSIVE)

def compute(x: int, y: int):
  if not isinstance(x, int):
    raise TypeError(f"Input x {x} incorrect type {type(x)}")

  if not isinstance(y, int):
    raise TypeError(f"Input x {y} incorrect type {type(y)}")


  if x in SUM_RANGE and y in SUM_RANGE:
    return x + y
  else:
    raise ValueError(f"Sum inputs not in range {SUM_RANGE}, x {x}, y {y}")


