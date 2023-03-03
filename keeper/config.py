from string import ascii_letters

ALPHAS_QUERY = list(ascii_letters)
NUMS_QUERY = [str(i) for i in range(10)]
SYMS_QUERY = ["@", "#", "?", "*"]

INIT_QUERY = ALPHAS_QUERY + NUMS_QUERY + SYMS_QUERY
