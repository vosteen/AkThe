from mpyc.runtime import mpc
from itertools import permutations
from random import randint


def permutation(n, l):
    return [list(i) for i in list(permutations(range(n), l)) if sorted(i) == list(i)]


async def mpc_prod(position, rand_int, n):
    await mpc.start()

    vec_l = [None] * n
    for i in range(n):
        if mpc.pid == i:
            vec_l[i] = rand_int[i]
    secint = mpc.SecInt(128)
    result_type = secint()

    sec_vec_l = [None] * n
    for i in range(n):
        sec_vec_l[i] = mpc.input(secint(vec_l[0]) if mpc.pid == 0 else result_type, senders=0)

    t = []
    for element in position:
        t.append(sec_vec_l[element])

    for i in range(len(position) - 1):
        pass

    #  erg = mpc.in_prod(*t)
    erg = mpc.prod(t, start=1)

    result = await mpc.output(erg)

    await mpc.shutdown()

    return result


async def main():
    n = 9  # number of participants
    rand_int = [randint(0, 1)] * n
    permutations = permutation(n, int(n / 2) + 1)
    erg = -1
    for element in permutations:
        temp = await mpc_prod(element, rand_int, n)
        if temp > 0:
            erg = 1
            break

    print(erg)


if __name__ == '__main__':
    mpc.run(main())
