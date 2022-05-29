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

  def test_checkout_single_inputs(self):
    sku_input = ["A"]
    assert checkout_solution.checkout(sku_input) == 50
  
    sku_input = ["B"]
    assert checkout_solution.checkout(sku_input) == 30

    sku_input = ["C"]
    assert checkout_solution.checkout(sku_input) == 20

    sku_input = ["D"]
    assert checkout_solution.checkout(sku_input) == 15

  def test_checkout_no_deals(self):
    sku_input = ["A", "B", "C", "D"]
    assert checkout_solution.checkout(sku_input) == (50 + 30 + 20 + 15)
    
    sku_input = ["A", "B", "C", "C"]    
    assert checkout_solution.checkout(sku_input) == (50 + 30 + 20 + 20)

    sku_input = ["A", "A", "C", "C"]    
    assert checkout_solution.checkout(sku_input) == (50 + 50 + 20 + 20)

  def test_checkout_deals_with_A(self):
    sku_input = ["A", "A", "A", "B"]
    assert checkout_solution.checkout(sku_input) == (130 + 30)

  def test_checkout_deals_with_B(self):
    sku_input = ["A", "A", "B", "B"]
    assert checkout_solution.checkout(sku_input) == (50 + 50 + 45)
    
  def test_checkout_invalid_input(self):
    sku_input = ["a"]
    assert checkout_solution.checkout(sku_input) == -1

    sku_input = ["01"]
    assert checkout_solution.checkout(sku_input) == -1

