for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'igual a', x, '*', n // x)
            break
    else:
        print(n, 'é número primo')

        # se o for nao tiver break executa o else