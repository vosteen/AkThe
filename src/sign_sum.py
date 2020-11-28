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

    def sign_sum(self, n):
        permutations = self.permutation(n, int(n / 2) + 1)
        for element in permutations:
            if self.mpc_binary_and(element) > 0:
                return 1
            else:
                return -1
