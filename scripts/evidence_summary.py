import pandas as pd
from pathlib import Path

# ============================================================
# Integrated pathogen evidence summary
# ============================================================

INPUT_COVERAGE = "results/final_pathogen_coverage_summary.csv"
INPUT_ABUNDANCE = "results/pathogen_mapped_read_distribution.csv"

OUTPUT_TABLE = "results/pathogen_evidence_summary.csv"

# ------------------------------------------------------------
# Load input tables
# ------------------------------------------------------------

coverage = pd.read_csv(INPUT_COVERAGE)
abundance = pd.read_csv(INPUT_ABUNDANCE)

# ------------------------------------------------------------
# Keep only additional coverage metrics
# ------------------------------------------------------------

coverage_metrics = coverage[
    [
        "Pathogen",
        "Coverage_Percent",
        "Coverage_5x_Percent",
        "Coverage_10x_Percent",
        "Mean_Depth"
    ]
]

# ------------------------------------------------------------
# Merge abundance and coverage results
# ------------------------------------------------------------

evidence = abundance.merge(
    coverage_metrics,
    on="Pathogen",
    how="left",
    suffixes=("_abundance", "_coverage")
)

evidence["Coverage_Percent"] = evidence["Coverage_Percent_coverage"]
evidence["Mean_Depth"] = evidence["Mean_Depth_coverage"]

evidence = evidence.drop(
    columns=[
        "Coverage_Percent_abundance",
        "Mean_Depth_abundance",
        "Coverage_Percent_coverage",
        "Mean_Depth_coverage"
    ]
)

# ------------------------------------------------------------
# Descriptive evidence interpretation
# ------------------------------------------------------------

def interpret_evidence(row):

    mapped_share = row["Mapped_Read_Share_Percent"]
    coverage_pct = row["Coverage_Percent"]
    mean_depth = row["Mean_Depth"]

    if (
        mapped_share >= 50
        and coverage_pct >= 40
        and mean_depth >= 5
    ):
        return "Strong computational evidence"

    elif (
        mapped_share >= 1
        and coverage_pct >= 10
        and mean_depth >= 0.5
    ):
        return "Secondary / tentative evidence"

    else:
        return "Minimal mapped-read signal"

evidence["Evidence_Interpretation"] = evidence.apply(
    interpret_evidence,
    axis=1
)

# ------------------------------------------------------------
# Sort by mapped-read share
# ------------------------------------------------------------

evidence = evidence.sort_values(
    "Mapped_Read_Share_Percent",
    ascending=False
).reset_index(drop=True)

# ------------------------------------------------------------
# Save integrated evidence table
# ------------------------------------------------------------

Path("results").mkdir(exist_ok=True)

evidence[
    [
        "Pathogen",
        "Mapped_Reads",
        "Mapped_Read_Share_Percent",
        "Coverage_Percent",
        "Coverage_5x_Percent",
        "Coverage_10x_Percent",
        "Mean_Depth",
        "Evidence_Interpretation"
    ]
].to_csv(
    OUTPUT_TABLE,
    index=False
)

# ------------------------------------------------------------
# Console output
# ------------------------------------------------------------

print("Integrated pathogen evidence summary generated successfully.")
print(f"Saved: {OUTPUT_TABLE}")
print()

print(
    evidence[
        [
            "Pathogen",
            "Mapped_Reads",
            "Mapped_Read_Share_Percent",
            "Coverage_Percent",
            "Coverage_5x_Percent",
            "Coverage_10x_Percent",
            "Mean_Depth",
            "Evidence_Interpretation"
        ]
    ].to_string(index=False)
)
