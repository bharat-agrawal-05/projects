# import sys 
import numpy as np
import matplotlib.pyplot as plt

ball1,ball2,ball3,ball4=0,0,0,0
trials=[]
relball1,relball2,relball3,relball4=[],[],[],[]
for i in range(50000):
    guess=np.random.randint(1,5)
    if guess==1:
        ball1+=1
    elif guess==2:
        ball2+=1
    elif guess==3:
        ball3+=1
    elif guess==4:
        ball4+=1
    relball1.append(ball1/(i+1))
    relball2.append(ball2/(i+1))
    relball3.append(ball3/(i+1))
    relball4.append(ball4/(i+1))

    trials.append(i+1)
    if i+1 == 50 or i+1 ==5000 or i+1 == 50000:
        plt.plot(trials,relball1,label='Ball 1')
        plt.plot(trials,relball2,label='Ball 2')
        plt.plot(trials,relball3,label='Ball 3')
        plt.plot(trials,relball4,label='Ball 4')
        plt.xlabel('Number of trials')
        plt.ylabel('Relative frequency of balls')
        plt.title('Relative frequency of balls vs number of trials')
        plt.legend()
        plt.savefig(f'problem3a{i+1}.png')
        plt.close()
