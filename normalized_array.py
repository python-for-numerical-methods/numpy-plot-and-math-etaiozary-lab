import numpy as np

def normalize_array(arr):
    arr = np.asarray(arr, dtype=float)
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    denom = max_val - min_val
    
    return np.where(denom == 0, 0, (arr - min_val) / denom)
   

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
