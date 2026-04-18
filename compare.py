import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel('nodes.xlsx', sheet_name='comparaciones')
results = df.head(6)

times = df.iloc[11:17, :]
times.columns = df.iloc[10, :]
times = times.iloc[:, :-1]

times['Nodos'] = pd.to_numeric(times['Nodos'])
times['Prom. T-CPU Rollout k=1'] = pd.to_numeric(times['Prom. T-CPU Rollout k=1'])
# times['Prom. T-CPU Rollout k=2'] = pd.to_numeric(times['Prom. T-CPU Rollout k=2'])
times['Prom. T-CPU ILP'] = pd.to_numeric(times['Prom. T-CPU ILP'])
times['Prom. T-CPU IQCP'] = pd.to_numeric(times['Prom. T-CPU IQCP'])

plt.figure(figsize=(10, 6))

# lines
sns.lineplot(data=times, x='Nodos', y='Prom. T-CPU Rollout k=1', 
             marker='o', color='blue', label='Rollout k=1')
# sns.lineplot(data=times, x='Nodos', y='Prom. T-CPU Rollout k=2', 
#              marker='o', color='green', label='Rollout k=2')

sns.lineplot(data=times, x='Nodos', y='Prom. T-CPU ILP', 
             marker='^', color='orange', label='ILP')

sns.lineplot(data=times, x='Nodos', y='Prom. T-CPU IQCP', 
             marker='s', color='red', label='IQCP')

# labels
offset_y = 0.5 
    
for index, row in times.iterrows():
    y_rollout = row['Prom. T-CPU Rollout k=1']
    y_ilp = row['Prom. T-CPU ILP']
    y_iqcp = row['Prom. T-CPU IQCP']
    
    plt.text(row['Nodos'], y_rollout + (y_rollout * 0.1 + 2.0), 
             f"{y_rollout:.2f}", color='blue', ha='center', va='top', fontsize=8)
    
    plt.text(row['Nodos'] - 1.5, y_ilp, 
             f"{y_ilp:.2f}", color='orange', ha='right', va='center', fontsize=8)
    
    plt.text(row['Nodos'], y_iqcp + (y_iqcp * 0.1 + 0.2), 
             f"{y_iqcp:.2f}", color='red', ha='center', va='bottom', fontsize=8, fontweight='bold')

plt.title('Comparación de Tiempos: Rollout vs Exactos', fontsize=14)
plt.xlabel('Número de Nodos (n)', fontsize=12)
plt.ylabel('Tiempo (segundos)', fontsize=12)

plt.legend() 
plt.grid(True)
plt.savefig('nodes-vs-time-1', dpi=300, bbox_inches='tight')
plt.show()