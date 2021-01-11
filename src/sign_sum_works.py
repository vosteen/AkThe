from mpyc.runtime import mpc
import time
import random
import pickle
import os


@mpc.coroutine
async def mpc_sum(input_bits):
    n = len(input_bits)
    # prepare mpyc
    secint = mpc.SecInt()
    # distribute secret data
    input_list = [None] * n
    for i in range(n):
        # each process finds its own number and writes it in its own list
        if mpc.pid == i:
            input_list[i] = input_bits[i]
    # prepare special array with placeholders and secret data
    result_type = secint()
    sec_vec_l = [None] * n
    for i in range(n):
        sec_vec_l[i] = mpc.input(secint(input_list[i])
                                 if mpc.pid == i else result_type, senders=i)
    # calculate sum
    erg = mpc.sum(sec_vec_l)
    return erg


@mpc.coroutine
async def mpc_signumsum(input_bits):
    # check if sum is larger than the half amount of participants
    return mpc.sgn(mpc_sum(input_bits), l=2)


async def main(numberOfParticipants=2, rounds=1):
    # numberOfParticipants = 2
    # the distribution of the secret numbers is done in the sum function
    # input_bits = [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    input_bits = []
    for i in range(numberOfParticipants):
        rnd = random.getrandbits(1)
        input_bits.append(rnd)
    for n, i in enumerate(input_bits):
        if i == 0:
            input_bits[n] = -1

    start_time = time.time()
    await mpc.start()
    mpc_start_time = time.time() - start_time

    calc_time_l = []
    calc_start_time = time.time()

    for _ in range(rounds):
        erg = mpc_signumsum(input_bits)
        result = await mpc.output(erg)
    calc_time = time.time() - calc_start_time
    calc_time_l.append(calc_time)

    # print("result of Sign(Sum()): ", "positive" if result == 1 else "negative")

    await mpc.shutdown()

    return mpc_start_time, calc_time_l


if __name__ == '__main__':
    start_file = "start_time_1-10000_p10.p"
    calc_file = "calc_time_1-10000_p10.p"

    if os.path.isfile(start_file) and os.path.isfile(calc_file):
        start_time_d = pickle.load(open(start_file, "rb"))
        calc_time_d = pickle.load(open(calc_file, "rb"))
    else:
        start_time_d = {}
        calc_time_d = {}

    # number_of_participants = sys.argv[0]
    number_of_participants = 10

    # calc_rounds_list=list(range(1,10))
    calc_rounds_list = list(range(1, 100))
    calc_rounds_list = calc_rounds_list + list(range(100, 1000, 100))
    calc_rounds_list = calc_rounds_list + list(range(1000, 10000, 1000))

    # start_time_d[number_of_participants] = mpc_start_time_
    # calc_time_d[number_of_participants] = calc_time_
    for i in calc_rounds_list:
        print("start calc, rounds:", i)
        mpc_start_time_, calc_time_ = mpc.run(main(number_of_participants, rounds=i))
        start_time_d[i] = mpc_start_time_
        calc_time_d[i] = calc_time_
        pickle.dump(start_time_d, open(start_file, "wb+"))
        pickle.dump(calc_time_d, open(calc_file, "wb+"))
        print("end writing")

    # pickle.dump(start_time_d, open(start_file, "wb+"))
    # pickle.dump(calc_time_d, open(calc_file, "wb+"))
