import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Step 1: Load the dataset
df = pd.read_csv('data/diabetes.csv')

# Step 2: Separate features (X) and labels (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

print("Training features:", X.columns.tolist())


# Step 3: Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Save the trained model to the 'models/' folder
with open('models/diabetes_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'diabetes_model.pkl'")
