from mpyc.runtime import mpc
from itertools import permutations
from random import randint


def permutation(n, l):
    return [list(i) for i in list(permutations(range(n), l)) if sorted(i) == list(i)]


async def mpc_prod(position, rand_int):
    await mpc.start()

    if mpc.pid == 0:
        vec0 = rand_int[0]
    if mpc.pid == 1:
        vec1 = rand_int[1]
    if mpc.pid == 2:
        vec2 = rand_int[2]
    if mpc.pid == 3:
        vec3 = rand_int[3]
    if mpc.pid == 4:
        vec4 = rand_int[4]
    if mpc.pid == 5:
        vec5 = rand_int[5]
    if mpc.pid == 6:
        vec6 = rand_int[6]
    if mpc.pid == 7:
        vec7 = rand_int[7]
    if mpc.pid == 8:
        vec8 = rand_int[8]
    if mpc.pid == 9:
        vec9 = rand_int[9]
    secint = mpc.SecInt(128)
    result_type = secint()

    sec_vec0 = mpc.input(secint(vec0) if mpc.pid == 0 else result_type, senders=0)
    sec_vec1 = mpc.input(secint(vec1) if mpc.pid == 1 else result_type, senders=1)
    sec_vec2 = mpc.input(secint(vec2) if mpc.pid == 2 else result_type, senders=2)
    # sec_vec0 = mpc.input([secint(v) for v in vec0] if mpc.pid == 0 else result_type, senders=0)
    # sec_vec1 = mpc.input([secint(v) for v in vec1] if mpc.pid == 1 else result_type, senders=1)
    # sec_vec2 = mpc.input([secint(v) for v in vec2] if mpc.pid == 2 else result_type, senders=2)
    #    sec_vec3 = mpc.input([secint(v) for v in vec3] if mpc.pid == 3 else result_type, senders=3)
    #    sec_vec4 = mpc.input([secint(v) for v in vec4] if mpc.pid == 4 else result_type, senders=4)
    #    sec_vec5 = mpc.input([secint(v) for v in vec5] if mpc.pid == 5 else result_type, senders=5)
    #    sec_vec6 = mpc.input([secint(v) for v in vec6] if mpc.pid == 6 else result_type, senders=6)
    #    sec_vec7 = mpc.input([secint(v) for v in vec7] if mpc.pid == 7 else result_type, senders=7)
    #    sec_vec8 = mpc.input([secint(v) for v in vec8] if mpc.pid == 8 else result_type, senders=8)
    #    sec_vec9 = mpc.input([secint(v) for v in vec9] if mpc.pid == 9 else result_type, senders=9)

    sec_vec_list = [sec_vec0, sec_vec1, sec_vec2]  # ,sec_vec3,sec_vec4,sec_vec5,sec_vec6,sec_vec7, sec_vec8, sec_vec9]

    t = []
    for element in position:
        t.append(sec_vec_list[element])

    for i in range(len(position) - 1):
        pass

    #  erg = mpc.in_prod(*t)
    erg = mpc.prod(t, start=1)

    result = await mpc.output(erg)

    await mpc.shutdown()

    return result


async def main():
    n = 3  # number of participants
    rand_int = [randint(0, 1)] * n
    permutations = permutation(n, int(n / 2) + 1)
    erg = -1
    for element in permutations:
        temp = await mpc_prod(element, rand_int)
        if temp > 0:
            erg = 1
            break

    print(erg)


if __name__ == '__main__':
    mpc.run(main())
