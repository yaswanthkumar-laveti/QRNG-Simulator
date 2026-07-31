import matplotlib.pyplot as plt
from collections import Counter

def plot_bit_frequency(binary_sequence, save_path=None):
    """
    Bar chart showing the frequency of 0s and 1s.

    """

    count = Counter(binary_sequence)

    labels = ["0", "1"]
    values = [count.get("0", 0), count.get("1", 0)]

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(labels, values)

    ax.set_title("Frequency of Quantum Random Bits")
    ax.set_xlabel("Bit")
    ax.set_ylabel("Count")
    
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
    return fig


def plot_histogram(binary_sequence, save_path=None):
    """
    Histogram of generated bits.

    """

    data = [int(bit) for bit in binary_sequence]

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.hist(data, bins=2)

    ax.set_title("Histogram of Generated Bits")
    ax.set_xlabel("Bit Value")
    ax.set_ylabel("Frequency")
    ax.set_xticks([0, 1])

    ax.grid(axis="y", linestyle="--", alpha=0.5)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
    return fig


def plot_pie_chart(binary_sequence, save_path=None):
    """
    Pie chart of 0s and 1s.

    """

    count = Counter(binary_sequence)

    labels = ["0", "1"]
    values = [count.get("0", 0), count.get("1", 0)]

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Distribution of Random Bits")
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
    return fig


def plot_line_graph(binary_sequence, save_path=None):
    """
    Line graph of generated bit sequence.

    """

    data = [int(bit) for bit in binary_sequence]

    fig, ax = plt.subplots(figsize=(10, 3))

    ax.plot(data, marker="o")

    ax.set_title("Quantum Random Bit Sequence")
    ax.set_xlabel("Bit Position")
    ax.set_ylabel("Bit Value")
    ax.set_ylim(-0.2, 1.2)

    ax.grid(True)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
    return fig


def plot_scatter(binary_sequence, save_path=None):
    """
    Scatter plot of generated bits.

    """

    data = [int(bit) for bit in binary_sequence]

    fig, ax = plt.subplots(figsize=(10, 3))

    ax.scatter(range(len(data)), data)

    ax.set_title("Scatter Plot of Random Bits")
    ax.set_xlabel("Bit Position")
    ax.set_ylabel("Bit Value")
    ax.set_ylim(-0.2, 1.2)

    ax.grid(True)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
    return fig