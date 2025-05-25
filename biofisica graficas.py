import pandas as pd
import matplotlib.pyplot as plt

df_con = pd.read_excel(r"C:\Users\a.ricaurte\Desktop\Laurdan_T_2_uM.xlsx")
df_sin = pd.read_excel(r"C:\Users\a.ricaurte\Desktop\Laurdan_T.xlsx")

df_con = df_con.dropna(subset=["Temperatura", "Dato", "Desviación"])
df_sin = df_sin.dropna(subset=["Temperatura", "Dato", "Desviación"])

df_con["Temperatura"] = pd.to_numeric(df_con["Temperatura"], errors="coerce")
df_con["Dato"] = pd.to_numeric(df_con["Dato"], errors="coerce")
df_con["Desviación"] = pd.to_numeric(df_con["Desviación"], errors="coerce")

df_sin["Temperatura"] = pd.to_numeric(df_sin["Temperatura"], errors="coerce")
df_sin["Dato"] = pd.to_numeric(df_sin["Dato"], errors="coerce")
df_sin["Desviación"] = pd.to_numeric(df_sin["Desviación"], errors="coerce")

plt.figure(figsize=(8, 5))
plt.errorbar(df_con["Temperatura"], df_con["Dato"], yerr=df_con["Desviación"], fmt="o", capsize=5, label="+Péptido (20 μL, 0.1 mM)")
plt.xlabel("Temperatura (°C)")
plt.ylabel("GPolarización")
plt.title("+Péptido (20 μL, 0.1 mM)")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.errorbar(df_sin["Temperatura"], df_sin["Dato"], yerr=df_sin["Desviación"], fmt="o", capsize=5, label="Control (sin péptido)", color="red")
plt.xlabel("Temperatura (°C)")
plt.ylabel("GPolarización")
plt.title("Control (sin péptido)")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.errorbar(df_con["Temperatura"], df_con["Dato"], yerr=df_con["Desviación"], fmt="o", capsize=5, label="+Péptido (20 μL, 0.1 mM)", color="blue")
plt.errorbar(df_sin["Temperatura"], df_sin["Dato"], yerr=df_sin["Desviación"], fmt="o", capsize=5, label="Control (sin péptido)", color="red")
plt.xlabel("Temperatura (°C)")
plt.ylabel("GPolarización")
plt.title("Efecto del péptido PIAM 23-4 sobre liposomas modelo de membrana de S. Aureus")
plt.legend()
plt.grid(True)
plt.show()



