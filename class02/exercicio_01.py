def remover_duplicado(L=[]):
    RET = []
    for a in L:
        exists = False
        for b in RET:
            if (b == a):
                exists = True
        
        if (exists == False):
            RET.append(a)
    return RET


R = remover_duplicado([12,1,1,2,3,3,2,1,1,1,2,1,3])            
print(R)

def remover_duplicado_prof(L):
    RET = []
    for a in L:
        if a not in RET:
            RET.append(a)
    return RET