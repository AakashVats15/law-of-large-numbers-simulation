import numpy as np

def generate_running_mean(n_samples=10000, distribution="normal"):
    """
    Generate running sample means for different distributions.

    Parameters
    ----------
    n_samples : int
        Number of samples to generate.
    distribution : str
        One of: "normal", "uniform", "bernoulli".

    Returns
    -------
    samples : np.ndarray
        Raw generated samples.
    running_mean : np.ndarray
        Running average of samples.
    """

    if distribution == "normal":
        samples = np.random.randn(n_samples)

    elif distribution == "uniform":
        samples = np.random.uniform(-1, 1, n_samples)

    elif distribution == "bernoulli":
        samples = np.random.binomial(1, 0.5, n_samples)

    else:
        raise ValueError(f"Unknown distribution: {distribution}")

    running_mean = np.cumsum(samples) / np.arange(1, n_samples + 1)

    return samples, running_mean