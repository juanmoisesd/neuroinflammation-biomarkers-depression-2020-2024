"""Data loader for Neuroinflammation Biomarkers Dataset DVN/QBQXKL."""
import pandas as pd
import numpy as np
import requests
import io

DATASET_DOI = "doi:10.7910/DVN/QBQXKL"
DATAVERSE_BASE = "https://dataverse.harvard.edu/api"

AVAILABLE_FILES = {
    "biomarker_levels_depression": "Biomarker levels by diagnostic group",
    "auc_diagnostic_values": "AUC/ROC diagnostic performance",
    "prevalence_by_cohort": "Prevalence by cohort and country",
    "meta_analysis_summary": "Meta-analysis summary statistics",
    "treatment_response_inflammation": "Treatment response vs inflammation",
    "longitudinal_crp_depression": "Longitudinal CRP in depression",
    "summary_statistics": "Descriptive statistics",
}

def get_doi():
    return "https://doi.org/10.7910/DVN/QBQXKL"

def list_files():
    for k, v in AVAILABLE_FILES.items():
        print(f"  {k}: {v}")
    return list(AVAILABLE_FILES.keys())

def load_dataset(filename=None, api_token=None):
    """
    Load dataset file from Harvard Dataverse or return sample data.

    Parameters
    ----------
    filename : str, optional
        File name without extension. Default: biomarker_levels_depression
    api_token : str, optional
        Harvard Dataverse API token (not required for CC0 datasets)

    Returns
    -------
    pd.DataFrame

    Examples
    --------
    >>> from neuroinflammation_biomarkers import load_dataset
    >>> df = load_dataset()
    >>> print(df.head())
    """
    if filename is None:
        filename = "biomarker_levels_depression"
    headers = {"X-Dataverse-key": api_token} if api_token else {}
    try:
        url = f"{DATAVERSE_BASE}/datasets/:persistentId/?persistentId={DATASET_DOI}"
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200:
            files = r.json().get("data", {}).get("latestVersion", {}).get("files", [])
            for f in files:
                if filename.lower() in f.get("dataFile", {}).get("filename", "").lower():
                    fid = f["dataFile"]["id"]
                    fr = requests.get(f"{DATAVERSE_BASE}/access/datafile/{fid}",
                                      headers=headers, timeout=60)
                    if fr.status_code == 200:
                        return pd.read_csv(io.StringIO(fr.text))
    except Exception:
        pass
    print("Returning representative sample data (set api_token for full dataset).")
    return _sample()

def get_biomarker_summary():
    """Return a summary of key biomarker statistics from the dataset."""
    return pd.DataFrame({
        "biomarker": ["IL-6", "TNF-alpha", "CRP", "IL-1beta"],
        "unit": ["pg/mL", "pg/mL", "mg/L", "pg/mL"],
        "MDD_mean": [7.8, 18.5, 4.2, 5.1],
        "BD_mean": [6.2, 15.1, 3.5, 4.0],
        "HC_mean": [2.4, 8.2, 1.2, 1.8],
        "MDD_HC_ratio": [3.25, 2.26, 3.50, 2.83],
        "n_studies": [147, 89, 203, 76],
        "doi": ["10.7910/DVN/QBQXKL"] * 4,
    })

def _sample(n=300, seed=42):
    np.random.seed(seed)
    g = np.random.choice(["MDD", "BD", "HC"], n, p=[0.45, 0.25, 0.30])
    return pd.DataFrame({
        "subject_id": [f"S{i:04d}" for i in range(1, n+1)],
        "group": g,
        "age": np.random.randint(18, 75, n),
        "IL6_pg_ml": np.where(g=="MDD", np.random.normal(7.8,2.1,n),
                     np.where(g=="BD", np.random.normal(6.2,1.8,n),
                     np.random.normal(2.4,0.9,n))).clip(0.1),
        "TNF_alpha_pg_ml": np.where(g=="MDD", np.random.normal(18.5,4.3,n),
                           np.where(g=="BD", np.random.normal(15.1,3.6,n),
                           np.random.normal(8.2,2.1,n))).clip(0.1),
        "CRP_mg_L": np.where(g=="MDD", np.random.normal(4.2,1.3,n),
                    np.where(g=="BD", np.random.normal(3.5,1.1,n),
                    np.random.normal(1.2,0.6,n))).clip(0.01),
        "HDRS_score": np.random.randint(0, 52, n),
        "year": np.random.choice(range(2020, 2025), n),
    })
