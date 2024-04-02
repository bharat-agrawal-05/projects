import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for Professor A
u_A = 78
sigma_A = 5

# Parameters for Professor B
u_B = 85
sigma_B = 3

# Probabilities for difficulty levels
easy = 0.3
medium = 0.5
hard = 0.2

# Part (a): Joint Probability Distribution
# Calculate joint probability distribution P(X, Y)
# Here, X represents exam score and Y represents difficulty level
# Assuming X follows normal distribution for both professors

# Score range
x_values = np.linspace(60, 100, 400)

# Calculate PDF for Professor A
pdf_A = norm.pdf(x_values, u_A, sigma_A)
print(pdf_A)

# Calculate PDF for Professor B
pdf_B = norm.pdf(x_values, u_B, sigma_B)

# Multiply PDFs by probability of difficulty levels
joint_prob_A_easy = pdf_A * easy
joint_prob_A_medium = pdf_A * medium
joint_prob_A_hard = pdf_A * hard

joint_prob_B_easy = pdf_B * easy
joint_prob_B_medium = pdf_B * medium
joint_prob_B_hard = pdf_B * hard

# Plot joint probabilities for each difficulty level
plt.figure(figsize=(10, 5))

# Plot for Professor A
plt.subplot(121)
plt.plot(x_values, joint_prob_A_easy, label='Easy')
plt.plot(x_values, joint_prob_A_medium, label='Medium')
plt.plot(x_values, joint_prob_A_hard, label='Hard')
plt.title('Professor A')
plt.xlabel('Score')
plt.ylabel('Joint Probability')
plt.legend()

# Plot for Professor B
plt.subplot(122)
plt.plot(x_values, joint_prob_B_easy, label='Easy')
plt.plot(x_values, joint_prob_B_medium, label='Medium')
plt.plot(x_values, joint_prob_B_hard, label='Hard')
plt.title('Professor B')
plt.xlabel('Score')
plt.ylabel('Joint Probability')
plt.legend()



plt.tight_layout()
plt.show()



# Calculate marginal probabilities for each score for Professor A
marginal_A_scores = joint_prob_A_easy + joint_prob_A_medium + joint_prob_A_hard

# Calculate marginal probabilities for each score for Professor B
marginal_B_scores = joint_prob_B_easy + joint_prob_B_medium + joint_prob_B_hard

# Plot marginal probabilities for each score
plt.figure(figsize=(10, 5))

# Plot for Professor A
plt.subplot(121)
plt.plot(x_values, marginal_A_scores, label='Scores')
plt.title('Professor A')
plt.xlabel('Score')
plt.ylabel('Marginal Probability')
plt.legend()

# Plot for Professor B
plt.subplot(122)
plt.plot(x_values, marginal_B_scores, label='Scores')
plt.title('Professor B')
plt.xlabel('Score')
plt.ylabel('Marginal Probability')
plt.legend()

plt.tight_layout()
plt.show()
# Part (b): Marginal Probability Distributions
# Calculate marginal probabilities by summing over one variable (difficulty level)
# this is the same as pdf B
# Calculate marginal probabilities for each difficulty level for Professor A
marginal_A_easy = np.sum(joint_prob_A_easy)
marginal_A_medium = np.sum(joint_prob_A_medium)
marginal_A_hard = np.sum(joint_prob_A_hard)

# Calculate marginal probabilities for each difficulty level for Professor B
marginal_B_easy = np.sum(joint_prob_B_easy)
marginal_B_medium = np.sum(joint_prob_B_medium)
marginal_B_hard = np.sum(joint_prob_B_hard)

# Plot marginal probabilities for each difficulty level
difficulty_levels = ['Easy', 'Medium', 'Hard']
marginal_A = [marginal_A_easy, marginal_A_medium, marginal_A_hard]
marginal_B = [marginal_B_easy, marginal_B_medium, marginal_B_hard]

plt.bar(difficulty_levels, marginal_A, alpha=0.5, label='Professor A',color = 'blue')

plt.ylabel('Marginal Probability')
plt.legend()
plt.show()

plt.bar(difficulty_levels, marginal_B, alpha=0.5, label='Professor B',color = 'yellow')

plt.ylabel('Marginal Probability')
plt.legend()
plt.show()

# Part (c): Conditional Probability
# Calculate conditional probability P(X > 80|Y = "Easy")
# Since X follows normal distribution, we can use the cumulative distribution function (CDF)
# P(X > 80|Y = "Easy") = 1 - P(X <= 80|Y = "Easy") = 1 - P(x<=80) since independent
print()
print("part c:")
conditional_prob_A_easy = 1 - norm.cdf(80, u_A, sigma_A)
print("Conditional probability of A given easy =", conditional_prob_A_easy) 
conditional_prob_B_easy = 1 - norm.cdf(80, u_B, sigma_B)
print("Conditional probability of B given easy =", conditional_prob_B_easy) 


# Part (d): Plotting PDFs

# Plot PDFs for Professor A
plt.figure(figsize=(10, 6))
plt.plot(x_values, pdf_A, label='Professor A', linestyle='--')
plt.fill_between(x_values, 0, pdf_A, alpha=0.3)

# Plot PDFs for Professor B
plt.plot(x_values, pdf_B, label='Professor B', linestyle='-.')
plt.fill_between(x_values, 0, pdf_B, alpha=0.3)

plt.title('Probability Density Functions (PDFs) of Exams')
plt.xlabel('Score')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()

# Part (e): Changes in Joint Probability Distribution
# If difficulty level assignment depends on the professor or student's expected score,
# probabilities for each combination of X and Y would change accordingly.
# This would require adjusting the joint probability distribution based on the new probabilities.