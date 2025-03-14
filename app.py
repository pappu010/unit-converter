from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Conversion rates for length & weight
conversion_rates = {
    "length": {"km": 1000, "m": 1, "cm": 0.01, "mm": 0.001},
    "weight": {"kg": 1, "g": 0.001, "lb": 0.453592, "oz": 0.0283495}
}

def convert_units(value, from_unit, to_unit, category):
    meters = value * conversion_rates[category][from_unit]
    return meters / conversion_rates[category][to_unit]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    value = float(data["value"])
    from_unit = data["fromUnit"]
    to_unit = data["toUnit"]
    category = data["category"]

    if category in ["length", "weight"]:
        result = convert_units(value, from_unit, to_unit, category)
        return jsonify({"result": round(result, 4)})

    elif category == "temperature":
        if from_unit == "C" and to_unit == "F":
            result = (value * 9/5) + 32
        elif from_unit == "F" and to_unit == "C":
            result = (value - 32) * 5/9
        else:
            result = value
        return jsonify({"result": round(result, 2)})

    return jsonify({"error": "Invalid category"}), 400

if __name__ == "__main__":
    app.run(debug=True)
 
