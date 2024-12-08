import numpy as np
import matplotlib.pyplot as plt

def generate_trajectory(mu, sigma, S0, tf, dt):
	# Variables
	S = S0
	t = 0

	# Logging
	S_t = [S]
	t_t = [t]

	# Simulation Loop
	while t<tf:
		S = S + mu*S*dt + sigma*S*np.random.normal(0,1)*np.sqrt(dt)
		t += dt
		
		# Log
		S_t.append(S)
		t_t.append(t)

	return S_t, t_t

if __name__ == "__main__":
	# Stock Parameters
	mu = 0.1 # Expected annual return ($/yr)
	sigma = 0.2 # Price volatility ($)
	S0 = 40 # Initial stock price ($)
	
	# Simulation Parameters
	dt = 1/365
	tf = 1

	S_t, t_t = generate_trajectory(mu, sigma, S0, tf, dt)

	# Plot
	plt.plot(t_t,S_t)
	plt.title("Sample Trajectory | $S_0=$" + f"{S0}" + r", $\mu=$" + f"{mu}" + r", $\sigma=$" + f"{sigma}")
	plt.xlabel("Time (yr)")
	plt.ylabel("Price ($)")
	plt.show()