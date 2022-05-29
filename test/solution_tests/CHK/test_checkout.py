from solutions.CHK import checkout_solution

from pytest import raises

class TestSum():
  def test_checkout_no_deals(self):
    input = ["A", "B", "C"]
    assert checkout_solution.compute(input) == 