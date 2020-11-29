from mpyc.runtime import mpc
from itertools import permutations
from random import randint


def permutation(n, l):
    return [list(i) for i in list(permutations(range(n), l)) if sorted(i) == list(i)]


async def mpc_prod(position, rand_int, n):
    # connect all threads
    await mpc.start()

    # prepare list of elements
    vec_l = [None] * n
    for i in range(n):
        # in each thread: fill corresponding position in list of elements
        if mpc.pid == i:
            vec_l[i] = rand_int[i]

    # define data types
    secint = mpc.SecInt(128)
    result_type = secint()

    # prepare list of protected values (invisible for everybody except owner
    sec_vec_l = [None] * n

    # fill protected list
    for i in range(n):
        sec_vec_l[i] = mpc.input(secint(vec_l[i]) if mpc.pid == i else result_type, senders=i)

    # choose elements to connect
    t = []
    for element in position:
        t.append(sec_vec_l[element])

    # smpc-calculation of product
    erg = mpc.prod(t, start=1)

    # get the result
    result = await mpc.output(erg)

    # disconnect again
    await mpc.shutdown()

    return result


async def main():
    n = 4  # number of participants
    rand_int = [randint(-10, 10) for _ in range(n)]
    # fange den Fall, dass der zu schützende Wert 0 ist ab, in dem ein zufälliger Boolzustand gewählt wird

    print("the following private data is to be protected:" + str(rand_int))

    for i in range(len(rand_int)):
        if rand_int[i] > 0:
            rand_int[i] = 1
        elif rand_int[i] < 0:
            rand_int[i] = 0
        elif rand_int[i] == 0:
            rand_int[i] = randint(0, 1)

    # Würfelrauschen
    for i in range(len(rand_int)):
        if randint(1, 10) < 2:
            pass
            # rand_int[i] = randint(0, 1)

    rand_int = [1, 1, 0, 0]
    print("the following private data is protected:" + str(rand_int))

    permutations = permutation(n, int(n / 2) + 1)
    erg = -1

    for element in permutations:
        print("permutation: ", element)
        prod_res = await mpc_prod(element, rand_int, n)
        print("das kommt heraus: ", prod_res)
        if prod_res > 0:
            erg = 1
            break
    print(erg)


if __name__ == '__main__':
    mpc.run(main())
