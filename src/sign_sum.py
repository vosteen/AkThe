from mpyc.runtime import mpc
from mpyc.seclists import seclist
from itertools import permutations


def permutation(n, l):
    return [list(i) for i in list(permutations(range(n), l)) if sorted(i) == list(i)]


async def mpc_prod(values, position, n):
    await mpc.start()

    print(mpc.pid)

    vec = [None]*n
    for i in range(n):
        if mpc.pid == i:
            vec[i] = values[i]

    secint = mpc.SecInt(42)
    result_type = [secint()]
    sec_vec = seclist([None]*n, secint)


    for i in range(n):
        if mpc.pid == i:
            sec_vec[i] = mpc.input([secint(v) for v in [vec[i]]] if mpc.pid == i else result_type, senders=0)


    t = []
    for element in position:
        print(sec_vec[element])
        t.append(sec_vec[element])

    erg = mpc.in_prod(*t)

    result = await mpc.output(erg)
    print(result)
    await mpc.shutdown()
    return result


async def main():
    n = 3  # number of participants
    values = [1, 0, 1]
    permutations = permutation(n, int(n / 2) + 1)
    erg = -1
    for element in permutations:
        temp = await mpc_prod(values, element, n)
        if temp > 0:
            erg = 1
            # break

    print(erg)


if __name__ == '__main__':
    mpc.run(main())
