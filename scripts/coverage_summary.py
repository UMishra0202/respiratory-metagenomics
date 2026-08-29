import pandas as pd
import matplotlib.pyplot as plt

# Load mapping summary
df = pd.read_csv("results/pathogen_mapping_summary.csv")

# Keep pathogens with mapped reads
detected = df[df["Mapped_Reads"] > 0].copy()

# Sort by coverage
detected = detected.sort_values("Coverage_Percent", ascending=True)

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    detected["Pathogen"],
    detected["Coverage_Percent"]
)

ax.set_xlabel("Genome coverage (%)")
ax.set_ylabel("Pathogen")
ax.set_title("Genome Coverage of Mapped Respiratory Pathogens")

for bar, value in zip(bars, detected["Coverage_Percent"]):
    ax.text(
        value + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.2f}%",
        va="center",
        fontsize=9
    )

ax.set_xlim(0, max(detected["Coverage_Percent"]) * 1.15)

ax.grid(
    axis="x",
    alpha=0.25
)

plt.tight_layout()

plt.savefig(
    "results/figures/pathogen_genome_coverage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Coverage summary figure generated successfully.")
