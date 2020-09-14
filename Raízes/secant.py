def secant(a,b,f,epsilon):
    i=0
    while(1):
        x=( b * f(a)-(a)*f(b))/(f(a)-f(b))
        if epsilon > abs(f(x)): # criterio  de parad
            break
        a=b
        b=x
        i+=1
    return x,i