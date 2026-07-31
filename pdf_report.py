from reportlab.lib.styles import getSampleStyleSheet
import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Image
)
from visualization import (
    plot_bit_frequency,
    plot_histogram,
    plot_pie_chart,
    plot_line_graph,
    plot_scatter
)

def generate_pdf_report(bits, stats, filename="qrng_report.pdf"):

    # -----------------------------
    # Save graph images
    # -----------------------------

    plot_bit_frequency(bits, "bit_frequency.png")
    plot_histogram(bits, "histogram.png")
    plot_pie_chart(bits, "pie_chart.png")
    plot_scatter(bits, "scatter_plot.png")
    plot_line_graph(bits, "line_plot.png")

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    # -----------------------------
    # Title
    # -----------------------------

    elements.append(
        Paragraph(
            "<b>Quantum Random Number Generator Simulator</b>",
            styles["Title"]
        )
    )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Binary Sequence
    # -----------------------------

    elements.append(
        Paragraph(
            "<b>Generated Binary Sequence</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(bits, styles["BodyText"])
    )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Statistics
    # -----------------------------

    elements.append(
        Paragraph(
            "<b>Statistical Analysis</b>",
            styles["Heading2"]
        )
    )

    for key, value in stats.items():
        elements.append(
            Paragraph(
                f"<b>{key}</b>: {value}",
                styles["BodyText"]
            )
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Graphs
    # -----------------------------

    graphs = [

        ("Bit Frequency Chart", "bit_frequency.png"),
        ("Histogram", "histogram.png"),
        ("Pie Chart", "pie_chart.png"),
        ("Scatter Plot", "scatter_plot.png"),
        ("Line Plot", "line_plot.png")

    ]

    for title, image in graphs:

        elements.append(
            Paragraph(
                f"<b>{title}</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Image(
                image,
                width=400,
                height=250
            )
        )

        elements.append(
            Paragraph("<br/>", styles["Normal"])
        )

    # -----------------------------
    # Build PDF
    # -----------------------------

    doc.build(elements)

    # -----------------------------
    # Delete temporary images
    # -----------------------------

    for _, image in graphs:
        if os.path.exists(image):
            os.remove(image)
    return filename