import numpy as np
import matplotlib.pyplot as plt

ball1,ball2,ball3,ball4=0,0,0,0
trials=[]
relball1,relball2,relball3,relball4,mean=[],[],[],[],[]

for i in range(50000):
    meanNum=0
    for j in range(5):
        guess=np.random.randint(0,4)
        meanNum+=guess
    mean.append(meanNum/4)
    ball1,ball2,ball3,ball4=0,0,0,0

plt.hist(mean)
plt.xlabel('Mean')
plt.ylabel('Frequency')
plt.title('Mean of 5 guesses')
plt.show()
plt.savefig('problem3b_5_50000.png')

for i in range(50000):
    meanNum=0
    for j in range(50):
        guess=np.random.randint(0,4)
        meanNum+=guess
    mean.append(meanNum/50)
    ball1,ball2,ball3,ball4=0,0,0,0

plt.hist(mean)
plt.xlabel('Mean')
plt.ylabel('Frequency')
plt.title('Mean of 50 guesses')
plt.show()
plt.savefig('problem3b_50_50000.png')
