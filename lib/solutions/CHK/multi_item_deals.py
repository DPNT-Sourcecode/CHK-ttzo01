from solutions.CHK.data_keys import (
  DEAL_COUNT_KEY,
  PRICE_REDUCTION_KEY,
  MULTI_ITEM_DEAL_KEY
)

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
