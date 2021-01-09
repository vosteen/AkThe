 @mpc_coro
    async def sgn(self, a, l=None, LT=False, EQ=False):
        """Secure sign(um) of a, return -1 if a < 0 else 0 if a == 0 else 1.
        If integer flag l=L is set, it is assumed that -2^(L-1) <= a < 2^(L-1)
        to save work (compared to the default l=type(a).bit_length).
        If Boolean flag LT is set, perform a secure less than zero test instead, and
        return 1 if a < 0 else 0, saving the work for a secure equality test.
        If Boolean flag EQ is set, perform a secure equal to zero test instead, and
        return 1 if a == 0 else 0, saving the work for a secure comparison.
        """
        assert not (LT and EQ)
        stype = type(a)
        await returnType((stype, True))
        Zp = stype.field

        l = l or stype.bit_length
        # l ist die Anzahl der Bits des Wertes a
        r_bits = await self.random_bits(Zp, l)
        # r_bits enthält nun sicher berechete l Zufallswerte
        r_modl = 0
        for r_i in reversed(r_bits):
            # reverset dreht die Liste um (warum ist das sinnvoll?)
            r_modl <<= 1 # shift um eins -> 0 wird im ersten Lauf zu 00 
            r_modl += r_i.value 
        a = await self.gather(a)
        a_rmodl = a + ((1<<l) + r_modl)
        # Hier wird a + Zufallsbinärwerte berechnet
        k = self.options.sec_param # Standardwert ist 30
        r_divl = self._random(Zp, 1<<k).value # Warum ist hier random als protected aufgerufen?
        c = await self.output(a_rmodl + (r_divl << l)) # c ist somit 30 Zufallszahlen || a (l bit lang) mit addierten Zufallszahlen 
        c = c.value % (1<<l) # jetzt nicht mehr; jetzt ist es nur noch a (l (l = klein L) bit lang) mit addierten Zufallszahlen
        s_sign = (await self.random_bits(Zp, 1, signed=True))[0].value # zufällig entweder -1 oder 1 ?

        e = [None] * (l+1) # leere Liste
        sumXors = 0
        for i in range(l-1, -1, -1): # die Schleife zählt von der Zahl l aus bis 0 herunter (bspw. für l= 5: 5,4,3,2,1,0 ) 
            c_i = (c >> i) & 1 # in der ersten Runde wird nur das erste Bit mit 1 verundet; danach die ersten beiden Bits,... -> es wird nur das i-te bit in c_i gespeichert
            r_i = r_bits[i].value # hier wird das i-te Zufallsbit vom Anfang in r_i gespeichert
            e[i] = Zp(s_sign + r_i - c_i + 3*sumXors) # Zp() ist bspe int(); s_sign ist konstant entweder -1 oder 1; 
            sumXors += 1 - r_i if c_i else r_i # hier wird das Zufallsbit vom Anfang zu dem Wert sumXor addiert 
        e[l] = Zp(s_sign - 1 + 3*sumXors)  # Zp() ist bspe int(); s_sign ist konstant entweder -1 oder 1; 
        g = await self.is_zero_public(stype(self.prod(e))) # es wird überprüft, ob die die Werte aus e miteinander multipliziert 0 ergeben 
        h = 3 - s_sign if g else 3 + s_sign # h wird auf + oder - 11(bin) gesetzt
        z = (c - a_rmodl + (h << l-1)) / (1<<l)

        h = self.all(r_bits[i] if (c >> i) & 1 else 1-r_bits[i] for i in range(l))
        h = await h
        z = (h - 1) * (2*z - 1)
        z = await self._reshare(z)

        z <<= stype.frac_length
        return z
