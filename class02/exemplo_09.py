def func_variadic(*args, param="oi"):
    print('param:',param)
    for arg in args:
        print(arg)

func_variadic("teste1", "teste2", "teste3","reerere")