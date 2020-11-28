from mpyc.runtime import mpc

from itertools import permutations


class SignSum:
    def __init__(self):
        pass

    def permutation(self, n, l):
        return [list(i) for i in list(permutations(range(5), 2)) if sorted(i) == list(i)]

    def mpc_binary_and(self, perm: list) -> bool:
        bin_and = 1
        for i in perm:
            bin_and = mpc.and_(bin_and, i)
        return bin_and

    def sum(self, n, permutations):
        pass
