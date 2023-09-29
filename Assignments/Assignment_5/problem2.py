def f(n):
    if n<2:
        return 1
    
    else:
        return 1.65*f(n-1)
    
def g(n):
    if n<2:
        return 1
    
    else:
        return 1.65*g(n-1)+1