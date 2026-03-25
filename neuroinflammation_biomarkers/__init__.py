"""
neuroinflammation-biomarkers-depression
========================================
Access the Harvard Dataverse dataset DVN/QBQXKL.
DOI: https://doi.org/10.7910/DVN/QBQXKL
Author: Juan Moises de la Serna (ORCID: 0000-0002-8401-8018)

Usage:
    from neuroinflammation_biomarkers import load_dataset, get_biomarker_summary
    df = load_dataset()
    summary = get_biomarker_summary()
"""
from .loader import load_dataset, list_files, get_biomarker_summary, get_doi
__version__ = "1.0.0"
__doi__ = "10.7910/DVN/QBQXKL"
__author__ = "Juan Moises de la Serna"
__all__ = ["load_dataset", "list_files", "get_biomarker_summary", "get_doi"]
