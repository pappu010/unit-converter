import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convert():
    try:
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        
        # Simple unit conversion logic (Example: Length conversion)
        conversion_factors = {
            'meters': 1,
            'kilometers': 0.001,
            'centimeters': 100,
            'inches': 39.3701,
            'feet': 3.28084
        }
        
        if from_unit in conversion_factors and to_unit in conversion_factors:
            result = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
            return f"Converted Value: {result:.2f} {to_unit}"
        else:
            return "Invalid units selected."
    except:
        return "Error: Invalid input. Please enter a valid number."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Get the port from environment variables
    app.run(host="0.0.0.0", port=port)  # Bind to 0.0.0.0 for external access
