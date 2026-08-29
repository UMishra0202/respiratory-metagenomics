from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Input / output paths
# ------------------------------------------------------------

INPUT = "results/pathogen_evidence_summary.csv"
OUTPUT_TABLE = "results/pathogen_evidence_ranked.csv"
OUTPUT_FIGURE = "results/figures/pathogen_evidence_overview.png"


# ------------------------------------------------------------
# Load integrated evidence table
# ------------------------------------------------------------

df = pd.read_csv(INPUT)


# ------------------------------------------------------------
# Prepare plotting data
# ------------------------------------------------------------

df["Mapped_Reads"] = pd.to_numeric(
    df["Mapped_Reads"],
    errors="coerce"
)

df["Coverage_Percent"] = pd.to_numeric(
    df["Coverage_Percent"],
    errors="coerce"
)

df["Mean_Depth"] = pd.to_numeric(
    df["Mean_Depth"],
    errors="coerce"
)


# Keep pathogens with mapped reads
df = df[df["Mapped_Reads"] > 0].copy()


# Sort by mapped reads
df = df.sort_values(
    "Mapped_Reads",
    ascending=False
).reset_index(drop=True)


# Save ranked evidence table
Path("results").mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_TABLE,
    index=False
)


# ------------------------------------------------------------
# Plot
# ------------------------------------------------------------

Path("results/figures").mkdir(
    parents=True,
    exist_ok=True
)

fig, ax = plt.subplots(
    figsize=(9, 6)
)


ax.scatter(
    df["Mapped_Reads"],
    df["Coverage_Percent"],
    s=80
)

  # ------------------------------------------------------------
# Add pathogen labels with manual positions
# ------------------------------------------------------------

label_positions = {
    "Streptococcus pneumoniae": (95000, 74),
    "Haemophilus influenzae": (15000, 28),
    "Staphylococcus aureus": (2600, 6.0),
    "Pseudomonas aeruginosa": (850, -4.0),
    "Moraxella catarrhalis": (230, 3.0),
}

for _, row in df.iterrows():

    coverage = row["Coverage_Percent"]

    if pd.isna(coverage):
        continue

    pathogen = row["Pathogen"]

    if pathogen not in label_positions:
        continue

    ax.annotate(
        pathogen,
        xy=(
            row["Mapped_Reads"],
            coverage
        ),
        xytext=label_positions[pathogen],
        textcoords="data",
        fontsize=9,
        arrowprops=dict(
            arrowstyle="-",
            linewidth=0.8
        )
    )


ax.set_xscale("log")

ax.set_xlim(
    df["Mapped_Reads"].min() * 0.7,
    df["Mapped_Reads"].max() * 2.0
)

ax.set_xlabel(
    "Mapped reads (log scale)"
)

ax.set_ylabel(
    "Genome coverage (%)"
)

ax.set_ylim(-7, 78)

ax.set_title(
    "Reference-Based Pathogen Evidence: Mapped Reads vs Genome Coverage"
)

ax.grid(
    axis="both",
    alpha=0.25
)


plt.tight_layout()


plt.savefig(
    OUTPUT_FIGURE,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ------------------------------------------------------------
# Console output
# ------------------------------------------------------------

print(
    "Pathogen evidence visualization generated successfully."
)

print(
    f"Saved ranked table: {OUTPUT_TABLE}"
)

print(
    f"Saved figure: {OUTPUT_FIGURE}"
)

print()

print(
    df[
        [
            "Pathogen",
            "Mapped_Reads",
            "Coverage_Percent",
            "Mean_Depth"
        ]
    ].to_string(index=False)
)
