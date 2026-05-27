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

        result = fraud_model.analyze_transaction(amount, time, location)

    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)