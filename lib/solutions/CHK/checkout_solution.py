
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

# noinspection PyUnusedLocal
# skus = unicode string
def compute(skus: List[str]) -> int:
  count_dict: Dict[str, int] = {}

  for sku in skus:
    if sku not in count_dict:
      count_dict[sku] = 0
    else:
      count_dict[sku] += 1
    
  unique_skus = set(skus)

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