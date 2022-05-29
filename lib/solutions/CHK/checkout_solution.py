# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+


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

SINGLE_ITEM_DEALS = {
  "A": [{
    DEAL_COUNT_KEY: 3,
    DEAL_PRICE_KEY: 130
  }, {
    DEAL_COUNT_KEY: 5,
    DEAL_PRICE_KEY: 200
  }],
  "B": [{
    DEAL_COUNT_KEY: 2,
    DEAL_PRICE_KEY: 45
  }]
}

INVALID_INPUT_RESPONSE = -1

# I forgot to restart this one after pausing it, and then coming back so its taken about 3 minutes longer
def checkout(skus: str) -> int:

  if not isinstance(skus, str):
    return INVALID_INPUT_RESPONSE

  unique_skus = set(skus)

  print(unique_skus)

  if not all(sku in PRICE_LIST for sku in unique_skus):
    return INVALID_INPUT_RESPONSE

  count_dict: Dict[str, int] = {sku: skus.count(sku) for sku in unique_skus}

  total_cost = 0
  for unique_sku in unique_skus:
    if unique_sku in DEALS:

      deal_data = DEALS[unique_sku]
      print(len(deal_data))

      deal_count = floor(count_dict[unique_sku] / deal_data[DEAL_COUNT_KEY])
      remainder_after_deal = count_dict[unique_sku] % deal_data[DEAL_COUNT_KEY]
      total_cost += deal_count * deal_data[DEAL_PRICE_KEY]

      total_cost += remainder_after_deal * PRICE_LIST[unique_sku]
    else:
      total_cost += count_dict[unique_sku] * PRICE_LIST[unique_sku]

  return total_cost


