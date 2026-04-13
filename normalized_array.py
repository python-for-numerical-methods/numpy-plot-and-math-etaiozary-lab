import numpy as np


def normalized_array(data):
    """
    מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.
def normalize_array(arr):
    arr = np.asarray(arr, dtype=float)
    # מציאת ערכי המינימום והמקסימום במערך
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    denom = max_val - min_val
    
    return np.where(denom == 0, 0, (arr - min_val) / denom)

    הנוסחה לביצוע:
    x_norm = (x - min) / (max - min)
    # חישוב המכנה (הטווח)
    diff = max_val - min_val

    פרמטרים:
    data (list or np.array): מערך של מספרים.
    # בדיקה אם כל הערכים שווים כדי למנוע חלוקה באפס
    if diff == 0:
        return np.zeros_like(arr, dtype=float)

    מחזירה:
    np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
    """
    # המרת הקלט ל-numpy array לצורך חישובים וקטוריים
    data = np.array(data)
    # ביצוע הנרמול לפי הנוסחה (פעולה וקטורית)
    # x_norm = (x - min) / (max - min)
    normalized = (arr - min_val) / diff

    # --- כיתבו את הקוד שלכם כאן ---
    pass
    # חשוב לזכור להחליף את pass ב- return
    return normalized

# --- דוגמאות הרצה ---
test1 = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

