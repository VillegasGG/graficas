import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('roots-time.xlsx')

promedios = {
    'Sequential': [
        df['time_taken_sec k=1'].mean(), 
        df['time_taken_sec k=2'].mean(), 
        df['time_taken_sec k=3'].mean()
    ],
    'Parallel': [
        df['time_taken_par k=1'].mean(), 
        df['time_taken_par k=2'].mean(), 
        df['time_taken_par k=3'].mean()
    ]
}

k_labels = ['$k = 1$', '$k = 2$', '$k = 3$']
x = np.arange(len(k_labels)) 
width = 0.35  # Ancho de las barras

fig, ax = plt.subplots(figsize=(10, 6))

rects1 = ax.bar(x - width/2, promedios['Sequential'], width, label='Sequential', color='#6c757d')
rects2 = ax.bar(x + width/2, promedios['Parallel'], width, label='Parallel', color='#28a745')

ax.bar_label(rects1, padding=3, fmt='%.3f', fontsize=13, color='black')
ax.bar_label(rects2, padding=3, fmt='%.3f', fontsize=13, color='black')

ax.set_ylabel('Average Execution Time (s)', fontsize=12)
ax.set_xlabel('Lookahead Depth ($k$)', fontsize=12)
# ax.set_title('Comparación de Tiempos de Ejecución: Secuencial vs. Paralelo', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(k_labels, fontsize=12)
ax.legend(fontsize=12)

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('comparacion_tiempos_k_roots.png', dpi=300, bbox_inches='tight')

plt.show()