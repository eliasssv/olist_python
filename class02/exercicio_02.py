def inverse(word):
    ret = ''
    for a in word:
        ret = a + ret
    return ret

R = inverse('ABCD')            
print(R)