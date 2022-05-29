from solutions.CHK import checkout_solution

from pytest import raises

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+



class TestSum():

  def test_checkout_check_empty(self):
    sku_input = ""
    assert checkout_solution.checkout(sku_input) == 0

  def test_checkout_single_inputs(self):
    sku_input = "A"
    assert checkout_solution.checkout(sku_input) == 50
  
    sku_input = "B"
    assert checkout_solution.checkout(sku_input) == 30

    sku_input = "C"
    assert checkout_solution.checkout(sku_input) == 20

    sku_input = "D"
    assert checkout_solution.checkout(sku_input) == 15

    sku_input = "E"
    assert checkout_solution.checkout(sku_input) == 40

    sku_input = "F"
    assert checkout_solution.checkout(sku_input) == 10

    sku_input = "G"
    assert checkout_solution.checkout(sku_input) == 20

    sku_input = "H"
    assert checkout_solution.checkout(sku_input) == 10

    sku_input = "I"
    assert checkout_solution.checkout(sku_input) == 35

    sku_input = "J"
    assert checkout_solution.checkout(sku_input) == 60

    sku_input = "K"
    assert checkout_solution.checkout(sku_input) == 80

    sku_input = "L"
    assert checkout_solution.checkout(sku_input) == 90

    sku_input = "M"
    assert checkout_solution.checkout(sku_input) == 15

    sku_input = "N"
    assert checkout_solution.checkout(sku_input) == 40

    sku_input = "O"
    assert checkout_solution.checkout(sku_input) == 10

    sku_input = "P"
    assert checkout_solution.checkout(sku_input) == 50

    sku_input = "Q"
    assert checkout_solution.checkout(sku_input) == 30

    sku_input = "R"
    assert checkout_solution.checkout(sku_input) == 50

assert checkout_solution.checkout(sku_input) == 30
assert checkout_solution.checkout(sku_input) == 50
assert checkout_solution.checkout(sku_input) == 30
assert checkout_solution.checkout(sku_input) == 20
assert checkout_solution.checkout(sku_input) == 40
assert checkout_solution.checkout(sku_input) == 50
assert checkout_solution.checkout(sku_input) == 20
assert checkout_solution.checkout(sku_input) == 90
assert checkout_solution.checkout(sku_input) == 10
assert checkout_solution.checkout(sku_input) == 50


# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+


  def test_checkout_no_deals(self):
    sku_input = "ABCD"
    assert checkout_solution.checkout(sku_input) == (50 + 30 + 20 + 15)
    
    sku_input = "ABCC"    
    assert checkout_solution.checkout(sku_input) == (50 + 30 + 20 + 20)

    sku_input = "AACC"    
    assert checkout_solution.checkout(sku_input) == (50 + 50 + 20 + 20)

  def test_checkout_deals_with_A(self):
    sku_input = "AAAB"
    assert checkout_solution.checkout(sku_input) == (130 + 30)

  def test_checkout_deals_with_B(self):
    sku_input = "AABB"
    assert checkout_solution.checkout(sku_input) == (50 + 50 + 45)
    
  def test_checkout_invalid_input(self):
    sku_input = "a"
    assert checkout_solution.checkout(sku_input) == -1

    sku_input = "01"
    assert checkout_solution.checkout(sku_input) == -1

  def test_checkout_free_item_conditons(self):
    sku_input = "EEBEE"
    assert checkout_solution.checkout(sku_input) == (4 * 40)

  def test_checkout_single_item_multiple_deals(self):
    sku_input = "AAAAABC"
    assert checkout_solution.checkout(sku_input) == (200 + 30 + 20)

    sku_input = "AAAAABCAAA"
    assert checkout_solution.checkout(sku_input) == (200 + 30 + 20 + 130)

  def test_checkout_single_item_multiple_deals_multiple_times(self):
    sku_input = "AAAAAAAAAAAAAAABC"
    assert checkout_solution.checkout(sku_input) == (3 * 200 + 30 + 20)

    sku_input = "AAAAAAAAAAAAAAABCAAAAAAAAA"
    assert checkout_solution.checkout(sku_input) == (4 * 200 + 30 + 20 + 130 + 50)

  def test_checkout_conflict_multi_item_vs_single_item_deals(self):
    sku_input = "EEEEBB"
    assert checkout_solution.checkout(sku_input) == (40 * 4)

    sku_input = "BEBEEE"
    assert checkout_solution.checkout(sku_input) == (40 * 4)

    sku_input = "ABCDEABCDE"
    assert checkout_solution.checkout(sku_input) == (2 * 50 + 30 + 2 * 20 + 2 * 15 + 2 * 40)

  def test_multiple_multi_item_deals(self):
    sku_input = "EEEEBFF"
    assert checkout_solution.checkout(sku_input) == (40 * 4 + 2 * 10)

    sku_input = "EEEEBBFF"
    assert checkout_solution.checkout(sku_input) == (40 * 4 + 2 * 10)

    sku_input = "FFFF"
    assert checkout_solution.checkout(sku_input) == (3 * 10)

    sku_input = "FFFFFF"
    assert checkout_solution.checkout(sku_input) == (4 * 10)
