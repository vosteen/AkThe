from mpyc.runtime import mpc
from itertools import permutations


def permutation(n, l):
    return [list(i) for i in list(permutations(range(n), l)) if sorted(i) == list(i)]


async def mpc_prod(position: list):
    await mpc.start()

    if mpc.pid == 0:
        vec0 = [1]
    if mpc.pid == 1:
        vec1 = [0]
    if mpc.pid == 2:
        vec2 = [1]

    secint = mpc.SecInt(42)
    result_type = [secint()]

    sec_vec0 = mpc.input([secint(v) for v in vec0] if mpc.pid == 0 else result_type, senders=0)
    sec_vec1 = mpc.input([secint(v) for v in vec1] if mpc.pid == 1 else result_type, senders=1)
    sec_vec2 = mpc.input([secint(v) for v in vec2] if mpc.pid == 2 else result_type, senders=2)

    if position[0] == 0:
        if position[1] == 1:
            t = [sec_vec0, sec_vec1]
        else:
            t = [sec_vec0, sec_vec2]
    else:
        t = [sec_vec1, sec_vec2]

    erg = mpc.in_prod(*t)

    result = await mpc.output(erg)
    print(result)

    await mpc.shutdown()

    return result


async def main():
    n = 3  # number of participants

    permutations = permutation(n, int(n / 2) + 1)
    erg = -1
    for element in permutations:
        temp = await mpc_prod(element)
        if temp > 0:
            erg = 1
            # break

    print(erg)


if __name__ == '__main__':
    mpc.run(main())
