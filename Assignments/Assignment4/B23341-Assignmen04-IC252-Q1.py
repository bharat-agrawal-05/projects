import matplotlib.pyplot as plt
import numpy as np

#part A

#sunny, rainy,cloudy
weather_prob = [1/3,1/3,1/3]
#t-shirt, jacket, sweater
clothing_given_sunny = [2/3,1/6,1/6]
clothing_given_rainy = [1/5,2/5,2/5]
clothing_given_cloudy = [1/5,2/5,2/5]
simulated = [[0,0,0],[0,0,0],[0,0,0]]
clothing = [clothing_given_sunny,clothing_given_rainy,clothing_given_cloudy]
for i in range(100000):
    a = np.random.randint(0,3)
    b = np.random.choice([0,1,2],p = clothing[a])
    simulated[a][b]+=1
for i in range(3):
    for j in range(3):
        simulated[i][j] = simulated[i][j]/100000
print("Simulated probabilities :")
print(simulated)


weather_probs = [sum(simulated[i][j] for j in range(3)) for i in range(3)]
clothing_probs = [sum(simulated[i][j] for i in range(3))  for j in range(3)]

# Plotting marginal probabilities
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.bar(['Sunny', 'Rainy', 'Cloudy'], weather_probs, color='skyblue')
plt.title('Marginal Probabilities of Weather')
plt.xlabel('Weather')
plt.ylabel('Probability')

plt.subplot(1, 2, 2)
plt.bar(['T-shirt', 'Jacket', 'Sweater'], clothing_probs, color='lightgreen')
plt.title('Marginal Probabilities of Clothing Choices')
plt.xlabel('Clothing Choice')
plt.ylabel('Probability')
plt.subplots_adjust(wspace=0.4)

plt.show()


conditional_probs = [[simulated[i][j] / weather_probs[i] for j in range(3)] for i in range(3)]

# Print conditional probabilities
print("Conditional Probabilities:")
for i, weather in enumerate(['Sunny', 'Rainy', 'Cloudy']):
    for j, clothing_choice in enumerate(['T-shirt', 'Jacket', 'Sweater']):
        print(f"P({clothing_choice} | {weather}) = {conditional_probs[i][j]}")
