from mpyc.runtime import mpc
import math


@mpc.coroutine
async def mpc_signumsum(input_bits):
    # compute sum and specify placeholder for result
    sec_sum = mpc.sum(input_bits)
    # compute maximum length of binary representation of sum (+1 as int() rounds down)
    bit_len = int(1 + math.log(len(input_bits), 2.0))
    # compute signum -- maximum length of binary representation is provided for better efficiency
    result = mpc.sgn(sec_sum, l=bit_len)
    return result


def prepare_list(input_bits):
    # define placeholder type as int
    sec_int = mpc.SecInt()
    # distribute secret data
    input_list = [None] * len(input_bits)
    for i in range(len(input_bits)):
        # each process finds its own data at the position of its id and writes it in its own secret version of the list
        if mpc.pid == i:
            input_list[i] = input_bits[i]
    # prepare special internal list with placeholders and secret data
    sec_vec_l = [None] * len(input_bits)
    for i in range(len(input_bits)):
        sec_vec_l[i] = mpc.input(sec_int(input_list[i]) if mpc.pid == i else sec_int(), senders=i)
    return sec_vec_l


@mpc.coroutine
async def mpc_minmax(placeholder_list):
    secint = mpc.SecInt()
    min_val, max_val = mpc.min_max(placeholder_list)
    return min_val, max_val


@mpc.coroutine
async def check_inputs(placeholder_list):
    min_val,max_val = mpc_minmax(placeholder_list)
    lower_bound = mpc.ge(min_val, -1)
    upper_bound = mpc.ge(1, max_val)

    return lower_bound, upper_bound


async def main():
    # specify the secret data
    input_bits = [0, 1, 1, -1, -1]
    # start mpc and connect parties
    await mpc.start()
    # distribute data to parties and prepare list of placeholders for it
    placeholder_list = prepare_list(input_bits)
    # check if input is valid
    lower_bound, upper_bound = check_inputs(placeholder_list)
    lower_bound = await mpc.output(lower_bound)
    upper_bound = await mpc.output(upper_bound)
    assert lower_bound and upper_bound, "invalid inputs"
    # compute the sign of the sum of the secret data
    erg = mpc_signumsum(placeholder_list)
    # fetch the result
    result = await mpc.output(erg)
    # close the mpc connections
    await mpc.shutdown()
    # print result
    print("result of Sign(Sum(", input_bits, ")): ", result)


if __name__ == '__main__':
    mpc.run(main())
