import numpy as np
import matplotlib.pyplot as plt

#part-a
def f(n):
    if n<2:
        return 1
    
    else:
        return 1.65*f(n-1)
    
def g(n):
    if n<2:
        return 1
    
    else:
        return g(n-1)+g(n-2)
    
def h(n):
    if n<2:
        return 2
    else:
        return 2*h(n-2)
    
def k(n):
    if n<3:
        return 3
    
    else:
        return k(n-1)+k(n-3)

#part-b    
xvalues=np.arange(0,10)
yvalues1=[f(i) for i in xvalues]
plt.scatter(xvalues,yvalues1,color='red',label='Function F')
plt.xlabel('Values of x--->',fontsize=20)
plt.ylabel('Values of Function F(x)--->',fontsize=20)
plt.title('Graph for Function F: ')
plt.show()

xvalues=np.arange(0,10)
yvalues2=[g(i) for i in xvalues]
plt.scatter(xvalues,yvalues2,color='green',label='Function G')
plt.xlabel('Values of x--->',fontsize=20)
plt.ylabel('Values of Function G(x)--->',fontsize=20)
plt.title('Graph for Function G: ')
plt.show()

xvalues=np.arange(0,10)
yvalues3=[h(i) for i in xvalues]
plt.scatter(xvalues,yvalues3,color='blue',label='Function H')
plt.xlabel('Values of x--->',fontsize=20)
plt.ylabel('Values of Function H(x)--->',fontsize=20)
plt.title('Graph for Function H: ')
plt.show()

xvalues=np.arange(0,10)
yvalues4=[k(i) for i in xvalues]
plt.scatter(xvalues,yvalues4,color='black',label='Function K')
plt.xlabel('Values of x--->',fontsize=20)
plt.ylabel('Values of Function K(x)--->',fontsize=20)
plt.title('Graph for Function K: ')
plt.show()

#part-c
xvalues=np.arange(0,20)
yvalues1=[f(i) for i in xvalues]
yvalues2=[g(i) for i in xvalues]
yvalues3=[h(i) for i in xvalues]
yvalues4=[k(i) for i in xvalues]

plt.scatter(xvalues,yvalues1,label='Function F',color='red')
plt.scatter(xvalues,yvalues2,label='Function G',color='green')
plt.scatter(xvalues,yvalues3,label='Function H',color='blue')
plt.scatter(xvalues,yvalues4,label='Function K',color='black')
plt.legend()
plt.xlabel('Values of x--->',fontsize=20)
plt.ylabel('Values of functions--->',fontsize=20)
plt.title('Graph for all the functions: ',fontsize=20)
plt.show()
