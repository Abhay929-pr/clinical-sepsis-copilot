# scripts/data_preprocessing.py
import pandas as pd

def load_and_preprocess_vitals(vitals_path, demographics_path):
    """
    Loads, merges, and preprocesses structured patient data.
    This is a simplified example. Real preprocessing is more complex.
    """
    vitals = pd.read_csv(vitals_path)
    demographics = pd.read_csv(demographics_path)

    vitals['charttime'] = pd.to_datetime(vitals['charttime'])
    
    vitals_pivot = vitals.pivot_table(
        index=['subject_id', 'charttime'], 
        columns='itemid', 
        values='valuenum'
    ).reset_index()

    vitals_pivot = vitals_pivot.sort_values(['subject_id', 'charttime'])

    vitals_resampled = vitals_pivot.groupby('subject_id').resample(
        'H', on='charttime'
    ).mean().fillna(method='ffill')
    
    final_data = pd.merge(vitals_resampled, demographics, on='subject_id')
    
    print("Data preprocessed successfully.")
    return final_data
