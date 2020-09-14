def false_pos(a,b,f,epsilon):
    i=0
    while(1): 
        x=(a*f(b)-b*f(a)) /(f(b)-f(a)) 

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        if  ((abs(b-a)) < epsilon) or (abs(f(x)) < epsilon): 
            break
        i+=1   
    return x,i