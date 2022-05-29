
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

from typing import Dict, List

PRICE_LIST = {
  "A": 50,  
  "B": 30,  
  "C": 20,  
  "D": 15,  
}

DEALS = {
  "A": {
    "count": 3,
    "price": 130
  },
  "B": {
    "count": 2,
    "price": 45
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