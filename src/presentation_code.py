from mpyc.runtime import mpc


@mpc.coroutine
async def signumsum(input_bits):
    # compute sum and specify placeholder for result
    sec_sum = mpc.sum(input_bits)

    result = mpc.sgn(sec_sum)
    return result

async def main():
    """
     mpyc benötigt eigene sichere Datenpypen
     die sicheren Datentypen werden als Platzhalter verwendet
     beim Start von mpc werden die Partein sich mit einem Platzhalter verbinden und ihre geheime Information eintragen
     """

    secint = mpc.SecInt()
    # damit können wir ints umwandeln in die sicheren Datentypen von mpyc
    input_bits = [secint(-1), secint(1), secint(1), secint(1)]

    # start mpc und Verbinden der Partein durch lokale TCP- Kommunikation
    await mpc.start()

    erg = signumsum(input_bits)
    # holen des Ergebnisses
    result = await mpc.output(erg)
    print("result:", result)

    # schließen der TCP-Verbindungen
    await mpc.shutdown()


if __name__ == "__main__":
    mpc.run(main())
