import numpy as np
from numba import njit

@njit(parallel=True)
def incremental_corr(data1, data2, window_size, rolling=True):
    n = data1.shape[0]
    cov = np.zeros(n - window_size + 1)
    corr = np.zeros(n - window_size + 1)
    mean1 = np.mean(data1[:window_size])
    mean2 = np.mean(data2[:window_size])
    var1 = np.sum((data1[:window_size] - mean1) ** 2)
    var2 = np.sum((data2[:window_size] - mean2) ** 2)
    cov[0] = np.sum((data1[:window_size] - mean1) * (data2[:window_size] - mean2))
    corr[0] = cov[0] / np.sqrt(var1 * var2)

    for i in range(1, n - window_size + 1):
        old_data1 = data1[i - 1]
        old_data2 = data2[i - 1]
        new_data1 = data1[i + window_size - 1]
        new_data2 = data2[i + window_size - 1]
        
        if rolling:
            mean1 = mean1 + (new_data1 - old_data1) / window_size
            mean2 = mean2 + (new_data2 - old_data2) / window_size
            var1 = var1 + (new_data1 - old_data1) * (new_data1 - mean1 + old_data1 - mean1) / window_size
            var2 = var2 + (new_data2 - old_data2) * (new_data2 - mean2 + old_data2 - mean2) / window_size
            cov[i] = cov[i - 1] + (new_data1 - old_data1) * (new_data2 - old_data2) - (data1[i - 1] - mean1) * (data2[i - 1] - mean2) + (data1[i + window_size - 1] - mean1) * (data2[i + window_size - 1] - mean2)
        else:
            mean1 = ((window_size - 1) * mean1 + new_data1) / window_size
            mean2 = ((window_size - 1) * mean2 + new_data2) / window_size
            var1 = var1 + (new_data1 - mean1) ** 2 - (old_data1 - mean1) ** 2
            var2 = var2 + (new_data2 - mean2) ** 2 - (old_data2 - mean2) ** 2
            cov[i] = cov[i - 1] + (new_data1 - mean1) * (new_data2 - mean2) - (old_data1 - mean1) * (old_data2 - mean2)
        
        corr[i] = cov[i] / np.sqrt(var1 * var2)

    return corr, cov




from numba import njit
import numpy as np

@njit
def rolling_corr(data1, data2, window_size, k=1):
    """
    Compute rolling correlation between two arrays using a sliding window.

    Parameters
    ----------
    data1 : ndarray
        First input data.
    data2 : ndarray
        Second input data.
    window_size : int
        Size of the sliding window.
    k : int, optional
        Number of steps to move the window at each iteration. Defaults to 1.

    Returns
    -------
    corr : ndarray
        Array of correlation coefficients, one for each window.

    Raises
    ------
    ValueError
        If data1 and data2 have different lengths.

    """
    if len(data1) != len(data2):
        raise ValueError("Input arrays must have the same length")

    n = len(data1)
    corr = np.empty(n - window_size + 1, dtype=np.float64)

    # Compute mean and variance of the first window
    window1 = data1[:window_size]
    window2 = data2[:window_size]
    mean1 = np.mean(window1)
    mean2 = np.mean(window2)
    var1 = np.var(window1, ddof=1)
    var2 = np.var(window2, ddof=1)
    cov = np.cov(window1, window2, ddof=1)[0, 1]

    # Compute correlation coefficient for first window
    corr[0] = cov / np.sqrt(var1 * var2)

    # Compute correlation coefficients for subsequent windows
    for i in range(1, n - window_size + 1):
        old1 = data1[i - 1]
        new1 = data1[i + window_size - 1]
        old2 = data2[i - 1]
        new2 = data2[i + window_size - 1]

        # Update mean and variance incrementally
        mean1 += (new1 - old1) * k / window_size
        mean2 += (new2 - old2) * k / window_size
        var1 += ((new1 - mean1) ** 2 - (old1 - mean1) ** 2) * k / window_size
        var2 += ((new2 - mean2) ** 2 - (old2 - mean2) ** 2) * k / window_size

        # Update covariance incrementally
        cov += ((new1 - old1) * (new2 - old2) * k / window_size -
                (k / (window_size - k)) * (mean1 - old1) * (mean2 - old2))

        # Compute correlation coefficient for current window
        corr[i] = cov / np.sqrt(var1 * var2)

    return corr
