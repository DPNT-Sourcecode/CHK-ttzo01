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
MULTI_ITEM_DEAL_KEY = "deal_item"

PRICE_LIST = {
  "A": 50,
  "B": 30,
  "C": 20,
  "D": 15,
  "E": 40,
}


# Sorted list of deals per item, Descending based on deal count.
SINGLE_ITEM_DEALS = {
  "A": {
    1: {
      DEAL_COUNT_KEY: 5,
      PRICE_REDUCTION_KEY: 50
    },
    2: {
      DEAL_COUNT_KEY: 3,
      PRICE_REDUCTION_KEY: 20
    },
  },
  "B": {
    1: {
      DEAL_COUNT_KEY: 2,
      PRICE_REDUCTION_KEY: 15
    }
  }
}

MULTI_ITEM_DEALS = {
  "E": {
      1: {
      DEAL_COUNT_KEY: 2,
      MULTI_ITEM_DEAL_KEY: "B",
      PRICE_REDUCTION_KEY: 30
    }
  }
}

INVALID_INPUT_RESPONSE = -1

def calculate_single_item_deal_price_reduction(count_dict: Dict[str, int], unique_skus: list) -> int:
  total_price_reduction = 0
  for unique_sku in unique_skus:
    if unique_sku in SINGLE_ITEM_DEALS:
      all_deal_data_for_item = SINGLE_ITEM_DEALS[unique_sku]

      # Should really check this exists before accessing from the dict. Also should really exist at this stage though
      total_for_single_item = count_dict[unique_sku]

      # Use the total for a single item, Reduce the count when the largest deal count deal has been applied
      for single_deal_for_item in all_deal_data_for_item.values():
        number_of_times_deal_applied = floor(total_for_single_item / single_deal_for_item[DEAL_COUNT_KEY])

        if (number_of_times_deal_applied > 0):
          total_price_reduction += number_of_times_deal_applied * single_deal_for_item[PRICE_REDUCTION_KEY]
          total_for_single_item = total_for_single_item % single_deal_for_item[DEAL_COUNT_KEY]

  return total_price_reduction


def calculate_multi_item_deal_price_reduction(count_dict: Dict[str, int], unique_skus: list) -> int:
  total_price_reduction = 0
  for unique_sku in unique_skus:
    if unique_sku in MULTI_ITEM_DEALS:
      all_deal_data_for_item = MULTI_ITEM_DEALS[unique_sku]

      # Should really check this exists before accessing from the dict. Also should really exist at this stage though
      total_for_single_item = count_dict[unique_sku]

      for single_deal_for_item in all_deal_data_for_item.values():
        deal_item = single_deal_for_item[MULTI_ITEM_DEAL_KEY]
        if deal_item in count_dict:
          deal_item_count = count_dict[deal_item]
          number_of_times_deal_applied = min(
            floor(total_for_single_item / single_deal_for_item[DEAL_COUNT_KEY]),
            floor(deal_item_count)
          )

          print("number_of_times_deal_applied", number_of_times_deal_applied)

          if (number_of_times_deal_applied > 0):
            total_price_reduction += number_of_times_deal_applied * single_deal_for_item[PRICE_REDUCTION_KEY]
            total_for_single_item = total_for_single_item % number_of_times_deal_applied
            count_dict[deal_item] -= number_of_times_deal_applied


  print("total_price_reduction", total_price_reduction)
      
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
    total_cost += count_dict[unique_sku] * PRICE_LIST[unique_sku]

  # calculate reduction in price from total

  # I've just noticed the deals conflict with each other
  # Calculate the multi item deals first and reduce the count_dict on the deal item if they've been applied
  total_cost -= calculate_multi_item_deal_price_reduction(count_dict, unique_skus)
  total_cost -= calculate_single_item_deal_price_reduction(count_dict, unique_skus)

  return total_cost
