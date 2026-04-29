import numpy as np

def normalized_array(input_array):
    x = np.array(input_array, dtype=float)
    
    if np.max(x) == np.min(x):
        return np.zeros_like(x)
    
    new_array = (x - np.min(x)) / (np.max(x) - np.min(x))
    return new_array
    
if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
