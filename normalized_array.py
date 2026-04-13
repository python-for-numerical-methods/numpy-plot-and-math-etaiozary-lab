import numpy as np



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
    diff = max_val - min_val
    פרמטרים:
    data (list or np.array): מערך של מספרים.
    if diff == 0:
        return np.zeros_like(arr, dtype=float)
    מחזירה:
    np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
    """
    data = np.array(data)
    # x_norm = (x - min) / (max - min)
    normalized = (arr - min_val) / diff
    pass
    return normalized
   
# --- דוגמאות הרצה ---
test1 = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
test2 = np.array([5, 5, 5, 5])

print(f"Original: {test1} -> Normalized: {normalize_array(test1)}")
print(f"Original: {test2} -> Normalized: {normalize_array(test2)}")

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
