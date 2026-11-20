import pandas as pd
import plotly.express as px

# 1. Lecture du fichier CSV contenant les données de ventes
df = pd.read_csv('ventes.csv')

# 2. Calcul du chiffre d'affaires par commande (quantité * prix unitaire)
df['chiffre_affaires'] = df['qte'] * df['prix']

# --- Tâche A : Calcul du chiffre d'affaires total ---
total_ca = df['chiffre_affaires'].sum()
print("=== Statistiques du Chiffre d'Affaires ===")
print(f"Chiffre d'affaires total : {total_ca} €\n")

# --- Tâche B : Analyse et visualisation par produit ---
df_produit = df.groupby('produit', as_index=False)['chiffre_affaires'].sum()

fig_produit = px.bar(
    df_produit, 
    x='produit', 
    y='chiffre_affaires', 
    title="Chiffre d'affaires par Produit",
    labels={'produit': 'Produit', 'chiffre_affaires': "Chiffre d'affaires (€)"},
    text_auto=True
)
fig_produit.show()
# Sauvegarde du graphique en fichier HTML interactif
fig_produit.write_html("ca_par_produit.html")

# --- Tâche C : Analyse et visualisation par région ---
df_region = df.groupby('region', as_index=False)['chiffre_affaires'].sum()

fig_region = px.bar(
    df_region, 
    x='region', 
    y='chiffre_affaires', 
    title="Chiffre d'affaires par Région",
    labels={'region': 'Région', 'chiffre_affaires': "Chiffre d'affaires (€)"},
    text_auto=True
)
fig_region.show()
# Sauvegarde du graphique en fichier HTML interactif
fig_region.write_html("ca_par_region.html")