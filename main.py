
class Calculeaza_Perioada_Oscilatiilor:
    # def __init__(self, lmbd, T):
    #     self.lmbd = lmbd
    #     self.T = T
    def calculate(lmbd, T):
        lmbd = int(lmbd)
        c = 3 * 10**8
        T = lmbd/c
        if type(lmbd/c) == float:
            value = str(T).split('e')
            nr2 = value[1].split('0')
            final_result = f'v = {value[0]}^{nr2[0]}{nr2[1]}'
            return final_result

