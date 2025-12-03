import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel('compare_results_nodes.xlsx', sheet_name='comparaciones')

# Take first 5 rows
results = df.head(6)

# Take 10 to 16 rows to new dataframe
# Column 10 is the new columns names
times = df.iloc[11:17, :]
times.columns = df.iloc[10, :]

# Delete last column
times = times.iloc[:, :-1]
print(results)
print(times)

plt.figure(figsize=(10, 6))

sns.lineplot(data=times, x='Nodos', y='Prom. T-CPU Rollout k=1', 
             marker='o', color='blue', label='Rollout k=1')

sns.lineplot(data=times, x='Nodos', y='Prom. T-CPU Rollout k=1', 
             marker='o', color='green', label='Rollout k=2')

sns.lineplot(data=times, x='Nodos', y='Prom. T-CPU ILP', 
             marker='^', color='orange', label='ILP')

sns.lineplot(data=times, x='Nodos', y='Prom. T-CPU IQCP', 
             marker='s', color='red', label='IQCP')

plt.title('Comparación de Tiempos: Rollout vs Exactos', fontsize=14)
plt.xlabel('Número de Nodos ($n$)', fontsize=12)
plt.ylabel('Tiempo (segundos)', fontsize=12)

plt.legend() 

plt.grid(True)
plt.savefig('nodes_vs_time_comparativo.png')
plt.show()