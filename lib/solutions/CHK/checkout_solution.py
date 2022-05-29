
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

from typing import Dict, List

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
def checkout(skus: List[str]) -> int:
  count_dict: Dict[str, int] = {}
  for sku in skus:

    if sku not in count:
      count[sku] = 0
    else:
      count[sku] += 1
    
  unique_skus = set(skus)

  total_cost = 0
  for unique_sku in unique_skus:
    if unique_sku in DEALS:
      if count_dict[unique_sku] >= DEALS[unique_sku]:
        total_cost = count_dict[unique_sku] % DEALS[unique_sku]