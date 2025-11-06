import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for each item
params = {
    "Temperature": {"mean": 25.1, "sigma": 1.5, "randomness": 0.5},
    "Pressure": {"mean": 100.2, "sigma": 2, "randomness": 2},
    "Corrected_Flow_Rate": {"mean": 500.2, "sigma": 1, "randomness": 0.3},
    "Diameter": {"mean": 9.0, "sigma": 1, "randomness": 0.2}
}

# Number of samples
num_samples = 1000

# Generate data
data = {}
for item, param in params.items():
    mean = param["mean"]
    sigma = param["sigma"]
    randomness = param["randomness"]
    
    # Generate normal distribution
    samples = np.random.normal(mean, sigma, num_samples)
    
    # Add randomness
    noise = np.random.normal(0, randomness * sigma, num_samples)
    samples_with_randomness = samples + noise
    
    # Store the data
    data[item] = samples_with_randomness

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("generated_data.csv", index=False)

# Plot the histogram
for item in data:
    plt.hist(data[item], bins=30, alpha=0.6, label=item)

plt.title("Histograms of Generated Data with Randomness")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()