import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('compare_results_1_roots.xlsx', sheet_name='gap_greedy')

sns.set_theme(style="whitegrid")
plt.figure(figsize=(9, 6))


ax = sns.boxplot(data=df, palette="Blues", showmeans=True,
                 meanprops={"marker":"x", "markerfacecolor":"red", "markeredgecolor":"red", "markersize": 8})

plt.ylim(0, .06)

plt.title('Optimality Gap Distribution by Root\'s degree for instance set 2, Greedy', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Root\'s degree', fontsize=12, labelpad=10)
plt.ylabel('Optimality Gap (%)', fontsize=12, labelpad=10)

plt.tight_layout()
plt.savefig('boxplot_optimality_gap_greedy_roots.png', dpi=300)
plt.show()