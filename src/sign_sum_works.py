from mpyc.runtime import mpc


@mpc.coroutine
async def mpc_sum(n, input_bits):
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
        sec_vec_l[i] = mpc.input(secint(input_list[i]) if mpc.pid == i else result_type, senders=i)
    # calculate sum
    erg = mpc.sum(sec_vec_l)
    return erg


@mpc.coroutine
async def mpc_signumsum(n, input_bits):
    # check if sum is larger than the half amount of participants
    return mpc.lt(int(n / 2), mpc_sum(n, input_bits))


async def main():
    numberOfParticipants = 11
    # the distribution of the secret numers is done in the sum function
    input_bits = [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1]

    await mpc.start()
    erg = mpc_signumsum(numberOfParticipants, input_bits)
    result = await mpc.output(erg)
    print("result of Sign(Sum()): ", "positive" if result == 1 else "negative")
    await mpc.shutdown()


if __name__ == '__main__':
    mpc.run(main())
