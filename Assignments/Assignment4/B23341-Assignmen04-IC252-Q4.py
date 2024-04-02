import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm

mean_am = 1
std_am = 0.5
mean_fm = 1.5
std_fm = 0.75

#SIMULATION OF REPAIR TIMES
am_repair_times = []
fm_repair_times = []
repair_time_total = []
for _ in range(100):
    repair_time_am = random.gauss(mean_am, std_am)
    repair_time_fm = random.gauss(mean_fm, std_fm)
    repair_time = repair_time_am + repair_time_fm
    am_repair_times.append(round(repair_time_am, 2))
    fm_repair_times.append(round(repair_time_fm, 2))
    repair_time_total.append(round(repair_time, 2))

print(am_repair_times)

print(f"AM Radio Repair Times (hours): {am_repair_times}")
print(f"FM Radio Repair Times (hours): {fm_repair_times}")


#PART-A : JOINT DISTRIBUTION

#2D histogram
print("PART-A\n")
plt.subplot(1, 2, 1)
plt.hist2d(am_repair_times, fm_repair_times, bins=10, cmap='coolwarm')
plt.colorbar()
plt.xlabel("AM Radio Repair Time (hours)")
plt.ylabel("FM Radio Repair Time (hours)")
plt.title("Joint Probability Distribution (2D Histogram)")
plt.grid(True)
#Scatter Plot
plt.subplot(1, 2, 2)
plt.scatter(am_repair_times, fm_repair_times)
plt.xlabel("AM Radio Repair Time (hours)")
plt.ylabel("FM Radio Repair Time (hours)")
plt.title("Scatter Plot")
plt.subplots_adjust(wspace=0.4)
plt.grid(True)
plt.show()


#PART-B : CONDITIONAL PROBABILITY
'''
As the repair times of AM and FM radios are independent, 
the probability of FM repair time less than 1 hour given that AM repair 
time is 2 hours is the same as the probability of FM repair time less than 1 hour.
'''
print("PART-B\n")

print("\nProbability of FM repair time less than 1 hour given that AM repair time is 2 hours:")
p_fm_less_than_1 = norm.cdf(1, mean_fm, std_fm)
print(f'{p_fm_less_than_1:.4f}')

#PART-C : Random Variable representating total time
print("PART-C\n")
print(f'Mean of the total repair time is: {np.mean(repair_time_total)}')
print(f'Standard Deviation for the total repair time is: {np.std(repair_time_total)}')

sns.histplot(repair_time_total, kde=True, color='skyblue')
plt.title("Histogram of Total Repair Times")
plt.xlabel("Total Repair Time (hours)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()