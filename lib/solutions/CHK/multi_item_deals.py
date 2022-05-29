from typing import Dict, List
from math import floor

from solutions.CHK.data_keys import (
  DEAL_COUNT_KEY,
  PRICE_REDUCTION_KEY,
  MULTI_ITEM_DEAL_KEY
)

# | E    | 40    | 2E get one B free               |
# | N    | 40    | 3N get one M free               |
# | R    | 50    | 3R get one Q free               |

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