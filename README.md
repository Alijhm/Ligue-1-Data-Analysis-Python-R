# Ligue 1 Analysis — Python & R

Projet d'analyse statistique des performances des clubs de Ligue 1 de la saison 2010-2011 à 2024-2025.

## Fonctionnement

Le projet repose sur un pipeline en deux étapes :

1. **`main.py`** (Python) — lit les fichiers CSV bruts saison par saison, extrait les statistiques du club choisi et génère un CSV propre dans `data/propre/`
2. **`etude_stats.R`** (R) — lit le CSV propre et produit les visualisations

## Visualisations (ggplot2 & areaplot)
- **Line charts** : évolution des buts marqués et concédés (domicile / extérieur / total) par saison
- **Area chart** : répartition des cartons jaunes et rouges par saison
- **Line chart** : corrélation entre fautes causées et buts concédés
- **Bar chart empilé** : résultats par saison (victoires, nuls, défaites)
- **Bar chart empilé** : précision des tirs (tirs / tirs cadrés / buts) par saison
- **Bar chart empilé** : répartition des fautes à domicile et à l'extérieur

## Technologies
Python · Pandas · R · ggplot2 · areaplot · tidyr

## Données
Fichiers CSV issus des statistiques officielles de Ligue 1, une saison par fichier (de 2010-2011 à 2024-2025).  
Source : à compléter · Licence : à compléter

## Utilisation

**Étape 1 — Générer le CSV propre**
```bash
python main.py
```
Saisir le nom du club que l'on souhaite analyser (ex : `Paris SG`) quand le programme Python le demande.

**Étape 2 — Lancer les visualisations**

Ouvrir `etude_stats.R` dans RStudio et l'exécuter.  
Saisir le même nom de club que l'on a demandé en exécutant le programme Python.
