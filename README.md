
# Hackathon — Finance: Fraud Detection (Team 2)

This repository contains the work we produced during the IBM/ESILV Hackathon on detecting fraudulent bank transactions. It includes datasets, preprocessing and modeling notebooks, a small dashboard for visualization, and output predictions used for submission.

## Team
- Alexandre FRANCONY
- Alexandre MOREL
- Raphaël ROUX
- Romain REQUENA
- Adrien SERVAS
- Léonard SEIDLITZ

## Project snapshot / what's included

Top-level folders and key files:

- `Credentials/` — team members' credential stubs (do not commit secrets).
- `Dashboard/` — small static dashboard to view selected visualizations.
	- `Dashboard/index.html` — open in a browser to view the dashboard.
	- `Dashboard/styles.css`, `Dashboard/img/` — assets.
- `data/` — raw and reference data used in analysis and model development
	- `cards_data.csv`
	- `evaluation_features.csv`
	- `mcc_codes.json`
	- `train_fraud_labels.json`
	- `transactions_train.csv`
	- `users_data.csv`
- `notebooks/` — Jupyter notebooks used for exploration, preprocessing and modeling
	- `exploration_fraud.ipynb` — EDA and feature investigation
	- `preprocessing.ipynb` — cleaning and feature engineering steps
	- `model_ML.ipynb` — model training, evaluation and experiments
- `output/` — artifacts and outputs produced by notebooks and scripts
	- `exploration_summary.txt` — short EDA summary
	- `fraud_predictions_submission.csv` — final predictions we produced
	- `processed_data.csv`, `train_processed.csv`, `transactions_labeled_cleaned.csv` — processed datasets
	- `models/` — (if present) saved model files
- `watsonx/` — additional deliverables and reports related to watsonX experiments
	- `Hackathon-finance-viz.ipynb`
	- `Rapport_model.html`

## What we did (short summary)

- Exploratory Data Analysis (EDA): investigated transaction patterns, user profiles and MCC codes to find signals related to fraud. Results summarized in `notebooks/exploration_fraud.ipynb` and `output/exploration_summary.txt`.
- Preprocessing & Feature Engineering: cleaned transactions and users data, merged datasets, engineered features used by models; notebook: `notebooks/preprocessing.ipynb`.
- Modeling: trained and evaluated several ML models (scikit-learn / LightGBM experiments) in `notebooks/model_ML.ipynb`. Best model predictions were exported to `output/fraud_predictions_submission.csv`.
- Visualization & Reporting: a small static dashboard lives in `Dashboard/` for quick local visualization. A watsonX notebook and an HTML report are in `watsonx/`.

Open and run the notebooks in `notebooks/` in the order:
1. `exploration_fraud.ipynb` — run cells to reproduce EDA and plots.
2. `preprocessing.ipynb` — run to generate the processed datasets in `output/`.
3. `model_ML.ipynb` — run to train/evaluate models and produce `fraud_predictions_submission.csv`.

To view the dashboard, open `Dashboard/index.html` in your browser (no server required for the static files).

## Key outputs and where to find them

- Predictions for submission: `output/fraud_predictions_submission.csv`.
- Processed training data: `output/train_processed.csv` and `output/processed_data.csv`.
- Cleaned transactions: `output/transactions_labeled_cleaned.csv`.
- EDA summary: `output/exploration_summary.txt`.
- Visual report and notebook: `watsonx/Rapport_model.html`, `watsonx/Hackathon-finance-viz.ipynb`.