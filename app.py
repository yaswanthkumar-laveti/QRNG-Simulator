import os

# MUST be set before importing qiskit, numpy, or scipy to avoid C-threading segfaults
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import streamlit as st
import pandas as pd

from qrng import generate_random_bits
from statistics import analyze_bits
from pdf_report import generate_pdf_report
from visualization import (
    plot_bit_frequency,
    plot_histogram,
    plot_pie_chart,
    plot_line_graph,
    plot_scatter
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Quantum Random Number Generator Simulator",
    page_icon="⚛️",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("⚛️ Quantum Random Number Generator Simulator")

st.markdown("""
Generate **true quantum random numbers** using the **Qiskit Aer Simulator**.

This application can:

- Generate quantum random binary sequences
- Perform statistical analysis
- Display graphical visualizations
- Export the results as CSV, TXT, and PDF reports
""")

st.markdown("---")

# --------------------------------------------------
# Bit Selection
# --------------------------------------------------

st.subheader("🎯 Select Number of Random Bits")

num_bits = st.selectbox(
    "Choose the number of bits:",
    [10, 50, 100, 500, 1000],
    index=2
)

st.markdown("---")

# --------------------------------------------------
# Generate Button
# --------------------------------------------------

st.subheader("⚡ Generate Random Numbers")

if st.button("Generate Random Numbers"):

    # Generate Random Bits
    bits = generate_random_bits(num_bits)

    st.success("Random numbers generated successfully!")

    # --------------------------------------------------
    # Generated Sequence
    # --------------------------------------------------

    st.subheader("🔢 Generated Binary Sequence")

    st.code(bits)

    # --------------------------------------------------
    # Statistical Analysis
    # --------------------------------------------------

    stats = analyze_bits(bits)

    st.markdown("---")
    st.subheader("📊 Statistical Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Bits", stats["Total Bits"])
        st.metric("Zeros", stats["Zeros"])
        st.metric("Ones", stats["Ones"])
        st.metric("Zero %", f"{stats['Zero Percentage']}%")
        st.metric("One %", f"{stats['One Percentage']}%")

    with col2:
        st.metric("Mean", round(stats["Mean"], 4))
        st.metric("Variance", round(stats["Variance"], 4))
        st.metric("Std Deviation", round(stats["Standard Deviation"], 4))
        st.metric("Entropy", round(stats["Entropy"], 4))

    with col3:
        st.metric("Chi-Square", round(stats["Chi-Square Statistic"], 4))
        st.metric("P-Value", round(stats["P-Value"], 4))
        st.metric("Runs Test Z", round(stats["Runs Test Z-Statistic"], 4))
        st.metric("Runs Test P", round(stats["Runs Test P-Value"], 4))

    st.success(f"Chi-Square Result: {stats['Chi-Square Result']}")
    st.success(f"Runs Test Result: {stats['Runs Test Result']}")

    # --------------------------------------------------
    # Visualizations
    # --------------------------------------------------

    st.markdown("---")
    st.subheader("📈 Visualizations")

    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(plot_bit_frequency(bits))
        st.pyplot(plot_pie_chart(bits))

    with col2:
        st.pyplot(plot_histogram(bits))
        st.pyplot(plot_scatter(bits))

    st.pyplot(plot_line_graph(bits))

    # --------------------------------------------------
    # Download Section
    # --------------------------------------------------

    st.markdown("---")
    st.subheader("📥 Download Results")

    # CSV

    df = pd.DataFrame({
        "Index": range(1, len(bits) + 1),
        "Bit": list(bits)
    })

    csv = df.to_csv(index=False).encode("utf-8")

    # TXT

    txt_data = bits

    # PDF

    pdf_file = generate_pdf_report(bits, stats)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            label="⬇️ Download CSV",
            data=csv,
            file_name="qrng_random_sequence.csv",
            mime="text/csv"
        )

    with col2:
        st.download_button(
            label="📄 Download TXT",
            data=txt_data,
            file_name="qrng_random_sequence.txt",
            mime="text/plain"
        )

    with col3:
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📑 Download PDF",
                data=file,
                file_name="qrng_report.pdf",
                mime="application/pdf"
            )

# --------------------------------------------------
# About Project
# --------------------------------------------------

st.markdown("---")

st.subheader("ℹ️ About Project")

st.info("""
### Quantum Random Number Generator (QRNG) Simulator

This application demonstrates quantum randomness using the **Qiskit Aer Simulator**.

### Features

- Quantum random bit generation
- Statistical analysis
- Frequency analysis
- Entropy calculation
- Chi-Square Test
- Runs Test
- Interactive visualizations
- CSV export
- TXT export
- PDF report generation

### Technologies Used

- Python
- Qiskit
- Streamlit
- Matplotlib
- SciPy
- ReportLab
""")