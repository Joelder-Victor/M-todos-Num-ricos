def newton(x,f_s,f,symbol,epsilon):
    fi=derivate(f_s,symbol)
    i=0
    while (1):
        fx=f(x)
        aux=fi(x)
        if epsilon > abs(fx) or abs(aux-x)<epsilon:
            break
        x=aux
        i+=1
    return x,i