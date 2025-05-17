import builtins
import collections
import decimal
import fractions
import functools
import heapq
import itertools
import math
import sys
from collections import Counter, defaultdict
from collections import defaultdict as dd
from functools import partial
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest
from itertools import accumulate, chain, groupby, pairwise, repeat
from math import ceil, inf, isqrt, sqrt
from typing import Any

try:
    from rich import get_console
except ModuleNotFoundError:
    pass
else:
    print = get_console().out
    del get_console

input = sys.stdin.readline
# sys.setrecursionlimit((1 << 31) - 1)

all_ints = lambda: list(map(int, sys.stdin.read().split()))
all_words = lambda: sys.stdin.read().split()
ints = lambda: list(map(int, input().split()))
ints_rev = lambda: list(map(int, reversed(input().split())))
words = lambda: input().split()
words_rev = lambda: list(reversed(input().split()))

eprint = partial(builtins.print, file=sys.stderr)
fprint = partial(builtins.print, flush=True)


def solve() -> Any:
    pass


if __name__ == "__main__":
    for _ in range(int(input())):
        ret = solve()
        if ret is not None:
            print(ret)
