from solutions.SUM import sum_solution

from pytest import raises

class TestSum():
  def test_sum(self):
    assert sum_solution.compute(1, 2) == 3

  def test_sum_out_of_range_raise_value_error(self):
    with raises(ValueError):
      sum_solution.compute(-1, 2)
    with raises(ValueError):
      sum_solution.compute(0, 101)
