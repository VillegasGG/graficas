import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

archivo_excel = 'compare_results_nodes.xlsx'

df_k1 = pd.read_excel(archivo_excel, sheet_name='time1')
df_k2 = pd.read_excel(archivo_excel, sheet_name='time2')
df_k3 = pd.read_excel(archivo_excel, sheet_name='time3')
df_greedy = pd.read_excel(archivo_excel, sheet_name='timegreedy') 

df_k1_long = df_k1.melt(var_name='Tree Size', value_name='Execution Time (s)')
df_k1_long['Algorithm'] = 'Rollout (k=1)'

df_k2_long = df_k2.melt(var_name='Tree Size', value_name='Execution Time (s)')
df_k2_long['Algorithm'] = 'Rollout (k=2)'

df_k3_long = df_k3.melt(var_name='Tree Size', value_name='Execution Time (s)')
df_k3_long['Algorithm'] = 'Rollout (k=3)'

df_greedy_long = df_greedy.melt(var_name='Tree Size', value_name='Execution Time (s)')
df_greedy_long['Algorithm'] = 'Greedy'

df_all = pd.concat([df_k1_long, df_k2_long, df_k3_long, df_greedy_long], ignore_index=True)

df_all['Tree Size'] = pd.to_numeric(df_all['Tree Size'])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

plt.yscale('log')

sns.lineplot(data=df_all, x='Tree Size', y='Execution Time (s)', hue='Algorithm',
             errorbar='sd', marker='o', linewidth=2.5, palette='Set1')

plt.title('Execution Time Comparison (Logarithmic Scale)', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Tree Size', fontsize=12, labelpad=10)
plt.ylabel('Execution Time (seconds)', fontsize=12, labelpad=10)
plt.legend(title='Method', fontsize=10, title_fontsize=11)


plt.tight_layout()
plt.savefig('lineplot_comparison_times_nodes.png', dpi=300)
plt.show()