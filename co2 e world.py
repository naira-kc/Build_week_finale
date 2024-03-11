import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("gdp e CO2 WORLD.csv")

# Rimuovo le righe con valori nulli
df.dropna(inplace=True)
# Calcolo la correlazione tra le colonne GDP e CO2 emissions
correlation = df['gdp'].corr(df['co2'])
print("Correlazione tra GDP e CO2 emissions:", correlation)

# Calcolo i coefficienti della retta di regressione
X = df['gdp']
y = df['co2']
# Calcola i coefficienti della retta di regressione
beta1, beta0 = np.polyfit(X, y, 1)

print("Coefficiente angolare (beta1):", beta1)
print("Termine noto (beta0):", beta0)