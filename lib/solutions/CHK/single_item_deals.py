from typing import Dict
from math import floor

from solutions.CHK.data_keys import (
  DEAL_COUNT_KEY,
  PRICE_REDUCTION_KEY,
)

# | A    | 50    | 3A for 130, 5A for 200          |
# | B    | 30    | 2B for 45                       |
# | F    | 10    | 2F get one F free               |
# | H    | 10    | 5H for 45, 10H for 80           |
# | K    | 70    | 2K for 120                      |
# | P    | 50    | 5P for 200                      |
# | Q    | 30    | 3Q for 80                       |
# | U    | 40    | 3U get one U free               |
# | V    | 50    | 2V for 90, 3V for 130           |

# Sorted dict of deals per item, Descending based on deal count. Doesn't need to be a dict could of just been a list
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
  },
  "F": {
      1: {
      DEAL_COUNT_KEY: 3,
      PRICE_REDUCTION_KEY: 10
    }
  },
  "H": {
    2: {
      DEAL_COUNT_KEY: 10,
      PRICE_REDUCTION_KEY: 20
    },
    1: {
      DEAL_COUNT_KEY: 5,
      PRICE_REDUCTION_KEY: 5
    }
  },
  "K": {
    1: {
      DEAL_COUNT_KEY: 2,
      PRICE_REDUCTION_KEY: 20
    },
  },
  "P": {
    1: {
      DEAL_COUNT_KEY: 5,
      PRICE_REDUCTION_KEY: 50
    },
  },
  "Q": {
    1: {
      DEAL_COUNT_KEY: 3,
      PRICE_REDUCTION_KEY: 10
    },
  },
  "U": {
    1: {
      DEAL_COUNT_KEY: 4,
      PRICE_REDUCTION_KEY: 40
    },
  },
  "V": {
    2: {
      DEAL_COUNT_KEY: 3,
      PRICE_REDUCTION_KEY: 20
    },
    1: {
      DEAL_COUNT_KEY: 2,
      PRICE_REDUCTION_KEY: 10
    }
  }
}

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
