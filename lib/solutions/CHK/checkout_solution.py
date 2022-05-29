
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

from typing import Dict, List
from math import floor

DEAL_COUNT_KEY = "count"
DEAL_PRICE_KEY = "price"

PRICE_LIST = {
  "A": 50,  
  "B": 30,  
  "C": 20,  
  "D": 15,  
}

DEALS = {
  "A": {
    DEAL_COUNT_KEY: 3,
    DEAL_PRICE_KEY: 130
  },
  "B": {
    DEAL_COUNT_KEY: 2,
    DEAL_PRICE_KEY: 45
  }
}

# I forgot to restart this one after pausing it, and then coming back so its taken about 3 minutes longer
def checkout(skus: List[str]) -> int:
  count_dict: Dict[str, int] = {}

  unique_skus = set(skus)

  if not all(sku in PRICE_LIST for sku in unique_skus):
    raise ValueError("Invalid input")

  for unique_sku in unique_skus:
    count_dict[unique_sku] = skus.count(unique_sku)

  total_cost = 0
  for unique_sku in unique_skus:
    if unique_sku in DEALS:

      deal_data = DEALS[unique_sku]

      deal_count = floor(count_dict[unique_sku] / deal_data[DEAL_COUNT_KEY])
      remainder_after_deal = count_dict[unique_sku] % deal_data[DEAL_COUNT_KEY]
      total_cost += deal_count * deal_data[DEAL_PRICE_KEY]

      total_cost += remainder_after_deal * PRICE_LIST[unique_sku]
    else:
      total_cost += count_dict[unique_sku] * PRICE_LIST[unique_sku]

  return total_cost



