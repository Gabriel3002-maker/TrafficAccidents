import pyreadstat
df , meta = pyreadstat.read_sav('./assets/2020_SINIESTROS_TRÁNSITO_BDD.sav')

print(df.head())


df.to_csv("./assets/2020_SINIESTROS_TRÁNSITO_BDD.csv" , index=False)

print("Archivo convertido a CSV con éxito.")
