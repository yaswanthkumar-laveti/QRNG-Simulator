from collections import Counter
from scipy.stats import chisquare
from statsmodels.sandbox.stats.runs import runstest_1samp
import math

def analyze_bits(binary_sequence):

    total_bits = len(binary_sequence)
    count = Counter(binary_sequence)
    zeros = count.get("0", 0)
    ones = count.get("1", 0)
    zero_percentage = (zeros / total_bits) * 100
    one_percentage = (ones / total_bits) * 100

    # Convert binary string to numeric list
    bit_values = [int(bit) for bit in binary_sequence]

    # Mean
    mean = sum(bit_values) / total_bits

    # Variance
    variance = sum((x - mean) ** 2 for x in bit_values) / total_bits

    # Standard Deviation
    std_dev = math.sqrt(variance)

    # Entropy
    entropy = 0
    for probability in [zeros / total_bits, ones / total_bits]:
        if probability > 0:
            entropy -= probability * math.log2(probability)

    # Chi-Square Test
    observed = [zeros, ones]
    expected = [total_bits / 2, total_bits / 2]
    chi2_stat, p_value = chisquare(observed, expected)
    if p_value > 0.05:
        chi_result = "PASS ✅ (Sequence appears random)"
    else:
        chi_result = "FAIL ❌ (Sequence may not be random)"

    # Runs Test
    z_stat, runs_p_value = runstest_1samp(bit_values)
    if runs_p_value > 0.05:
        runs_result = "PASS ✅ (Sequence order appears random)"
    else:
        runs_result = "FAIL ❌ (Sequence order may not be random)"

    return {
        "Total Bits": total_bits,
        "Zeros": zeros,
        "Ones": ones,
        "Zero Percentage": round(zero_percentage, 2),
        "One Percentage": round(one_percentage, 2),
        "Mean": round(mean, 4),
        "Variance": round(variance, 4),
        "Standard Deviation": round(std_dev, 4),
        "Entropy": round(entropy, 4),
        "Chi-Square Statistic": round(chi2_stat, 4),
        "P-Value": round(p_value, 4),
        "Chi-Square Result": chi_result,
        "Runs Test Z-Statistic": round(z_stat, 4),
        "Runs Test P-Value": round(runs_p_value, 4),
        "Runs Test Result": runs_result
    }