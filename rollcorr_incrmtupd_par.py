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
