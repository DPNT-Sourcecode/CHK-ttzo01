from typing import Dict, List
from math import floor

from solutions.CHK.data_keys import (
  DEAL_COUNT_KEY,
  PRICE_REDUCTION_KEY,
  MULTI_ITEM_DEAL_KEY
)

# | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |

# total_count_for_combo deal
# for each unique sku
#  total_count += count_dict[sku]
#

MULTI_ITEM_COMBO_DEALS = {
  ["S","T","X","Y","Z"]: {
    1: {
      DEAL_COUNT_KEY: 3,
      TOTAL_PRICE_KEY: 45
    }
  },
}

def calculate_multi_item_deal_price_reduction(count_dict: Dict[str, int], unique_skus: list) -> int:
  total_price_reduction = 0

  total_count_for_combo = 0
  for unique_sku in unique_skus:
    if unique_sku in MULTI_ITEM_COMBO_DEALS:
      all_deal_data_for_item = MULTI_ITEM_COMBO_DEALS[unique_sku]

      # Should really check this exists before accessing from the dict. Also should really exist at this stage though
      total_for_single_item = count_dict[unique_sku]

      total_count_for_combo += total_for_single_item

  return total_price_reduction
