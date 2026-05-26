class FraudModel:

    def __init__(self):
        pass


    # ✅ Detect fraud using rules
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


    # ✅ Calculate risk level
    def calculate_risk(self, amount, fraud_status):

        if fraud_status == "Fraud":
            return "High"

        if amount > 15000:
            return "Medium"

        return "Low"


    # ✅ Combine fraud + risk
    def analyze_transaction(self, amount, time, location):

        fraud_status = self.detect_fraud(amount, time, location)
        risk_level = self.calculate_risk(amount, fraud_status)

        return {
            "Fraud Status": fraud_status,
            "Risk Level": risk_level
        }


    # ✅ Detect fraud from Kaggle dataset record
    def detect_from_dataset(self, record):

        try:
            amount = float(record["Amount"])
            fraud_flag = record["Class"]

            if fraud_flag == "1":
                fraud_status = "Fraud"
            else:
                fraud_status = "Not Fraud"

            risk_level = self.calculate_risk(amount, fraud_status)

            return {
                "Fraud Status": fraud_status,
                "Risk Level": risk_level
            }

        except Exception as e:
            return {
                "Error": str(e)
            }