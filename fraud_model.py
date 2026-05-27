class FraudModel:

    def __init__(self):
        pass

    DATASET_CONFIG = {
        "credit_card": {
            "amount": "Amount",
            "label": "Class"
        },
        "otp": {
            "amount": "transaction_amount",
            "label": "fraud_flag",
            "otp_verified": "otp_verified",
            "otp_attempts": "otp_attempts"
        }
    }

    def find_column(record, possible_names):
        for name in possible_names:
            if name in record:
                return record[name]
        return None


    def detect_fraud(self, amount, time, location):

        if amount > 20000:
            return "Fraud"

        if time == "Night" and amount > 10000:
            return "Fraud"

        if location == "Unknown":
            return "Fraud"
        if amount > 50000:
            return "Fraud"

        if amount > 15000 and time == "Night":
            return "Fraud"

        if location.lower() == "unknown":
            return "Fraud"

        return "Not Fraud"

    def calculate_risk(self, amount, fraud_status):

        if fraud_status == "Fraud":
            return "High"

        if amount > 15000:
            return "Medium"

        return "Low"


    def analyze_transaction(self, amount, time, location):

        fraud_status = self.detect_fraud(amount, time, location)
        risk_level = self.calculate_risk(amount, fraud_status)

        return {
            "Fraud Status": fraud_status,
            "Risk Level": risk_level
        }

    def train_simple_model(self, data):

        fraud_amounts = []
        normal_amounts = []

        for record in data:
            try:
                amount = float(record["Amount"])
                label = record["Class"]

                if label == "1":
                    fraud_amounts.append(amount)
                else:
                    normal_amounts.append(amount)

            except:
                continue
        self.avg_fraud = sum(fraud_amounts) / len(fraud_amounts)
        self.avg_normal = sum(normal_amounts) / len(normal_amounts)

    def predict_fraud(self, amount):
        if abs(amount - self.avg_fraud) < abs(amount - self.avg_normal):
            return "Fraud"

        return "Not Fraud"


    def detect_from_dataset(self, record, dataset_type):

        config = DATASET_CONFIG.get(dataset_type)

        if not config:
            return {"Error": "Unknown dataset type"}

        try:
            amount = float(record[config["amount"]])
            fraud_flag = record[config["label"]]

            # Default classification
            if fraud_flag == "1":
                fraud_status = "Fraud"
            else:
                fraud_status = "Not Fraud"

            if dataset_type == "otp":

                otp_verified = record.get(config["otp_verified"], "yes")
                otp_attempts = int(record.get(config["otp_attempts"], 1))

                if otp_verified == "no":
                    fraud_status = "Fraud"

                if otp_attempts > 3:
                    fraud_status = "Fraud"

            risk_level = self.calculate_risk(amount, fraud_status)

            return {
                "Fraud Status": fraud_status,
                "Risk Level": risk_level
            }

        except Exception as e:
            return {"Error": str(e)}
