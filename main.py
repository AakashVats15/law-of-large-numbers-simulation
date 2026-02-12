
from source.simulations.simulate_lln import generate_running_mean
from source.plots.plots_lln import plot_running_mean

def main():
    """
    Run the LLN simulation and plot the results.
    """

    # Choose parameters
    n_samples = 10000
    distribution = "normal"

    # Run simulation
    samples, running_mean = generate_running_mean(n_samples, distribution)

    # Plot results
    plot_running_mean(n_samples=n_samples, distribution=distribution)

if __name__ == "__main__":
    main()
