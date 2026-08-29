import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

Path("results/figures").mkdir(parents=True, exist_ok=True)

# -----------------------------
# Mapping results
# -----------------------------
mapping = pd.DataFrame({
    "Pathogen": [
        "Streptococcus pneumoniae",
        "Haemophilus influenzae",
        "Staphylococcus aureus",
        "Pseudomonas aeruginosa",
        "Moraxella catarrhalis",
        "Rhinovirus C",
        "SARS-CoV-2",
        "RSV-A",
        "Human metapneumovirus"
    ],
    "Mapped_Reads": [
        168138,
        10557,
        1875,
        711,
        195,
        0,
        0,
        0,
        0
    ]
})

# -----------------------------
# Coverage results
# -----------------------------
coverage = pd.read_csv(
    "results/final_pathogen_coverage_summary.csv"
)

coverage["Short_Name"] = [
    "S. pneumoniae",
    "H. influenzae"
]

# -----------------------------
# Create figure
# -----------------------------
fig, axes = plt.subplots(
    3, 1,
    figsize=(10, 14)
)

# Panel A
plot_mapping = mapping.sort_values(
    "Mapped_Reads",
    ascending=True
)

axes[0].barh(
    plot_mapping["Pathogen"],
    plot_mapping["Mapped_Reads"]
)

axes[0].set_xlabel("Mapped reads")
axes[0].set_ylabel("Pathogen")
axes[0].set_title(
    "A. Targeted Respiratory Pathogen Screening"
)

for i, value in enumerate(plot_mapping["Mapped_Reads"]):
    if value > 0:
        axes[0].text(
            value,
            i,
            f" {value:,}",
            va="center"
        )

# Panel B
axes[1].bar(
    coverage["Short_Name"],
    coverage["Coverage_Percent"]
)

axes[1].set_ylabel("Genome coverage (%)")
axes[1].set_title(
    "B. High-Confidence Genome Coverage (MAPQ ≥20)"
)

for i, value in enumerate(coverage["Coverage_Percent"]):
    axes[1].text(
        i,
        value + 2,
        f"{value:.2f}%",
        ha="center"
    )

axes[1].set_ylim(0, 85)

# Panel C
depth_files = {
    "S. pneumoniae":
        "results/coverage/streptococcus_pneumoniae.depth_q20.tsv",
    "H. influenzae":
        "results/coverage/haemophilus_influenzae.depth_q20.tsv"
}

for label, file in depth_files.items():

    depth = pd.read_csv(
        file,
        sep="\t",
        header=None,
        names=["reference", "position", "depth"]
    )

    # Bin genome into 10 kb windows
    depth["bin"] = (
        (depth["position"] - 1) // 10000
    )

    binned = (
        depth.groupby("bin")
        .agg(
            position=("position", "mean"),
            mean_depth=("depth", "mean")
        )
        .reset_index()
    )

    axes[2].plot(
        binned["position"],
        binned["mean_depth"],
        linewidth=1,
        label=label
    )

axes[2].axhline(
    5,
    linestyle="--",
    linewidth=1,
    label="5× threshold"
)

axes[2].axhline(
    10,
    linestyle=":",
    linewidth=1,
    label="10× threshold"
)

axes[2].set_xlabel("Genome position (bp)")
axes[2].set_ylabel("Mean read depth")
axes[2].set_title(
    "C. Genome-wide Read Depth After MAPQ Filtering"
)

axes[2].legend()
axes[2].grid(alpha=0.25)

plt.tight_layout()

plt.savefig(
    "results/figures/final_pathogen_evidence.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "Final figure generated successfully:"
)
print(
    "results/figures/final_pathogen_evidence.png"
)
