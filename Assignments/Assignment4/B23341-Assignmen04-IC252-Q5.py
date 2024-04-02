from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

#PART-A : Random Variable Generation & Joint Distribution
print("PART-A\n")
x=np.random.uniform(0,1,300)
x=x.tolist()
y=np.random.uniform(1,2,300)
y=y.tolist()

x_count={i:x.count(i) for i in x}
y_count={j:y.count(j) for j in y}

X=[]
Y=[]
Z=[]
for i in x:
    for j in y:
        X.append(i)
        Y.append(j)
        Z.append(x_count[i]*y_count[j])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='b', marker='.')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('P(X,Y)')
ax.set_title('Joint probability distribution', fontsize=20, fontweight='bold', color='black', style='italic', family='monospace')
plt.show()

#PART-B : Independence of Random Variables
plt.cla()
plt.clf()

print()
print("PART-B\n")
plt.subplot(1,2,1)
plt.title("PDF of X", fontsize=20, fontweight='bold', color='black', style='italic', family='monospace')
plt.xlabel("X")
plt.ylabel("f(x)")
plt.plot(x,x_count.values())

plt.subplot(1,2,2)
plt.title("PDF of Y", fontsize=20, fontweight='bold', color='black', style='italic', family='monospace')
plt.xlabel("Y")
plt.ylabel("f(y)")
plt.plot(y,y_count.values())
plt.show()

print("As we see that the plots are all equal to 1 therefore f(x)f(y)=f(x,y) as 1*1=1. Therefore the events are independent\n")

#PART-C : Conditional Probability
print("PART-C")
print("As the events are independent we just calculate probability of X>0.5\n")
x1=np.random.uniform(0,1,10000)
success=0
for i in x1:
    if i>0.5:
        success+=1
print("The probability that X>0.5 =",success/10000,"\n")


#PART-D : Conditional PDF
print("PART-D")
plt.cla()
plt.clf()
print("Similarly the PDF of X dosen't change when Y takes any value therefore the PMF will be")
plt.title("Conditional PDF of X given Y=1.5", fontsize=20, fontweight='bold', color='black', style='italic', family='monospace')
plt.xlabel("X")
plt.ylabel("f(x|Y=1.5)")
plt.plot(x,x_count.values())
plt.show()