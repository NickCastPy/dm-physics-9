
class Calculeaza_Perioada_Oscilatiilor:
    
    def calculate(lmbd, T, v):
        lmbd_int = int(lmbd)
        c = 3 * 10**8
        if T == 'x':
            T = lmbd_int/c
            value = str(T).split('e')
            nr2 = value[1].split('0')
            final_result = f'T = {value[0]}^{nr2[0]}{nr2[1]} s'
        elif v == 'x':
            v =  c/lmbd_int
            final_result = f'v = {v} Hz'
        elif lmbd == 'x':
            lmbd_int = c*T
            final_result = f'lambda = {lmbd_int} m'
        return final_result

