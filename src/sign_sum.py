from mpyc.runtime import mpc
from itertools import permutations


class SignSum:
    def __init__(self):
        pass

    def permutation(self, n, l):
        return [list(i) for i in list(permutations(range(n), l)) if sorted(i) == list(i)]

    def mpc_binary_and(self, position: list, values: list):
        bin_and = 1
        for i in position:
            bin_and = mpc.and_(bin_and, values[i])
        return bin_and

    def mpc_prod(selfself, position: list, values: list):
        bin_and = 1
        for i in position:
            bin_and = mpc.prod(bin_and, values[i])
        return bin_and

    def sign_sum(self, n):
        permutations = self.permutation(n, int(n / 2) + 1)
        for element in permutations:
            if self.mpc_binary_and(element) > 0:
                return 1
            else:
                return -1
