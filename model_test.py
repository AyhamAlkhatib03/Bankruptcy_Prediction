import unittest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ModelTests(unittest.TestCase):

    def setUp(self):
        # Load data as in the notebook
        df = pd.read_csv("data/american_bankruptcy.csv")  
        df.dropna(inplace=True)
        X = df.drop(["company_name", "status_label"], axis=1)
        y = df["status_label"]

        # Split the data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.3, random_state=42)

        # Train model (Random Forest for this cass here)
        self.model = RandomForestClassifier(random_state=42)
        self.model.fit(self.X_train, self.y_train)
    # Check if there are any null values (which I did but just to make sure)
    def test_data_integrity(self):
        self.assertFalse(self.X_train.isnull().values.any(), "X_train has NaNs")
        self.assertFalse(self.X_test.isnull().values.any(), "X_test has NaNs")
    # Check the model achieves at least 80% accuracy
    def test_model_accuracy(self):
        preds = self.model.predict(self.X_test)
        acc = accuracy_score(self.y_test, preds)
        self.assertGreater(acc, 0.80, f"Accuracy too low: {acc:.2f}")

if __name__ == "__main__":
    unittest.main()
