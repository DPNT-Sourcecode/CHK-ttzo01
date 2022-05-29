from solutions.CHK import checkout_solution

from pytest import raises

# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

class TestSum():
  def test_checkout_no_deals(self):
    input = ["A", "B", "C", "D"]
    assert checkout_solution.compute(input) == (50 + 30 + 20 + 15)
