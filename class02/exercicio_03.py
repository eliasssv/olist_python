def lista_de_listas(i):
    ret = []
    x = 1
    for j in range (i):
        l = []
        for k in range(i):
            l.append(x)
            x += 1

        ret.append(l)

    return ret

print(lista_de_listas(int(input("Nro de listas: "))))