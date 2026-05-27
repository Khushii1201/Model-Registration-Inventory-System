from flask import Flask, render_template, request
from fraud_model import FraudModel

app = Flask(__name__)

fraud_model = FraudModel()
@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        time = request.form["time"]
        location = request.form["location"]

        prediction = fraud_model.predict(amount)

        result = {
            "Fraud Status": prediction,
            "Risk Level": "High" if prediction == "Fraud" else "Low"
        }
        from data_loader import DataLoader

        @app.route("/train", methods=["POST"])
        def train():
            loader = DataLoader("creditcard.csv")
            data = loader.load_data()

            fraud_model.train_model(data)

            return "✅ Model trained successfully!"

    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
