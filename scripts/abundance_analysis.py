import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------------------------------------
# Relative mapped-read distribution across screened pathogens
# ---------------------------------------------------------

INPUT = "results/pathogen_mapping_summary.csv"
OUTPUT_TABLE = "results/pathogen_mapped_read_distribution.csv"
OUTPUT_FIGURE = "results/figures/pathogen_mapped_read_distribution.png"

# Load mapping summary
df = pd.read_csv(INPUT)

# Keep pathogens with mapped reads
detected = df[df["Mapped_Reads"] > 0].copy()

# Calculate total mapped reads across the screened panel
total_mapped = detected["Mapped_Reads"].sum()

# Relative share of mapped reads
detected["Mapped_Read_Share_Percent"] = (
    detected["Mapped_Reads"] / total_mapped * 100
)

# Sort from highest to lowest
detected = detected.sort_values(
    "Mapped_Reads",
    ascending=False
).reset_index(drop=True)

# Save summary table
Path("results").mkdir(exist_ok=True)

detected[
    [
        "Pathogen",
        "Mapped_Reads",
        "Mapped_Read_Share_Percent",
        "Coverage_Percent",
        "Mean_Depth",
    ]
].to_csv(
    OUTPUT_TABLE,
    index=False
)

# ---------------------------------------------------------
# Plot
# ---------------------------------------------------------

Path("results/figures").mkdir(
    parents=True,
    exist_ok=True
)

fig, ax = plt.subplots(figsize=(9, 6))

bars = ax.barh(
    detected["Pathogen"],
    detected["Mapped_Read_Share_Percent"]
)

ax.set_xlabel("Share of mapped reads (%)")
ax.set_ylabel("Pathogen")
ax.set_title(
    "Relative Distribution of Reads Mapped to Screened Pathogens"
)

ax.invert_yaxis()

for bar, value in zip(
    bars,
    detected["Mapped_Read_Share_Percent"]
):
    ax.text(
        value + 0.3,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.2f}%",
        va="center",
        fontsize=9
    )

ax.set_xlim(
    0,
    max(detected["Mapped_Read_Share_Percent"]) * 1.15
)

ax.grid(
    axis="x",
    alpha=0.25
)

plt.tight_layout()

plt.savefig(
    OUTPUT_FIGURE,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ---------------------------------------------------------
# Console output
# ---------------------------------------------------------

print("Relative mapped-read distribution generated successfully.")
print(f"Total mapped reads across screened pathogens: {total_mapped}")
print(f"Saved: {OUTPUT_TABLE}")
print(f"Saved: {OUTPUT_FIGURE}")
print()
print(
    detected[
        [
            "Pathogen",
            "Mapped_Reads",
            "Mapped_Read_Share_Percent"
        ]
    ].to_string(index=False)
)
