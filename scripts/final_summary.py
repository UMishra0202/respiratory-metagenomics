import pandas as pd
from pathlib import Path

samples = {
    "Streptococcus pneumoniae":
        "results/coverage/streptococcus_pneumoniae.depth_q20.tsv",
    "Haemophilus influenzae":
        "results/coverage/haemophilus_influenzae.depth_q20.tsv"
}

rows = []

for pathogen, file in samples.items():

    df = pd.read_csv(
        file,
        sep="\t",
        header=None,
        names=["reference", "position", "depth"]
    )

    total = len(df)
    covered = (df["depth"] > 0).sum()
    cov5 = (df["depth"] >= 5).sum()
    cov10 = (df["depth"] >= 10).sum()

    rows.append({
        "Pathogen": pathogen,
        "Genome_Positions": total,
        "Covered_Positions": covered,
        "Coverage_Percent": covered / total * 100,
        "Coverage_5x_Percent": cov5 / total * 100,
        "Coverage_10x_Percent": cov10 / total * 100,
        "Mean_Depth": df["depth"].mean()
    })

out = pd.DataFrame(rows)

Path("results").mkdir(exist_ok=True)

out.to_csv(
    "results/final_pathogen_coverage_summary.csv",
    index=False
)

print(out.to_string(index=False))
print("\nSaved: results/final_pathogen_coverage_summary.csv")
