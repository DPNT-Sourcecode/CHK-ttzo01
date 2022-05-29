
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
      PRICE_REDUCTION_KEY: 10
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
