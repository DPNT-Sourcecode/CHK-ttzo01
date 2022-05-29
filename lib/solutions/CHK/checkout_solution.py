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
PRICE_REDUCTION_KEY = "price_reduction"

PRICE_LIST = {
  "A": 50,
  "B": 30,
  "C": 20,
  "D": 15,
  "E": 40,
}

SINGLE_ITEM_DEALS = {
  "A": {
    1: {
      DEAL_COUNT_KEY: 3,
      PRICE_REDUCTION_KEY: 20
    },
    2:{
      DEAL_COUNT_KEY: 5,
      PRICE_REDUCTION_KEY: 50
    }
  },
  "B": {
    1: {
      DEAL_COUNT_KEY: 2,
      PRICE_REDUCTION_KEY: 45
    }
  }
}

MULTI_ITEM_DEALS = {
  "E": {
    DEAL_COUNT_KEY: 2,
    "deal_item": "B",
    PRICE_REDUCTION_KEY: 30
  }
}

INVALID_INPUT_RESPONSE = -1

def calculate_single_item_deal_price_reduction(count_dict: Dict[str, int], unique_skus: list) -> int:
  total_price_reduction = 0
  for unique_sku in unique_skus:
    if unique_sku in SINGLE_ITEM_DEALS:
      all_deal_data = SINGLE_ITEM_DEALS[unique_sku]

      # Need a list of the deal counts starting from largest first
      descending_deal_required_amount_list = sorted([single_deal_data[DEAL_COUNT_KEY] for single_deal_data in all_deal_data.values()], reverse=True)

      # Should really check this exists before accessing from the dict. Also should really exist at this stage though
      total_for_single_item = count_dict[unique_sku]

      deal_applied_dict = {}

      for required_deal_amount in descending_deal_required_amount_list:
        number_of_times_deal_applied = floor(total_for_single_item / required_deal_amount)

        deal_applied_dict[required_deal_amount] = number_of_times_deal_applied

        total_for_single_item = total_for_single_item % required_deal_amount
      
      print(deal_applied_dict)

      for deal in deal_applied_dict


  return total_price_reduction

# I forgot to restart this one after pausing it, and then coming back so its taken about 3 minutes longer
def checkout(skus: str) -> int:

  if not isinstance(skus, str):
    return INVALID_INPUT_RESPONSE

  unique_skus = set(skus)

  if not all(sku in PRICE_LIST for sku in unique_skus):
    return INVALID_INPUT_RESPONSE

  count_dict: Dict[str, int] = {sku: skus.count(sku) for sku in unique_skus}

  total_cost = 0

  for unique_sku in unique_skus:
    total_cost += PRICE_LIST[unique_sku]

  # calculate reduction in price from total

  total_cost -= calculate_single_item_deal_price_reduction(count_dict, unique_skus)

  # total_cost -= calculate_single_item_deal_price_reduction(count_dict, unique_skus)

  # for unique_sku in unique_skus:
  #   if unique_sku in SINGLE_ITEM_DEALS:

  #     single_item_deal_data = SINGLE_ITEM_DEALS[unique_sku]

  #     deal_count = floor(count_dict[unique_sku] / single_item_deal_data[DEAL_COUNT_KEY])
  #     remainder_after_deal = count_dict[unique_sku] % single_item_deal_data[DEAL_COUNT_KEY]

  #     total_cost += deal_count * single_item_deal_data[PRICE_REDUCTION_KEY]
  #     total_cost += remainder_after_deal * PRICE_LIST[unique_sku]
  #   else:
  #     total_cost += count_dict[unique_sku] * PRICE_LIST[unique_sku]

  # return total_cost

  return total_cost








