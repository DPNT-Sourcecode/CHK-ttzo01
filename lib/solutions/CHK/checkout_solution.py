from math import floor

from solutions.CHK.single_item_deals import calculate_single_item_deal_price_reduction
from solutions.CHK.price_list import PRICE_LIST
from solutions.CHK.multi_item_deals import calculate_multi_item_deal_price_reduction


INVALID_INPUT_RESPONSE = -1

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




