from trajectories import generate_trajectory
import matplotlib.pyplot as plt
import numpy as np

# Options parameters
M = 10000 # Number of trajectories to simulate
K = 50 # Strike price ($)

# Stock Parameters
mu = 0.07 # Expected annual return ($/yr)
sigma = 0.2 # Price volatility ($)
S0 = 55 # Initial stock price ($)

# Simulation Parameters
N = 200 # Number of simulation steps
T = 6/12 # Time at which to estimate expected value of an option (yr)
dt = T/N # Time step (Yr)

# Calculate expected future value of the call option
S_T = np.array([generate_trajectory(mu, sigma, S0, T, dt)[0][-1] for _ in range(M)])

# Payoff
f = np.maximum(S_T - K, 0)

V_T = np.sum(f)/M

# Calculate present value of call option

C = (1+mu*dt)**(-1*N) * V_T

print(f"Expected value of option after {T*12} months: {V_T}$")
print(f"Present value of option: {C}$")

plt.figure(1)
plt.hist(S_T, bins=int(len(S_T)/100))
plt.xlabel("S(T)")
plt.ylabel("Frequency")
plt.title(r"S(T) Histogram | " + f"M={M}")

# Calculate mean and standard deviation
mean = np.mean(S_T)
std = np.std(S_T)

# Add vertical lines for mean and standard deviation
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(mean + std, color='black', linestyle='dashed', linewidth=2, label='Mean + 1 Stdev')
plt.axvline(mean - std, color='black', linestyle='dashed', linewidth=2, label='Mean - 1 Stdev')
plt.legend()

plt.figure(2)
plt.hist(f, bins=int(len(f)/100))
plt.xlabel(r"$f(S)$")
plt.ylabel("Frequency")
plt.title(f"Payoff Histogram | M={M}")

# Calculate mean and standard deviation
mean = np.mean(f)
std = np.std(f)

# Add vertical lines for mean and standard deviation
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(mean + std, color='black', linestyle='dashed', linewidth=2, label='Mean + 1 Stdev')
plt.axvline(mean - std, color='black', linestyle='dashed', linewidth=2, label='Mean - 1 Stdev')
plt.legend()


plt.show()