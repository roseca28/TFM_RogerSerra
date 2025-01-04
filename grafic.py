'''
Aquest codi s'ha utilitzat per la representació dels valors de la funció de pèrdua, a partir dels resultats
obtinguts en l'execució de l'entrenament.
'''


import pandas as pd
import matplotlib.pyplot as plt

# Llegeix els tres arxius CSV
csv1 = pd.read_csv("./resultats/SNN_numsteps_25_tau_2.5_Surrogate modificado con slope 5.csv")
csv2 = pd.read_csv("./resultats/SNN_numsteps_25_tau_2.5_Surrogate modificado con slope 25.csv")
csv3 = pd.read_csv("./resultats/SNN_numsteps_25_tau_2.5_Surrogate original.csv")

# Afegeix una columna per identificar cada dataset
csv1['Dataset'] = 'Surrogate modificat amb slope 5'
csv2['Dataset'] = 'Surrogate modificat amb slope 25'
csv3['Dataset'] = 'Surrogate original'

# Combina els tres datasets
combined = pd.concat([csv1, csv2, csv3])

# Crea el gràfic
plt.figure(figsize=(10, 6))
for label, group in combined.groupby('Dataset'):
    plt.plot(group['Step'], group['Value'], label=label)

# Configura el gràfic
plt.xlabel('Step')
plt.ylabel('Valor')
plt.title('Funció de pèrdua per les dades amb Codificació Latency')
plt.legend()
plt.grid(True)

# Mostra el gràfic
plt.show()
