import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load pathogen summary
# -----------------------------
df = pd.read_csv("results/pathogen_mapping_summary.csv")

# Sort by mapped reads
df = df.sort_values("Mapped_Reads", ascending=True)

# -----------------------------
# Figure 1: Pathogen read counts
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

x = np.log10(df["Mapped_Reads"] + 1)

bars = ax.barh(df["Pathogen"], x)

ax.set_xlabel("log10(mapped reads + 1)")
ax.set_ylabel("Pathogen")
ax.set_title("Targeted Respiratory Pathogen Screening")

# Label actual read counts
for bar, reads in zip(bars, df["Mapped_Reads"]):
    ax.text(
        bar.get_width() + 0.03,
        bar.get_y() + bar.get_height()/2,
        f"{reads:,}",
        va="center",
        fontsize=9
    )

ax.grid(axis="x", alpha=0.25)
plt.tight_layout()

plt.savefig(
    "results/figures/pathogen_screening_read_counts.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# -----------------------------
# Function to load depth data
# -----------------------------
def load_depth(path):
    return pd.read_csv(
        path,
        sep="\t",
        header=None,
        names=["chrom", "position", "depth"]
    )

# -----------------------------
# Figure 2: S. pneumoniae coverage
# -----------------------------
sp = load_depth(
    "results/coverage/streptococcus_pneumoniae.depth.tsv"
)

# Bin genome into 10 kb windows
bin_size = 10000
sp["bin"] = (sp["position"] - 1) // bin_size

sp_binned = (
    sp.groupby("bin")
      .agg(
          position=("position", "mean"),
          mean_depth=("depth", "mean")
      )
      .reset_index()
)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    sp_binned["position"],
    sp_binned["mean_depth"],
    linewidth=1
)

ax.axhline(
    5,
    linestyle="--",
    linewidth=1,
    label="5× depth"
)

ax.axhline(
    10,
    linestyle="--",
    linewidth=1,
    label="10× depth"
)

ax.set_xlabel("Genome position (bp)")
ax.set_ylabel("Mean read depth")
ax.set_title("Genome-wide Read Depth: Streptococcus pneumoniae")

ax.legend()
ax.grid(alpha=0.25)

plt.tight_layout()

plt.savefig(
    "results/figures/streptococcus_pneumoniae_coverage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Figures generated successfully.")
