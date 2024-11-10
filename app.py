from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate_bmi():
    try:
        height = float(request.form['height'])
        weight = float(request.form['weight'])

        if height <= 0 or weight <= 0:
            return render_template("error.html", message="Height and weight must be positive numbers.")

        bmi = weight / (height / 100) ** 2

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        return render_template("calculate.html", bmi=round(bmi, 2), category=category)

    except ValueError:
        return render_template("error.html", message="Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    app.run(debug=True)