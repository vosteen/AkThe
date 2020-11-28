from itertools import permutations

class SignSum:
    def __init__(self):
        pass

    def permutation(self, n, l):
        return [list(i) for i in list(permutations(range(5), 2)) if sorted(i) == list(i)]

    def mpc_binary_and(self, permuations: list) -> bool:
        pass

    def sum(self, n, permutations):
        pass
