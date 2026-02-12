import matplotlib.pyplot as plt
from source.simulations.simulate_lln import generate_running_mean

def plot_running_mean(n_samples=10000, distribution="normal"):
    """
    Plot the running mean for a chosen distribution.
    """

    _, running_mean = generate_running_mean(n_samples, distribution)

    plt.figure(figsize=(10, 5))
    plt.plot(running_mean, label="Running Mean")
    plt.axhline(0, color="red", linestyle="--", label="True Mean (0)")
    plt.xlabel("n")
    plt.ylabel("Mean")
    plt.title(f"LLN: Convergence of Sample Mean ({distribution.capitalize()})")
    plt.legend()
    plt.grid(True)
    plt.show()