from typing import Dict, List
from math import floor

from solutions.CHK.data_keys import (
  DEAL_COUNT_KEY,
  PRICE_REDUCTION_KEY,
  MULTI_ITEM_DEAL_KEY
)
from solutions.CHK.price_list import PRICE_LIST


# | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |

# total_count_for_combo deal
# for each unique sku
#  total_count += count_dict[sku]
#

MULTI_ITEM_COMBO_DEALS = [
  {
    DEAL_COMBO_LIST_KEY: ["S","T","X","Y","Z"],
    DEAL_COUNT_KEY: 3,
    TOTAL_PRICE_KEY: 45
  },
]

def calculate_multi_item_combo_deal_price_reduction(count_dict: Dict[str, int], unique_skus: list) -> int:
  total_price_reduction = 0

  # need to get the list of items in price order and count the most expensive ones first

  for deal in DEAL_COMBO_LIST_KEY:

    prices_for_deal = {}
    total_count_for_combo = 0
    cost_without_deal = 0

    for sku_in_combo_deal in deal[DEAL_COMBO_LIST_KEY]:

      prices_for_deal[sku_in_combo_deal] = PRICE_LIST[sku_in_combo_deal]

      if sku_in_combo_deal in count_dict:
        total_count_for_combo += count_dict[sku_in_combo_deal]
        cost_without_deal += count_dict[sku_in_combo_deal] * PRICE_LIST[sku_in_combo_deal]
  
    number_of_times_deal_applied = total_count_for_combo/deal[DEAL_COUNT_KEY]:

    print(number_of_times_deal_applied)

    sorted_ascending_prices_for_deal = dict(sorted(prices_for_deal.items(), key=lambda item: item[1]))

    for sku_and_price in sorted_ascending_prices_for_deal:


  return total_price_reduction