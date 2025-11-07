# [IBM Hackathon] Subject : Finance - Detection of fraudulent bank transactions

## Team N°2
- Alexandre FRANCONY
- Alexandre MOREL
- Raphaël ROUX
- Romain REQUENA
- Adrien SERVAS
- Léonard SEIDLITZ

## Initialization
```
git clone https://github.com/Tailroil/hackaton_finance_team2.git
```
Dans le terminal, à la base du projet:
```
pdm init
```

## Avancement local et intégration watsonX

J'ai préparé une base pour travailler sur la détection de fraudes et pour intégrer IBM watsonX :

- `src/explore.py` : script d'exploration rapide (genère `output/explore_report.txt`).
- `src/watsonx_template.py` : template d'intégration watsonX (exemples et instructions). Définissez `WATSONX_APIKEY` et `WATSONX_URL` dans l'environnement pour utiliser ce template.
- `docs/plan.md` : plan méthodologique (prétraitement, validation cold-start, modèle, métriques, livrables).

Recommandation : lancer l'exploration locale avec :

```zsh
pdm run python src/explore.py
```

Si vous voulez que j'ajoute les dépendances recommandées pour l'exploration et la modélisation (pandas, scikit-learn, lightgbm, matplotlib), je peux exécuter `pdm add` pour les installer dans l'environnement PDM du projet.
