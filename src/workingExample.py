from mpyc.runtime import mpc
from itertools import permutations
from random import randint



@mpc.coroutine
async def sum():
    secint = mpc.SecInt()
    x = [secint(1), secint(1), secint(0), secint(1), secint(1), secint(0)]
    t = mpc.sum(x)
    return t

@mpc.coroutine
async def ge():
    secint = mpc.SecInt()
    t = mpc.ge(sum(), 6)
    return t

async def main():
    await mpc.start()
    erg = ge()
    result = await mpc.output(erg)
    print("result:", result)
    await mpc.shutdown()


if __name__ == '__main__':
    mpc.run(main())
