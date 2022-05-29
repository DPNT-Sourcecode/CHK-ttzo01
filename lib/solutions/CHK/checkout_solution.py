# +------+-------+---------------------------------+
# | Item | Price | Special offers                  |
# +------+-------+---------------------------------+
# | A    | 50    | 3A for 130, 5A for 200          |
# | B    | 30    | 2B for 45                       |
# | C    | 20    |                                 |
# | D    | 15    |                                 |
# | E    | 40    | 2E get one B free               |
# | F    | 10    | 2F get one F free               |
# | G    | 20    |                                 |
# | H    | 10    | 5H for 45, 10H for 80           |
# | I    | 35    |                                 |
# | J    | 60    |                                 |
# | K    | 70    | 2K for 120                      |
# | L    | 90    |                                 |
# | M    | 15    |                                 |
# | N    | 40    | 3N get one M free               |
# | O    | 10    |                                 |
# | P    | 50    | 5P for 200                      |
# | Q    | 30    | 3Q for 80                       |
# | R    | 50    | 3R get one Q free               |
# | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | U    | 40    | 3U get one U free               |
# | V    | 50    | 2V for 90, 3V for 130           |
# | W    | 20    |                                 |
# | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
# +------+-------+---------------------------------+
from solutions.CHK.single_item_deals import SINGLE_ITEM_DEALS

from typing import Dict, List
from math import floor

PRICE_LIST = {
  "A": 50,
  "B": 30,
  "C": 20,
  "D": 15,
  "E": 40,
  "F": 10,
  "G": 20,
  "H": 10,
  "I": 35,
  "J": 60,
  "K": 70,
  "L": 90,
  "M": 15,
  "N": 40,
  "O": 10,
  "P": 50,
  "Q": 30,
  "R": 50,
  "S": 20,
  "T": 20,
  "U": 40,
  "V": 50,
  "W": 20,
  "X": 17,
  "Y": 20,
  "Z": 21,
}

# | E    | 40    | 2E get one B free      |
# | N    | 40    | 3N get one M free      |
# | R    | 50    | 3R get one Q free      |

MULTI_ITEM_DEALS = {
  "E": {
      1: {
      DEAL_COUNT_KEY: 2,
      MULTI_ITEM_DEAL_KEY: "B",
      PRICE_REDUCTION_KEY: 30
    }
  },
  "N": {
      1: {
      DEAL_COUNT_KEY: 3,
      MULTI_ITEM_DEAL_KEY: "M",
      PRICE_REDUCTION_KEY: 15
    }
  },
  "R": {
      1: {
      DEAL_COUNT_KEY: 3,
      MULTI_ITEM_DEAL_KEY: "Q",
      PRICE_REDUCTION_KEY: 30
    }
  },
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

          if (number_of_times_deal_applied > 0):
            total_price_reduction += number_of_times_deal_applied * single_deal_for_item[PRICE_REDUCTION_KEY]
            total_for_single_item = total_for_single_item % number_of_times_deal_applied
            count_dict[deal_item] -= number_of_times_deal_applied


  return total_price_reduction

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

  # Calculate the multi item deals first and reduce the count_dict on the deal item if they've been applied
  # This doesn't really work if the multi_item deal price is less than the single item deal
  total_cost -= calculate_multi_item_deal_price_reduction(count_dict, unique_skus)
  total_cost -= calculate_single_item_deal_price_reduction(count_dict, unique_skus)

  return total_cost


