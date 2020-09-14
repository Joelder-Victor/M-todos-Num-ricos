def bissec(a,b,f,epsilon):
    i=0
    while(1):
        x= (a+b) / 2 

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        
        if  ((abs(b-a)) < epsilon) or (abs(f(x)) < epsilon):
                break
        i=i+1
    return x,i