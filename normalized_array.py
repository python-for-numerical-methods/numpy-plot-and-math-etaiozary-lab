import numpy as np

def normalized_array(input_array):
    data = np.array(input_array)
    if np.all(data == data[0]):
        return np.zeros(data.shape)
    else:
        new_array = (data - np.min(data)) / (np.max(data) - np.min(data))
        
    return new_array

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
