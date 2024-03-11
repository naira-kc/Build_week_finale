import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("climate_change_data.csv")

desc_stats = df.describe()
print(desc_stats)

#selezione le colonne desiderate
emis_selected = df[['Temperature']].sort_values(by='Temperature', ascending=False)
# Calcola la matrice di correlazione tra temperatura, innalzamento del mare, precipitazioni, umidità e velocità del vento
correlation_matrix = df[['Temperature', 'Sea Level Rise', 'Precipitation', 'Humidity', 'Wind Speed']].corr()
# Imposta il colore personalizzato
custom_color = '#22577a'
#immagine
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, vmin=-1, vmax=1, annot=True, cmap=custom_color, fmt=".2f")
plt.title("Correlazione tra temperature e innalzamento dei mari, precipitazioni, Umidità e Velocità del vento")
plt.show()