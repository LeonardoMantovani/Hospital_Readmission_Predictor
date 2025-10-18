import pandas as pd

# A function that maps ICD-9 codes to broad clinical categories
def map_icd9_to_category(code):
   
    if pd.isna(code):
        return 'Missing'
    
    code = str(code)
    
    # Remove any non-numeric characters and get first digits
    if code.startswith('V'):
        return 'Supplementary_V'
    elif code.startswith('E'):
        return 'External_Causes'
    
    # Convert to float for numeric comparison
    try:
        code_num = float(code)
    except:
        return 'Other'
    
    # Map based on ICD-9 ranges
    if 1 <= code_num < 140:
        return 'Infectious_Parasitic'
    elif 140 <= code_num < 240:
        return 'Neoplasms'
    elif 240 <= code_num < 280:
        return 'Endocrine_Metabolic'
    elif 280 <= code_num < 290:
        return 'Blood'
    elif 290 <= code_num < 320:
        return 'Mental'
    elif 320 <= code_num < 390:
        return 'Nervous_System'
    elif 390 <= code_num < 460:
        return 'Circulatory'
    elif 460 <= code_num < 520:
        return 'Respiratory'
    elif 520 <= code_num < 580:
        return 'Digestive'
    elif 580 <= code_num < 630:
        return 'Genitourinary'
    elif 630 <= code_num < 680:
        return 'Pregnancy_Childbirth'
    elif 680 <= code_num < 710:
        return 'Skin'
    elif 710 <= code_num < 740:
        return 'Musculoskeletal'
    elif 740 <= code_num < 760:
        return 'Congenital'
    elif 760 <= code_num < 780:
        return 'Perinatal'
    elif 780 <= code_num < 800:
        return 'Symptoms_Signs'
    elif 800 <= code_num < 1000:
        return 'Injury_Poisoning'
    else:
        return 'Other'


def parse_dosage(value):
    if pd.isna(value):
        return 0
    elif isinstance(value, str) and value.startswith('>'):
        try:
            return float(value[1:])
        except ValueError:
            return np.nan
    elif isinstance(value, float):
        return value
    else:
        return np.nan