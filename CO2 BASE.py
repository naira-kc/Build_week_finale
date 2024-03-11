import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("CO2 CON VUOTI.xlsx")

# Analisi minima dei dati
desc_stats = df.describe()
#print(desc_stats)

# Seleziono le colonne relative alla popolazione e alle colonne che contengono CO2 nel nome
colonne_co2 = [colonna for colonna in df.columns if 'co2' in colonna.lower()]
colonne_selezionate = ['population'] + colonne_co2
df_selezionato = df[colonne_selezionate]

# Calcolo la matrice di correlazione
matrice_correlazione = df_selezionato.corr()

# Matrice di correlazione
plt.figure(figsize=(10, 8))
sns.heatmap(matrice_correlazione, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matrice di correlazione tra popolazione e colonne CO2')
plt.show()

# Matrice di correlazione verde come il tema su power BI
plt.figure(figsize=(10, 8))
sns.heatmap(matrice_correlazione, annot=True, cmap='Greens', fmt=".2f")
plt.title('Matrice di correlazione tra popolazione e colonne CO2')
plt.show()

# Seleziono le colonne relative alla popolazione e le colonne che contengono CO2 senza "per_capita"
colonne_co2_senza_per_capita = [colonna for colonna in df.columns if 'co2' in colonna.lower() and 'per_capita' not in colonna.lower()]
colonne_selezionate = ['population'] + colonne_co2_senza_per_capita
df_selezionato = df[colonne_selezionate]

# Calcolo la matrice di correlazione
matrice_correlazione = df_selezionato.corr()

# Matrice di correlazione verde
plt.figure(figsize=(10, 8))
sns.heatmap(matrice_correlazione, annot=True, cmap='Greens', fmt=".2f")
plt.title('Matrice di correlazione tra popolazione e colonne CO2 (senza CO2 per capita)')
plt.show()

# Seleziono le colonne escludendo quelle relative alle emissioni di CO2 per capita
colonne_co2_senza_per_capita = [colonna for colonna in df.columns if 'co2' in colonna.lower() and 'per_capita' not in colonna.lower()]
emis_selected = df[['population'] + colonne_co2_senza_per_capita]

# Calcolo la correlazione
correlation_matrix = emis_selected.corr()[['population']].sort_values(by='population', ascending=False)

# correlazione con un heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, vmin=-1, vmax=1, annot=True, cmap=sns.light_palette("seagreen", as_cmap=True))
plt.title("Correlazione tra popolazione e emissioni di CO2")
plt.show()


# Seleziono le colonne, includendo solo quelle relative alle emissioni di CO2 per capita
colonne_co2_per_capita = [colonna for colonna in df.columns if 'co2' in colonna.lower() and 'per_capita' in colonna.lower()]
emis_per_capita_selected = df[['population'] + colonne_co2_per_capita]

# Calcola la correlazione
correlation_matrix_per_capita = emis_per_capita_selected.corr()[['population']].sort_values(by='population', ascending=False)
#palette
palette = sns.light_palette("seagreen", as_cmap=True)

# Visualizo la correlazione con un heatmap utilizzando la palette di colori inversa
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_per_capita, vmin=-1, vmax=1, annot=True, cmap=palette)
plt.title("Correlazione tra popolazione e emissioni di CO2 per capita")
plt.show()
