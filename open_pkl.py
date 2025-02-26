import pickle

# Load the .pkl file
file_path = "artifacts/model.pkl"  # Change to your actual path

with open(file_path, "rb") as file:
    loaded_data = pickle.load(file)

# Print the loaded data
print("\n✅ Loaded Data Type:", type(loaded_data))
print("\n📌 Content Preview:", loaded_data)
