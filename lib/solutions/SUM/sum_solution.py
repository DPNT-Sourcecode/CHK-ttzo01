# noinspection PyShadowingBuiltins,PyUnusedLocal
LOWER_BOUND_INCLUSIVE = 0
UPPER_BOUND_EXCLUSIVE = 101

SUM_RANGE = range(LOWER_BOUND_INCLUSIVE, UPPER_BOUND_EXCLUSIVE)

def compute(x: int, y: int):
  if x in SUM_RANGE and y in SUM_RANGE:
    return x + y
  else:
    raise ValueError(f"Sum inputs not in range {SUM_RANGE}, x {x}, y {y}")


