import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('compare_results_3_nodes.xlsx', sheet_name='gaps')

sns.set_theme(style="whitegrid")
plt.figure(figsize=(9, 6))


ax = sns.boxplot(data=df, palette="Blues", showmeans=True,
                 meanprops={"marker":"x", "markerfacecolor":"red", "markeredgecolor":"red", "markersize": 8})

plt.title('Optimality Gap Distribution by Tree Size for instance set 1, k=3', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Tree Size (Number of Nodes)', fontsize=12, labelpad=10)
plt.ylabel('Optimality Gap (%)', fontsize=12, labelpad=10)

plt.tight_layout()
plt.savefig('boxplot_optimality_gap_3_nodes.png', dpi=300)
plt.show()