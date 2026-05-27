from model_registry import ModelRegistry
from fraud_model import FraudModel
from data_loader import DataLoader

registry = ModelRegistry()
fraud_model = FraudModel()
loader = DataLoader("creditcard.csv")


def main():
    while True:
        print("\n===== Fraud Detection System =====")
        print("1. Register Model")
        print("2. View Inventory")
        print("3. Fraud Check")
        print("4. View Dataset")
        print("5. Test Real Data")
        print("6. Train ML Model")
        print("7. Predict using ML")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Model Name: ")
            version = input("Enter Version: ")
            sponsor = input("Enter Sponsor: ")

            result = registry.register_model(
                name, version, sponsor,
                "Risk", "Fraud", "High", "Production"
            )
            print("\nResult:")
            print(result)

        elif choice == "2":
            models = registry.get_all_models()
            print("\nModel Inventory:")
            if len(models) == 0:
                print("No models found")
            else:
                for m in models:
                    print(m)

        elif choice == "3":
            amount = float(input("Enter Amount: "))
            time = input("Enter Time (Day/Night): ")
            location = input("Enter Location: ")
            result = fraud_model.analyze_transaction(amount, time, location)
            print("\nFraud Result:")
            print(result)


        elif choice == "4":
            data = loader.get_sample(5)
            print("\nDataset Sample:")
            for record in data:
                print(record)
        elif choice == "5":
            data = loader.load_data()
            total = len(data)
            fraud_count = 0
            for record in data[:100]:  # test first 100 records
                result = fraud_model.detect_from_dataset(record)
                if result["Fraud Status"] == "Fraud":
                    fraud_count += 1

            print("\n===== Dataset Analysis =====")
            print("Total Records Checked:", 100)
            print("Fraud Transactions:", fraud_count)
            print("Non-Fraud:", 100 - fraud_count)

        elif choice == "6":

            data = loader.load_data()

            fraud_model.train_simple_model(data)

            print("✅ Model trained successfully")
        elif choice == "7":

            amount = float(input("Enter Amount: "))

            result = fraud_model.predict_fraud(amount)

            print("Prediction:", result)

        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again")
print("\nProcessing Credit Card Dataset...")

if __name__ == "__main__":
    main()
