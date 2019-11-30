def func(param, oi="oi", **keywords):
    print("param:", param)
    print(keywords)
    print(oi)
    for kw in keywords:
        print(kw,":",keywords[kw])

func("teste",
        keyword_a="Value A",
        keyword_b="Value B",
        oi="teste ooi",
        keyword_c="Value C")